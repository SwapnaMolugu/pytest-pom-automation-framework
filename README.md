# Pytest-POM Automation Framework

## License
Python Pytest License

## Overview
A comprehensive, scalable test automation framework built with **Pytest** for Web (Selenium) testing, designed specifically for validating the E2E e-commerce platform. The framework follows industry-standard design patterns to ensure maintainability, reusability, and ease of integration into CI/CD pipelines.

## 🎯 Features
- **Page Object Model (POM):** Structured web test automation for login, cart, checkout, and product flows
- **Multiple Environments:** Configurable for Dev, QA, Staging, and Production
- **Parallel Execution:** Run tests in parallel with `pytest-xdist` for faster feedback
- **Rich Reporting:** HTML, Allure, and JSON reports for detailed insights
- **Data-Driven Testing:** YAML/JSON test data support for flexible scenarios
- **Retry Mechanism:** Auto-retry failed tests to reduce flakiness
- **CI/CD Ready:** Seamless integration with GitHub Actions and Jenkins
- **Logging:** Comprehensive logging with colored output for better debugging
- **Screenshot on Failure:** Automatic screenshot capture for failed test cases
- **Cross-Browser Support:** Chrome, Firefox, Edge, and Safari


## Project Structure

```
project_root/
│
├── pages/                          # Page Object Models (Web)
│   │   __init__.py 
│   │   login_page.py               # Login page
│   │   cart_page.py                # Cart page
│   │   logout.py                   # Logout page
│   │   product_page.py
│
├── screenshot/
│   │   test_check_out_failure.png
│
├── tests/                          # Test files
│   │   test_checkout.py
│   │   test_login.py
│   │   test_logout.py
│   │   __init__.py
│   │
│   ├── outputs/        
│   │   mylog.log                   #logs
│   │   report.html                 #Test resports
│
├── utils/                          # Utility modules
│   │   test_helpers.py             # Helper functions
│   │
│   ├── config/                     # Environment configurations
│   │   credentials.yaml            #login credentials
│   │
│   ├── data_reader/
│   │   │   __init__.py
│   │   │   config_loader.py        # Test data readers
│
├── conftest.py        # Pytest fixtures and hooks
├── mylog.log          # added at project root
├── pytest.ini         # Pytest configuration file
├── README.md          # project documentation
├── requirements.txt   # dependencies
```

## Getting Started
### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git
- Chrome/Firefox browser

### Installation
- Clone the repository
- Create virtual environment
- Install dependencies
- Set up environment 

### Framework Design 
-  POM, Tests, Utils, conftest.py, helper_functions.py, pytest.ini
### Running Tests
- pytest -v
- pytest -n 4
- pytest --browser firefox

### Configuration
- credentials.yaml → login credentials
- pytest.ini → global pytest settings

### Reporting
#### HTML Report
pytest --html=reports/report.html --self-contained-htmlHTML report → tests/outputs/report.html
#### JSON Report
pytest --json-report --json-report-file=reports/report.json
#### Allure Report
pytest --alluredir=reports/allure-results
allure serve reports/allure-results

### CI/CD Integration
- GitHub Actions workflow example
- Jenkins pipeline snippet

## Troubleshooting
### Common Issues
#### Issue: WebDriver not found

##### Solution: Install webdriver-manager
- pip install webdriver-manager
- Issue: Tests failing in headless mode

##### Solution: Increase window size
- BROWSER_WIDTH=1920 BROWSER_HEIGHT=1080 

Issue: Element not found
- Check if element is in iframe
-  locator strategy
- Add explicit waits
- Check for dynamic content

## Test Reporting
- Available Report Types
- HTML Report: pytest-html 
- Allure Report: Rich interactive reports 
- JSON Report: Machine-readable results
- JUnit XML: CI/CD integration 
- Custom Reports: Extend reporting as needed