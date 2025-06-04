# Project Overview

This project utilizes `pytest` and `Playwright` to test a web application. It includes a GitHub Actions workflow for continuous integration, automatically running tests on pushes to the `main` branch.

```
├── .github/
│   └── workflows/
│       └── playwright.yml  # GitHub Actions workflow
├── pages/
│   └── map_page.py                   # Page Object Model for the map
├── reports/
│   └── report.html                   # Generated test report
├── tests/
│   ├── __init__.py
│   ├── conftest.py                   # Pytest fixtures for setup/teardown
│   └── test_popup.py                 # Popup test suite
├── utils/
│   ├── __init__.py
│   └── custom_logger.py              # Custom logging utility
├── .env                              # Environment variables (local, ignored by Git)
├── .env.sample                       # Sample .env file
├── .gitignore                        # Git ignore file
├── pytest.ini                        # Pytest configuration
├── README.md                         # Project README file
└── requirements.txt                  # Python dependencies
```
## Setup

### Prerequisites

* Python 3.11
* `pip` (Python package installer)

### Local Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-folder>
    ```
    *Replace `<your-repository-url>` with the actual URL of your Git repository.*
    *Replace `<your-repository-folder>` with the name of the cloned directory.*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```


4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Install Playwright browsers:**
    ```bash
    playwright install
    ```

6.  **Environment Variables:**
    Create a `.env` file in the root directory of your project and add the `OPENLAYERS_URL` variable, pointing to the URL of the application you want to test.

    Example `.env` file:
    ```
    OPENLAYERS_URL=http://localhost:8080/
    ```

    *Note: The `.env` file is excluded from version control via `.gitignore`.*

## Running Tests

### Locally

To run all tests:

```bash
pytest