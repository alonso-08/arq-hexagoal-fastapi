from typing import Union
import sys
print("algo pasa",sys.path)
from fastapi import FastAPI

# from event_management.controllers.event_controller import app as event_app
from controllers.event_controller import router as event_app
app = FastAPI()


app.include_router(event_app)