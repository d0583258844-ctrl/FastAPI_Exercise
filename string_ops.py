from fastapi import FastAPI


app = FastAPI()

@app.get("/reverse/{text}")
def reverse_str(text: str):
    return { "original": text, "reversed_text": text[::-1]}


@app.get("/uppercase/{text}")
def to_upper(text: str):
    return { "original": text, "uppercased": text.upper()}


@app.post("/remove-vowels")
def remove_vowels(text: str):
    letters = ["a", "e", "i", "o", "u"]
    new_text = ""
    for ch in text:
        if ch not in letters:
            new_text = new_text+ ch
    return { "original": text, "without_vowels": new_text }
