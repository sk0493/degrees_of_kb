""" dynamic pytest wrapper"""

import glob
import subprocess
import pytest

FILTER = './../../**/*.md'
PYTHON_FILES = glob.glob(FILTER, recursive=True)


@pytest.mark.parametrize('filepath', PYTHON_FILES)
def test_file_has_no_spelling_errors(filepath):
    """validate that there are no spelling mistakes in any markdown file""" # noqa: 501 pylint: disable=line-too-long
    print(F"creating tests for file {filepath}")

    with subprocess.Popen("codespell " + filepath + "-I ../../.codespellignore", # noqa: 501 pylint: disable=line-too-long
                          stdout=subprocess.PIPE, shell=True) as proc:
        (out, _err) = proc.communicate()

    if out and out.strip():
        print(out)

    # pylint: disable=C1801
    assert len(out) == 0
