from fastapi import FastAPI
from app.core.dataBase import Base, engine
from app.routes.productRoute import router as product_router
from app.handlers.register import register_exception_handlers


app = FastAPI(
    title="Stock Flow API", description="API para controle de estoque", version="1.0.0"
)

register_exception_handlers(app)


Base.metadata.create_all(bind=engine)

app.include_router(product_router)


@app.get("/")
def read_root():
    return {"message": "Stock Flow API is running!", "version": "1.0.0"}
