from ward import fixture, test


class User(object):
    def __init__(self, name):
        self.name = name


@test("the list contains 42")
def _():
    assert 42 in [-21, 42, 999]


@fixture
def user():
    return User(name="darren")


@test("the user is called darren")
def _(u=user):
    assert u.name == "darren"
