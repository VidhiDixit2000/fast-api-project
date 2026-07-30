from pydantic import BaseModel

class product(BaseModel):
    id: float
    name: str
    description: str
    price: float
    quantity: int
    
