from fastapi import FastAPI
import os

# 建立 FastAPI 應用
app = FastAPI(title="我的第一個 FastAPI")

# 定義一個 GET 路由
@app.get("/")
def read_root():
    return {
        "message": "Hello FastAPI!",
        "DB_HOST" : os.getenv("DATABASE_HOST"),
        "DB_PORT": os.getenv("DATABASE_PORT"),
        "log_level": os.getenv("LOG_LEVEL"),
        "DB_name": os.getenv("DATABASE_USER"),
        "DB_pass": os.getenv("DATABASE_PASSWORD"),
        "api_key": os.getenv("API_KEY"),
        "version": "v3"
    }

# 定義一個帶參數的路由
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}
