from pydantic import BaseModel, Field

class LlmRequest(BaseModel):
    query: str = Field(..., description="The prompt to send to the LLM.", min_length=1)
    temperature: float = Field(0.7, description="The temperature for the LLM response.", ge=0.0, le=1.0)

class LlmResponse(BaseModel):
    response: str
    model_used: str
