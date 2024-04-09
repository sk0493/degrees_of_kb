'''happy path tests for 6 degress of kb'''
import sys
sys.path.insert(0, "..")
import degrees_of_kb \
        # pylint: disable=import-error,wrong-import-position # noqa: E402


def test_valid_url():
    '''test a valid url and that urls is populated'''
    k_b = degrees_of_kb.KevinBacon6Degrees("/wiki/Kevin_Bacon")
    k_b.generate_6_degrees()
    assert len(k_b.urls) == 6
