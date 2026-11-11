# Python Calculator — CI/CD Practical

A small command-line calculator used to demonstrate **Continuous Integration (CI)** with GitHub Actions.

## Project structure

```text
python-calculator-cicd/
├── .github/
│   └── workflows/
│       └── python-ci.yml
├── tests/
│   └── test_calculator.py
├── calculator.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 1. Run the calculator locally

Use Python 3.11 or later.

```bash
python main.py
```

Choose an operation (1–4), enter two numbers, and view the result. Enter `q` to quit.

## 2. Install the test dependency

```bash
python -m pip install -r requirements.txt
```

## 3. Run tests locally

```bash
python -m pytest -v
```

The test suite checks addition, subtraction, multiplication, division, decimal results,
negative numbers, and division by zero.

## 4. Push the project to GitHub

Create an empty GitHub repository, then run these commands from this project folder
(replace the URL with your own repository URL):

```bash
git init
git add .
git commit -m "Add Python calculator and CI workflow"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

## 5. Observe GitHub Actions

1. Open your repository on GitHub.
2. Select the **Actions** tab.
3. Open **Python Calculator CI**.
4. Inspect each step and its logs.

The workflow is stored at `.github/workflows/python-ci.yml`. GitHub Actions detects this
file and runs the job when code is pushed to `main` or when a pull request targets `main`.

The workflow checks out the code, sets up Python 3.11, installs the requirements,
and runs the pytest suite. A green check means the workflow completed successfully;
a red cross means at least one step failed.

## Teaching note

This practical demonstrates **Continuous Integration**: every qualifying push or pull
request triggers automated checks. It does not automatically deploy the application,
so this example is CI rather than a complete production CD pipeline.
