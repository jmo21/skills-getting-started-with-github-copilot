"""
Shared pytest fixtures and configuration for API tests.
"""
import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Provide a TestClient for making requests to the FastAPI app."""
    return TestClient(app)


@pytest.fixture
def reset_activities():
    """Reset activities to a known state before each test.
    
    Yields the activities dictionary, then restores it after the test.
    """
    # Save original state
    original_activities = {
        name: {
            "description": details["description"],
            "schedule": details["schedule"],
            "max_participants": details["max_participants"],
            "participants": details["participants"].copy(),
        }
        for name, details in activities.items()
    }

    # Yield to test
    yield activities

    # Restore original state
    for name in activities:
        activities[name]["participants"] = original_activities[name]["participants"].copy()
