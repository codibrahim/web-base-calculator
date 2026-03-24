from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    """Render the calculator page."""
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    """Handle calculation requests from the frontend."""
    data = request.get_json()
    expression = data.get("expression", "")

    try:
        # Safely evaluate the mathematical expression
        allowed_chars = set("0123456789+-*/(). ")
        if not all(c in allowed_chars for c in expression):
            return jsonify({"result": "Error: Invalid characters"})

        result = eval(expression)

        # Handle division by zero and format result
        if isinstance(result, float) and result != result:
            return jsonify({"result": "Error: Invalid operation"})

        # Return integer if result has no decimal part
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        return jsonify({"result": str(result)})

    except ZeroDivisionError:
        return jsonify({"result": "Error: Division by zero"})
    except Exception:
        return jsonify({"result": "Error: Invalid expression"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
