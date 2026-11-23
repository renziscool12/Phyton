from fastapi import FastAPI
from LibraryManagementSystem.Routes.book_routes import router

app = FastAPI()
app.include_router(router)
