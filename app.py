from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'NotMath' 

def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op = random.choice(["+", "-", "*"])
    
    if op == "+":
        answer = num1 + num2
    elif op == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2

    return f"{num1} {op} {num2}", answer

@app.route("/", methods=["GET"])
def landing():
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def quizPage():
    if "score" not in session:
        session["score"] = 0
        session["question"], session["answer"] = generate_question()

    feedback = ""
    
    if request.method == "POST":
        try:
            user_answer = int(request.form["answer"])
            if user_answer == session["answer"]:
                session["score"] += 1
                feedback = "✅ Correct!"
            else:
                feedback = f"❌ Incorrect. The correct answer was {session['answer']}"
        except ValueError:
            feedback = "⚠️ Please enter a valid number."

        session["question"], session["answer"] = generate_question()

    return render_template("quizPage.html", question=session["question"], score=session["score"], feedback=feedback)

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("quizPage"))

if __name__ == "__main__":
    app.run(debug=True)
