
from flask import Flask, render_template, request, jsonify
import ast
import operator

app = Flask(__name__)

# Allowed mathematical operations
operations = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos
}


def calculate(expression):
    def evaluate(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in operations:
            left = evaluate(node.left)
            right = evaluate(node.right)

            if isinstance(node.op, ast.Pow) and abs(right) > 100:
                raise ValueError("Exponent is too large")

            result = operations[type(node.op)](left, right)

            if abs(result) > 1e100:
                raise ValueError("Result is too large")

            return result

        if isinstance(node, ast.UnaryOp) and type(node.op) in operations:
            return operations[type(node.op)](evaluate(node.operand))

        raise ValueError("Invalid expression")

    tree = ast.parse(expression, mode="eval")
    return evaluate(tree.body)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate_result():
    try:
        data = request.get_json()
        expression = data.get("expression", "")

        if not isinstance(expression, str) or not expression.strip():
            return jsonify({"error": "Enter an expression"}), 400

        if len(expression) > 100:
            return jsonify({"error": "Expression is too long"}), 400

        result = calculate(expression)

        return jsonify({"result": result})

    except ZeroDivisionError:
        return jsonify({"error": "Cannot divide by zero"}), 400

    except (ValueError, SyntaxError, TypeError, OverflowError):
        return jsonify({"error": "Invalid calculation"}), 400


if __name__ == "__main__":
    app.run(debug=True)
