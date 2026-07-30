from fastapi import Depends,FastAPI
from fastapi.middleware.cors import CORSMiddleware
from module import product 
import database_module
from database import SessionLocal,engine
from sqlalchemy.orm import Session


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
   
)
database_module.Base.metadata.create_all(bind=engine)

PRODUCTS=[
   product(id=1, name="Product 1", description="Description of Product 1", price=10.99, quantity=100),
   product(id=7, name="Product 2", description="Description of Product 2", price=15.99, quantity=50),
   product(id=3, name="Product 3", description="Description of Product 3", price=20.99, quantity=25)
]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = SessionLocal()
    count=db.query(database_module.product).count()

    if count==0:
        try:
        # Add initial products to the database
            for p in PRODUCTS:
                db.add(database_module.product(**p.model_dump()))
                db.commit()
        finally:
                db.close()
                print("db closed")
init_db()

@app.get("/")
def greet():
   return "Hello, welcome to the program!"

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    #db=SessionLocal()
    #db.query()
    db_product=db.query(database_module.product).all()
    return db_product


@app.get("/products/{id}")
def get_productbyid(id: int, db: Session = Depends(get_db)):

    db_product=db.query(database_module.product).filter(database_module.product.id==id).first()
    if db_product:
        return db_product
    return {"message": "Product not found"}

@app.post("/products")
def postproducts(PRODUCT: product, db: Session = Depends(get_db)):
    db.add(database_module.product(**PRODUCT.model_dump()))
    db.commit()
    return PRODUCT

@app.put("/products/{id}")
def update_product(
    id: int,
    updated_product: product,
    db: Session = Depends(get_db)
):
    db_product = db.query(database_module.product).filter(
        database_module.product.id == id
    ).first()

    if db_product:
        """ db_product = updated_product, we cant use this coz db_product = updated_product is valid Python syntax, but it is not the correct way to update a database record. It only changes the local Python reference; it does not modify the ORM object being tracked by SQLAlchemy. Therefore, commit() finds no changes in the tracked entity and no UPDATE query is executed.

One possible alternative is merge(), which copies the state of an ORM object into the tracked entity. However, merge() only accepts SQLAlchemy ORM objects. In FastAPI, request bodies are Pydantic models, not ORM models, so merge(updated_product) raises an UnmappedInstanceError. We also cannot declare the request body as an ORM model because FastAPI expects Pydantic models for request validation and OpenAPI schema generation.

Therefore, the correct approach is to update the fields of the tracked ORM object individually , that is """
        db_product.name = updated_product.name
        db_product.description = updated_product.description
        db_product.price = updated_product.price
        db_product.quantity = updated_product.quantity
        db.commit()
        return "Product updated successfully"

    return "Product not found"


@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    
    print("DELETE endpoint called")
    db_product = db.query(database_module.product).filter(database_module.product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product deleted successfully"
        
    return  "Product not found"
            


     