import pytest
from fastapi.testclient import TestClient
import random as r


def test_api_random_values():
    client = TestClient
    for _ in range(100):
        a = r.randint(-30, 30)
        b = r.randint(-30, 30)
    
    