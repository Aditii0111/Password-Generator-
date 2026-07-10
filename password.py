from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    password = ""
    strength = ""

    if request.method == "POST":

        length = int(request.form["length"])

        characters = ""

        if "uppercase" in request.form:
            characters += string.ascii_uppercase

        if "lowercase" in request.form:
            characters += string.ascii_lowercase

        if "numbers" in request.form:
            characters += string.digits

        if "symbols" in request.form:
            characters += string.punctuation

        if characters:

            password = "".join(
                random.choice(characters)
                for _ in range(length)
            )

            score = 0

            if length >= 8:
                score += 1

            if length >= 12:
                score += 1

            if any(c.isdigit() for c in password):
                score += 1

            if any(c in string.punctuation for c in password):
                score += 1

            if score <= 2:
                strength = "Weak"

            elif score == 3:
                strength = "Medium"

            else:
                strength = "Strong"

    return render_template(
        "index.html",
        password=password,
        strength=strength
    )

if __name__ == "__main__":
    app.run(debug=True)