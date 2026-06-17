from fastapi import FastAPI

from src.web.routes.pdf_routes import router

app = FastAPI()

app.include_router(router)