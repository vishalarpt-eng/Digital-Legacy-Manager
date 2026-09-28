from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4

from src.storage import load_assets, save_assets

app = FastAPI(
    title="Digital Legacy Manager",
    description="A demonstration API for managing digital assets and beneficiaries",
    version="1.0.0"
)


class Asset(BaseModel):
    owner: str
    asset_name: str
    asset_type: str
    beneficiary: str


class DigitalWill(BaseModel):
    owner: str
    beneficiary: str
    transfer_condition: str


@app.get("/")
def home():
    return {
        "message": "Welcome to Digital Legacy Manager",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/assets")
def create_asset(asset: Asset):
    assets = load_assets()

    new_asset = {
        "id": str(uuid4()),
        "owner": asset.owner,
        "asset_name": asset.asset_name,
        "asset_type": asset.asset_type,
        "beneficiary": asset.beneficiary
    }

    assets.append(new_asset)
    save_assets(assets)

    return {
        "message": "Digital asset created successfully",
        "asset": new_asset
    }


@app.get("/assets")
def get_assets():
    return load_assets()


@app.get("/assets/{asset_id}")
def get_asset(asset_id: str):
    assets = load_assets()

    for asset in assets:
        if asset["id"] == asset_id:
            return asset

    raise HTTPException(
        status_code=404,
        detail="Asset not found"
    )


@app.post("/will")
def create_will(will: DigitalWill):
    return {
        "message": "Digital will created successfully",
        "will": will.model_dump()
    }
