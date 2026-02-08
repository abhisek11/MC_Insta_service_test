from fastapi import FastAPI
from mangum import Mangum
from app.api.routes import router

app=FastAPI(title="Scalable Image Service")
app.include_router(router)

handler=Mangum(app)
