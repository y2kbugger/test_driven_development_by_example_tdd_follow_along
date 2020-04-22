class TestCase:
    def __init__(self, name):
        self.name = name
    def setup(self):
        pass
    def run(self):
        self.setup()
        method = self.__getattribute__(self.name)
        method()

class WasRun(TestCase):
    def setup(self):
        self.log = ['setup']

    def test_method(self):
        self.log.append('running')
