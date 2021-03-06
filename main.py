import uvicorn as uvicorn
from fastapi import FastAPI

from routes.weather import weather

API_description = """ 
**Vulcano-Weather API helps Vulcano people to know the weather 
of the planet in the next 10 years before it was destroyed by Nero**

In this swagger doc you can see the API Documentation and the different routes

Enjoy it..
"""

app = FastAPI(title="Vulcano Weather",
              description=API_description,
              version="1.0",
              contact={
                  "name": "Angel Racini",
                  "url": "https://github.com/arracinim/vulcano-weather",
                  "email": "angelricardoracinimeza@gmail.com"
              })

app.include_router(weather)


@app.get("/", name= "Health Check",
         summary= "Check if the API is UP",
         tags=["Health Check"],
         responses={
             200: {
                 "content": {
                     "application/json": {
                         "example": {"health_check": "up"}
                     }}}}
         )
def health_check():
    return {"health_check": "up"}