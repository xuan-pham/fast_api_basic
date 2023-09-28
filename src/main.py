from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware
from .modules.v1.router import router
from .config.index import config


def get_application() -> FastAPI:
    application = FastAPI(title="ENE Homepage Renewal API")

    # setup CORS
    application.add_middleware(
        CORSMiddleware,
        allow_origins='*',
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_middleware(DBSessionMiddleware, db_url=config.DATABASE_URL)

    # endpoint of application
    application.include_router(router)

    return application


api = get_application()
