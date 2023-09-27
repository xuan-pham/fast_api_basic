from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.modules.v1.router.index import router
from fastapi_sqlalchemy import DBSessionMiddleware
from src.config.index import config


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
