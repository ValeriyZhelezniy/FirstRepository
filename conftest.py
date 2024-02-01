import pytest
#sys.stdout.reconfigure(encoding='utf-8')


class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create_name(self):
        self.name = 'Valeriy'
        self.second_name = 'Zhelezniy'
    def remove_name(self):
        self.name = ''
        self.second_name = ''

@pytest.fixture
def user():
    user = User()
    user.create()
    
    yield User

    user.remove()