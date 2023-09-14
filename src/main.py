from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.modules.v1.router.index import router


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

    # endpoint of application
    application.include_router(router)

    return application


api = get_application()
