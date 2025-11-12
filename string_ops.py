from fastapi import FastAPI


app = FastAPI()

@app.get("reverse/{text}")
def reverse_str(text: str):
    return { "original": text, "reversed_text": text[::-1] }
