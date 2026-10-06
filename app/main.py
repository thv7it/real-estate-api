from fastapi import FastAPI

from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.properties import router as properties_router


app = FastAPI(
    title="Real Estate API",
    description="Backend API for a real estate agency",
    version="1.0.0",
)



app.include_router(auth_router)
app.include_router(users_router)
app.include_router(properties_router)



@app.get("/")
async def root():
    return {"message": "Real Estate API is working"}

