from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from actions.replicate_actions import generate_flux_image
import uvicorn

# Add these lines for debugging
import os
print(f"REPLICATE_API_TOKEN: {os.getenv('REPLICATE_API_TOKEN')}")

app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory=".")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate-image")
async def generate_image(request: Request):
    data = await request.json()
    prompt = data.get("prompt")
    output = await generate_flux_image(prompt)
    return JSONResponse(content={"image_url": output[0]})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)