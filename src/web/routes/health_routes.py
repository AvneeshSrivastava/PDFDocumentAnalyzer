from fastapi import APIRouter

# ==========================================================
# Router Configuration
# ==========================================================

router = APIRouter()


# ==========================================================
# Health Check Endpoint
# ==========================================================

@router.get(
    "/health",
    tags=["Health"]
)
async def health_check() -> dict:
    """
    Check whether the application is running successfully.

    Returns
    -------
    dict
        Application health status.
    """

    return {
        "status": "healthy"
    }