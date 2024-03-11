from fastapi import FastAPI
from db import Session,engine,Base
from routes import events as event_routes
from routes import user as user_routes
from fastapi.middleware.cors import CORSMiddleware
Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "http://localhost:3000",  # Assuming your frontend runs on localhost:3000

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of origins that are allowed to make requests.
    allow_credentials=True,  # Whether to support cookies in the requests.
    allow_methods=["*"],  # Specify which method are allowed.
    allow_headers=["*"],  # Specify which headers are allowed.
)
app.include_router(event_routes.router,prefix="/api")
app.include_router(user_routes.router,prefix="/api")
