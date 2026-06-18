from fastapi import FastAPI

from src.web.routes.pdf_routes import router

app = FastAPI()

from src.logging import logger

logger.info("Application started successfully.")

app.include_router(router)