
---

# 🧪 AutomationExercise Testing Framework

## 📘 Project Description

This project is a web UI test automation suite built using **Pytest**,  **Playwright**, and **Allure** for [https://automationexercise.com/](https://automationexercise.com/).
It verifies key functionalities like registration, login, product search, contact form submission, and more using modular test design, fixtures, and rich reporting.

---

## ✅ Requirements

* Python 3.13
* [Pipenv](https://pipenv.pypa.io/en/latest/) for dependency management

---

## 🛠️ Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Maximka47/PyTest_Task
   cd PyTest_Task
   ```

2. **Install Dependencies**

   ```bash
   pipenv install
   ```

3. **Install Playwright Browsers**

   ```bash
   pipenv run playwright install
   ```

---

## 🚀 How to Run Tests

To execute all tests with the default browser (Chromium):

```bash
pipenv run pytest
```

To run tests in a specific browser (Chromium, Firefox, or WebKit):

```bash
pipenv run pytest --use-browser=firefox
```

To run tests in parallel using multiple CPUs:

```bash
pipenv run pytest -n auto
```

> 💡 Test results and screenshots are automatically captured via Allure and saved under `./reports/allure-results`.

---

## 📊 How to Generate Test Report

After running the tests:

1. **Generate Allure HTML Report**

   ```bash
   allure generate ./reports/allure-results --clean -o ./reports/allure-report
   ```

2. **Open the Report in Your Browser**

   ```bash
   allure open ./reports/allure-report
   ```

---
