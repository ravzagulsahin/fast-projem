from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root(a:int,
    b:int,
    isim:str):
    result = a*b
    return { f"hello {isim} {result}"}

            