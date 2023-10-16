from typing import Any

from fastapi import APIRouter

from src.api.endpoints import todos

api_router = APIRouter()
api_router.include_router(todos.router, prefix="/todos", tags=["Todos"])


@api_router.get("/health", tags=["Health"])
def get_health() -> Any:
    return {"status": "OK"}
