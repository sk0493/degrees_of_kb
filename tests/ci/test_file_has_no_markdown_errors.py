""" dynamic pytest wrapper"""

import glob
import subprocess
import pytest

FILTER = './../../**/*.md'
PYTHON_FILES = glob.glob(FILTER, recursive=True)


@pytest.mark.parametrize('filepath', PYTHON_FILES)
def test_file_has_no_markdown_errors(filepath):
    """validate that there are zero markdown warnings against any markdown file""" # noqa: 501 pylint: disable=line-too-long
    print(F"creating tests for file {filepath}")

    with subprocess.Popen("pymarkdown -d line-length,no-missing-space-atx,blanks-around-lists,first-line-heading,no-emphasis-as-heading,no-inline-html,code-block-style scan " + filepath, # noqa: 501 pylint: disable=line-too-long
                          stdout=subprocess.PIPE, shell=True) as proc:

        (out, _err) = proc.communicate()

    if out and out.strip():
        print(out)

    # pylint: disable=C1801
    assert len(out) == 0
