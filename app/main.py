import uvicorn as uvicorn
from fastapi import FastAPI

from app.routes.weather import weather

API_description = """ 
**Vulcano-Weather API helps Vulcano people to know the weather of the planet in the next 10 years**
"""

app = FastAPI(title="Vulcano Weather",
              description=API_description,
              version="1.0",
              contact={
                  "name": "Angel Racini",
                  "url": "https://github.com/arracinim/vulcano-weather",
                  "email": "angelricardoracinimeza@gmail.com"
              }, )

app.include_router(weather)


@app.get("/")
def health_check():
    return {"health_check": "up"}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8082)
