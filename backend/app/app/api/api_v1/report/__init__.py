from typing import Any, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.api.api_v1.report.gen_report import Report

from fastapi.responses import FileResponse,StreamingResponse
router = APIRouter()



@router.get("/report/template/{excel_name}",tags=["report"])
def read_routes(db: Session = Depends(deps.get_db),
                excel_name: Optional[str] = None,
                # current_user: models.User = Depends(deps.get_current_active_user)
                ) -> Any:
    """
    Retrieve Mock Data.
    """
    report =  Report(code=excel_name,).module
    bio =  report.get_template()
    file_name = report.file_name.encode('utf-8').decode('latin1')
    return StreamingResponse(bio,headers={'Content-Disposition':f'attachment; filename={file_name}.xlsx'})



