from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.middleware.access_middle import AccessMiddleware


def register_middleware(app):
    app.add_middleware(AccessMiddleware)
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            # allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
