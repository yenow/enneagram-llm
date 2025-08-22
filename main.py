from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from app.api.router import router as api_router

# Load environment variables from .env file
load_dotenv()

app = FastAPI(title="Enneagram LLM Project")

# Define allowed origins
origins = [
    "http://localhost:3000",
    # Add other origins here if needed, e.g., your production frontend URL
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# API routers
app.include_router(api_router, prefix="/api", tags=["LLM"])