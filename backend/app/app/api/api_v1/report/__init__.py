from typing import Any

from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse

from app.api import deps
from app.api.api_v1.report.gen_report import Report

router = APIRouter()


@router.get("/report/excel_generate/{excel_name}", tags=["report"])
def excel_generate(*, excel_name: str = "", request: Request, db: Session = Depends(deps.get_db)) -> Any:
    """
    通过动态import的形式，统一处理excel:模板下载/数据导出
    """
    report = Report(code=excel_name, query_params=request.query_params).module
    if request.query_params.get("template", "1") == "1":
        bio = report.get_template()  # 模板
    else:
        bio = report.get_instance(db)  # 实例
    file_name = report.file_name.encode('utf-8').decode('latin1')
    headers = {
        'Access-Control-Expose-Headers': 'content-disposition',
        'Content-Disposition': f'attachment; filename={file_name}.xlsx'
    }
    return StreamingResponse(bio, headers=headers)
