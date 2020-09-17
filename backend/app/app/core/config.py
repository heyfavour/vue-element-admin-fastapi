import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator


class Settings():
    API_V1_STR: str = ""
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    # SERVER_NAME: str
    # SERVER_HOST: str = "smtp.qq.com"
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["*"]

    # @validator("BACKEND_CORS_ORIGINS", pre=True)
    # def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
    #     if isinstance(v, str) and not v.startswith("["):
    #         return [i.strip() for i in v.split(",")]
    #     elif isinstance(v, (list, str)):
    #         return v
    #     raise ValueError(v)

    PROJECT_NAME: str = "Vue-Element-Admin-Fastapi"
    # SENTRY_DSN: Optional[HttpUrl] = None

    # @validator("SENTRY_DSN", pre=True)
    # def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
    #     if len(v) == 0:
    #         return None
    #     return v

    POSTGRES_SERVER: str = "49.235.242.224:3306"
    POSTGRES_USER: str = "root"
    POSTGRES_PASSWORD: str = "wzx940516"
    POSTGRES_DB: str = "DWDB"
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = "mysql://root:wzx940516@49.235.242.224/DWDB?charset=utf8"

    # @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    # def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
    #     if isinstance(v, str):
    #         return v
    #     return PostgresDsn.build(
    #         scheme="mysql",
    #         user="root",
    #         password="wzx@940516",
    #         host="49.235.242.224",
    #         path=f"/{'DWDB' or ''}",
    #     )

    SMTP_TLS: bool = False
    SMTP_PORT: Optional[int] = 587
    SMTP_HOST: Optional[str] = "smtp.qq.com"
    SMTP_USER: Optional[str] = "619511821@qq.com"
    SMTP_PASSWORD: Optional[str] = "efgjrswetsnybdif"
    EMAILS_FROM_EMAIL: Optional[EmailStr] = "619511821@qq.com"
    EMAILS_FROM_NAME: Optional[str] = "Mr.Wang"

    # # @validator("EMAILS_FROM_NAME")
    # def get_project_name(cls, v: Optional[str], values: Dict[str, Any]) -> str:
    #     if not v:
    #         return values["PROJECT_NAME"]
    #     return v
    #
    # EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEMPLATES_DIR: str = "app/email-templates/build"
    EMAILS_ENABLED: bool = True
    #
    @validator("EMAILS_ENABLED", pre=True)
    def get_emails_enabled(cls, v: bool, values: Dict[str, Any]) -> bool:
        return bool(values.get("SMTP_HOST") and values.get("SMTP_PORT") and values.get("EMAILS_FROM_EMAIL"))

    FIRST_SUPERUSER: str = "admin"
    FIRST_SUPERUSER_EMAIL: str = "619511821@qq.com"
    FIRST_SUPERUSER_PASSWORD: str =  "qwe123"
    USERS_OPEN_REGISTRATION: bool = False

    class Config:
        case_sensitive = True


settings = Settings()
