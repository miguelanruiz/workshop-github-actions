import os
import subprocess
import sys

sys.path.append(os.path.dirname(__file__))


def test():
    """
    Run all tests with pytest, output results to xml file. Equivalent command:
    `poetry install`
    `poetry run python -m pytest --junitxml=test_results.xml`
    """
    subprocess.run(["poetry", "lock"])
    subprocess.run(["poetry", "install"])
    subprocess.run(["python", "-m", "pytest", "--junitxml=tests/results/test-results.xml"])
