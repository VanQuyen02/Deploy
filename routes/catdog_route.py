import sys
from pathlib import Path
from fastapi import File, UploadFile, APIRouter
from schemas.catdog_schema import CatDogResponse
from config.catdog_cfg import ModelConfig
from models.catdog_predictor import Predictor

# Add the parent directory to the system path
sys.path.append(str(Path(__file__).parent))

# Initialize router and predictor
router = APIRouter()
predictor = Predictor(
    model_name=ModelConfig.MODEL_NAME,
    model_weight=ModelConfig.MODEL_WEIGHT,
    device=ModelConfig.DEVICE
)

@router.post("/predict")
async def predict(file_upload: UploadFile = File(...)):
    response = await predictor.predict(file_upload.file)
    return CatDogResponse(**response)
