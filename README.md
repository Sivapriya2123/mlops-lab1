# MLOps Lab 1: Extended Calculator

This project is based on Lab 1 from the MLOps course repository.

## Project Overview

The original lab included four calculator functions:

- Addition
- Subtraction
- Multiplication
- Sum of three numbers

For my modified version, I kept the original calculator functions and extended the project by adding four new operations:

- Division
- Power
- Modulus
- Average

## Functions

The calculator now contains:

- `fun1(x, y)`: Addition
- `fun2(x, y)`: Subtraction
- `fun3(x, y)`: Multiplication
- `fun4(x, y, z)`: Sum of three numbers
- `fun5(x, y)`: Division
- `fun6(x, y)`: Power
- `fun7(x, y)`: Modulus
- `fun8(x, y)`: Average

## Testing

This project includes automated tests using:

- Pytest
- Python Unittest

### Run Pytest

```bash
pytest
```

### Run Unittest

```bash
python3 -m unittest test.test_unittest
```

## GitHub Actions

GitHub Actions are configured to automatically run both testing frameworks.

The workflows run when:

- Changes are pushed to the `main` branch
- A pull request targets the `main` branch

The workflow files are:

- `.github/workflows/pytest_action.yml`
- `.github/workflows/unittest_action.yml`

## Project Structure

```text
mlops-lab1/
├── .github/
│   └── workflows/
│       ├── pytest_action.yml
│       └── unittest_action.yml
├── data/
│   └── __init__.py
├── src/
│   ├── __init__.py
│   └── calculator.py
├── test/
│   ├── __init__.py
│   ├── test_pytest.py
│   └── test_unittest.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Modification from Original Lab

The original lab contained four basic calculator functions.

For this modified version, I kept the original functionality and added four additional calculator operations:

- Division
- Power
- Modulus
- Average

I also added corresponding Pytest and Unittest test cases for the new functions.

## Test Results

Both testing workflows successfully pass using GitHub Actions:

- Pytest: Passed
- Unittest: Passed