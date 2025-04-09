# UniRazak-MVPAssignment
Manage Virtual Project

## Automation Workflow

This project uses GitHub Actions to automate various tasks on push to the `main` branch. The workflow is defined in `.github/automation_workflow.yml` and `.github/workflows`.

### Steps in the Workflow

1. **Checkout Repository**: Checks out the repository to the GitHub runner.
2. **Set up Python**: Sets up the Python environment.
3. **Install Dependencies**: Installs the required dependencies.
4. **Run Workflow Script**: Executes the `workflow.py` script.
5. **Run Linting**: Runs linting using `flake8`.
6. **Run Tests**: Runs tests using `pytest`.
7. **Build Project**: Builds the project using `python setup.py build`.

### Running Linting, Tests, and Build Locally

To run linting, tests, and build locally, follow these steps:

1. **Install Dependencies**:
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

2. **Run Linting**:
   ```bash
   flake8 .
   ```

3. **Run Tests**:
   ```bash
   pytest
   ```

4. **Build Project**:
   ```bash
   python setup.py build
   ```
