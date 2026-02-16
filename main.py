from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root(a:int,
    b:int,
    isim:str,char:str,pat:int):
    result = a*b
    c = char
    return {"message": f"hello {char} {isim} {result}"}

            