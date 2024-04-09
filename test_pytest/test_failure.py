'''error path tests for 6 degress of kb'''
import sys
import pytest
sys.path.insert(0, "..")
import degrees_of_kb \
        # pylint: disable=import-error,wrong-import-position # noqa: E402


def test_invalid_url():
    '''test a valid url and that urls is populated'''
    k_b = degrees_of_kb.KevinBacon6Degrees("/nonesense!/Kevin_Bacon")
    with pytest.raises(ValueError):
        k_b.generate_6_degrees()


def test_empty_url():
    '''test empty url'''
    with pytest.raises(ValueError):
        k_b = degrees_of_kb.KevinBacon6Degrees("")\
            # pylint: disable=unused-variable # noqa: F841


def test_no_url():
    ''' test no url'''
    with pytest.raises(ValueError):
        k_b = degrees_of_kb.KevinBacon6Degrees(None)\
            # pylint: disable=unused-variable # noqa: F841
