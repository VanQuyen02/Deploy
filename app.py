import sys
from pathlib import Path
from fastapi import FastAPI
from middleware import LogMiddleware, setup_cors
from routes.base import router
import uvicorn

try:
    # # Add the parent directory to the system path
    sys.path.append(str(Path(__file__).parent))

    # Create a FastAPI application instance
    app = FastAPI()

    # Add middleware for logging
    app.add_middleware(LogMiddleware)

    # Set up CORS
    setup_cors(app)

    # Include the router
    app.include_router(router)

except Exception as e:
    print(f"An error occurred: {e}")


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
