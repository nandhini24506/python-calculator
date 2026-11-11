
const expressionDisplay = document.getElementById("expression");
const resultDisplay = document.getElementById("result");

let expression = "";

function updateDisplay() {
    expressionDisplay.textContent = expression || "0";
}

function appendValue(value) {
    expression += value;
    updateDisplay();
    resultDisplay.textContent = "";
}

function clearDisplay() {
    expression = "";
    updateDisplay();
    resultDisplay.textContent = "";
}

function deleteLast() {
    expression = expression.slice(0, -1);
    updateDisplay();
    resultDisplay.textContent = "";
}

async function calculateResult() {
    if (!expression.trim()) {
        resultDisplay.textContent = "Enter a value";
        return;
    }

    try {
        const response = await fetch("/calculate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                expression: expression
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error);
        }

        resultDisplay.textContent = data.result;

    } catch (error) {
        resultDisplay.textContent = error.message || "Error";
    }
}

// Keyboard support
document.addEventListener("keydown", function(event) {
    const key = event.key;

    if ("0123456789+-*/%.()".includes(key) && key.length === 1) {
        appendValue(key);
    } else if (key === "Enter") {
        calculateResult();
    } else if (key === "Backspace") {
        deleteLast();
    } else if (key === "Escape") {
        clearDisplay();
    }
});
