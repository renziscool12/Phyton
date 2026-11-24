from fastapi import FastAPI
from Routes.Stadent_Routes import router

app = FastAPI()
app.include_router(router)
