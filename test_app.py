from fastapi.testclient import TestClient
from src.app import app
from src import storage

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_create_asset(monkeypatch):
    assets = []

    monkeypatch.setattr(storage, "load_assets", lambda: assets)
    monkeypatch.setattr(storage, "save_assets", lambda data: None)

    response = client.post(
        "/assets",
        json={
            "owner": "Vishal",
            "asset_name": "Sample Document",
            "asset_type": "Document",
            "beneficiary": "Demo Beneficiary"
        }
    )

    assert response.status_code == 200
    assert response.json()["asset"]["asset_name"] == "Sample Document"


def test_create_will():
    response = client.post(
        "/will",
        json={
            "owner": "Vishal",
            "beneficiary": "Demo Beneficiary",
            "transfer_condition": "After verification"
        }
    )

    assert response.status_code == 200
    assert response.json()["will"]["beneficiary"] == "Demo Beneficiary"