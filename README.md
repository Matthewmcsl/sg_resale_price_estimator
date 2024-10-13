# Singapore Resale HDB Price Predictor
Practice on an end-to-end deployment of a Regression-based predictive model.

## Setup Instructions

1. **Activate bash script to setup project structure**
   - Navigate to the project folder - ```/sg_resale_price_estimator/```
   - Run the following command to setup our predefined project structure.
     ```bash
     ../project_setup.sh
     ```

2. **Install Poetry, skip if already exists.**
   - Install Poetry using the following command:
     ```bash
     curl -sSL https://install.python-poetry.org | python3 -
     ```

3. **Initialize Poetry**
   - Run the following command to create the `pyproject.toml` file:
     ```bash
     poetry init
     ```
   - Follow the prompts to define your project and dependencies.

4. **Create virtual environment and install dependencies using Poetry**
   - Run the following command to install the dependencies specified in `pyproject.toml` and create a virtual environment:
     ```bash
     poetry install
     ```

5. **Activate the virtual environment**
   - Spawn a shell within the Poetry-managed virtual environment with, this is similar to ```source venv/bin/activate```:
     ```bash
     poetry shell
     ```

6. **Run your application or scripts**
   - Now you can start developing your scripts or run your application.




