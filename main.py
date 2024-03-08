from fastapi import FastAPI
from db import Session,engine,Base
from routes import events as event_routes
from routes import user as user_routes
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(event_routes.router,prefix="/api")
app.include_router(user_routes.router,prefix="/api")
