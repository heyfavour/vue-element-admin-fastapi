from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


#重写异常
def register_exception(app: FastAPI):
    @app.exception_handler(Exception)
    async def unicorn_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=418,
            content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
        )

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request, exc):
        return PlainTextResponse(str(exc.detail), status_code=exc.status_code)
