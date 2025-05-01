from flask import Flask, render_template

app = Flask(__name__)

# Sample flashcards
flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
]

@app.route("/")
def index():
    return render_template("index.html", flashcards=flashcards)

if __name__ == "__main__":
    app.run(debug=True)