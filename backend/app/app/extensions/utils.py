import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, Optional

import emails
from emails.template import JinjaTemplate
from jose import jwt

from app.core.config import settings


def send_email(email_to: str, subject_template: str = "", html_template: str = "",
               environment: Dict[str, Any] = {}, ) -> None:
    assert settings.EMAILS_ENABLED, "no provided configuration for email variables"
    message = emails.Message(
        subject=JinjaTemplate(subject_template),
        html=JinjaTemplate(html_template),
        mail_from=(settings.EMAILS_FROM_NAME, settings.EMAILS_FROM_EMAIL),
    )
    smtp_options = {"host": settings.SMTP_HOST, "port": settings.SMTP_PORT}
    if settings.SMTP_TLS: smtp_options["tls"] = True
    if settings.SMTP_USER: smtp_options["user"] = settings.SMTP_USER
    if settings.SMTP_PASSWORD: smtp_options["password"] = settings.SMTP_PASSWORD
    response = message.send(to=email_to, render=environment, smtp=smtp_options)
    logging.info(f"send email result: {response}")
    assert response.status_code == 250


def send_test_email(email_to: str) -> None:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name}-Test"
    with open(Path(settings.EMAIL_TEMPLATES_DIR) / "test_email.html") as f: template_str = f.read()
    send_email(
        email_to=email_to,
        subject_template=subject,  # 主题
        html_template=template_str,
        environment={
            "project_name": settings.PROJECT_NAME,
            "email": email_to,
            "msg": "这是一封测试邮件",
            "emails_from_name": "Mr.Wang"
        },  # html template parameters
    )


def send_reset_password_email(email_to: str, email: str, token: str) -> None:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - Password recovery for user {email}"
    with open(Path(settings.EMAIL_TEMPLATES_DIR) / "reset_password.html") as f:
        template_str = f.read()
    server_host = settings.SERVER_HOST
    link = f"{server_host}/reset-password?token={token}"
    send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={
            "project_name": settings.PROJECT_NAME,
            "username": email,
            "email": email_to,
            "valid_hours": settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS,
            "link": link,
        },
    )


def send_new_account_email(email_to: str, username: str, password: str) -> None:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - New account for user {username}"
    with open(Path(settings.EMAIL_TEMPLATES_DIR) / "new_account.html") as f:
        template_str = f.read()
    link = settings.SERVER_HOST
    send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={
            "project_name": settings.PROJECT_NAME,
            "username": username,
            "password": password,
            "email": email_to,
            "link": link,
        },
    )


def generate_password_reset_token(email: str) -> str:
    delta = timedelta(hours=settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": email}, settings.SECRET_KEY, algorithm="HS256",
    )
    return encoded_jwt


def verify_password_reset_token(token: str) -> Optional[str]:
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        return decoded_token["email"]
    except jwt.JWTError:
        return None


def list_to_tree(node_list, root_id=None, *, order="", exclude=None):
    """
        将list转成树结构 list = [{id:xx,parent_id:xx,},id:xx,parent_id:xx,},id:xx,parent_id:xx,}]
        :param root_id  返回选择的id结点  order    排序字段   exclude  剔除某个节点
    """
    if not node_list: return []
    # 排序
    if order: node_list.sort(key=lambda k: k.get(order))
    # node
    node_dict = {node["id"]: node if node.get("parent_id") else node.update({"parent_id": -1}) or node for node in
                 node_list}
    # children
    for node in node_list:
        if node["id"] == exclude: continue
        node_dict.setdefault(node["parent_id"], {}).setdefault("children", []).append(node)
    if root_id:
        return node_dict[root_id]
    return node_dict.get(-1, {}).get("children", [])


def dfs_tree_to_list(nodes):
    """
    将树结构转成list
    :param nodes:
    :return:
    """
    ids = []
    for node in nodes:
        ids.append(node["id"])
        children = node.get("children", [])
        if children != []: ids = ids + dfs_tree_to_list(children)
    return ids


def round_float(float_num, num=2):
    """
    四舍五入
    :param float_num:
    :param num:
    :return:
    """
    import decimal
    context = decimal.getcontext()
    context.rounding = decimal.ROUND_HALF_UP
    return float(round(decimal.Decimal(str(float_num)), num))
