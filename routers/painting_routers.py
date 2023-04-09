from fastapi import APIRouter

router = APIRouter(
    prefix="/paintings"
)

# Gets all paintings
@router.get("/")
async def get_paintings():
    return {"hello", "angus"}
