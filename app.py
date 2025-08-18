from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with a form
HTML_TEMPLATE = """
<!doctype html>
<html>
    <head>
        <title>Sum Two Numbers</title>
    </head>
<body>
    <h1>Enter Two Numbers</h1>
<form method="POST" action="/">
    <label for="num1">Number 1:</label>
    <input type="number" id="num1" name="num1" required>
    <br><br>
    <label for="num2">Number 2:</label>
    <input type="number" id="num2" name="num2" required>
    <br><br>
    <button type="submit">Calculate Sum</button>
</form>
    {% if result is not none %}
        <h2>Result: {{ result }}</h2>
    {% endif %}
    </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculate():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            result = num1 + num2
        except ValueError:
            result = "Invalid input. Please enter valid numbers."
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(debug=True)

