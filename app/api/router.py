from fastapi import APIRouter

router = APIRouter()

@router.get("/llm")
def llm_endpoint():
    return {"message": "This is the LLM endpoint."}
