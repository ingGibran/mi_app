from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def main():
    print("Mi BOMBOOOOOO")
    return "Mi Bomboooooo"

@app.get("/sum")
def sum(a: int, b: int):
    return a + b


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )