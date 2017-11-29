from nose.tools import assert_equal, assert_not_equal

from requirements.requirement import Requirement


def get_reqs(requirement_1, requirement_2):
    return (Requirement.parse(requirement_1),
            Requirement.parse(requirement_2))


def test_simple_equality():
    assert_equal(*get_reqs("pylib==1.0.0", "pylib==1.0.0"))


def test_equality_no_specifiers():
    assert_equal(*get_reqs("pylib", "pylib"))


def test_simple_inequality():
    assert_not_equal(*get_reqs("pylib==1.0.0", "pylib==1.0.1"))


def test_spec_order_equality():
    """
    The same specifications, in a different order, are still equal
    """
    assert_equal(*get_reqs("pylib>=1.0,<2.0", "pylib<2.0,>=1.0"))


def test_vcs_equality():
    assert_equal(*get_reqs(
        "-e git://git.example.com/MyProject.git@da39a3ee#egg=MyProject",
        "-e git://git.example.com/MyProject.git@da39a3ee#egg=MyProject"))


def test_vcs_hash_inequality():
    assert_not_equal(*get_reqs(
        "-e git://git.example.com/MyProject.git@123#egg=MyProject",
        "-e git://git.example.com/MyProject.git@abc#egg=MyProject"))
