from fastapi import FastAPI

files = FastAPI()

@files.get("/")
def get_files():
    return {
        "Hello": "Here are your files"
    }
