from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html><body style="font-family:sans-serif; text-align:center; padding:40px;">
    <h1>FitBuddy 💪</h1>
    <form method="post" action="/generate">
        <input name="goal" placeholder="Goal: Weight Loss" required style="padding:10px; width:250px;"><br><br>
        <input name="level" placeholder="Level: Beginner" required style="padding:10px; width:250px;"><br><br>
        <button style="padding:10px 20px; background:green; color:white;">Generate Plan</button>
    </form></body></html>
    """

@app.post("/generate", response_class=HTMLResponse)
def generate(goal: str = Form(...), level: str = Form(...)):
    return f"<html><body style='padding:20px'><h2>Your Plan for {goal} - {level}</h2><p>Day1: Chest<br>Day2: Back<br>Day3: Legs<br>Day4: Rest</p><a href='/'>Back</a></body></html>"