from fastapi import APIRouter
from .polls.api_router import router as polls_router

router = APIRouter(prefix="/v1")
router.include_router(polls_router)
