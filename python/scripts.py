import os
import subprocess
import sys

sys.path.append(os.path.dirname(__file__))


def test():
    """
    Run all tests with pytest, output results to an XML and HTML files.
    """
    subprocess.run(
        [
            "python",
            "-m",
            "pytest",
            "--junitxml=tests/results/test-results.xml",
        ]
    )


def __main__():
    """
    Run the test function.
    """
    test()
