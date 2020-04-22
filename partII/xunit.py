class TestCase:
    def __init__(self, name):
        self.name = name
    def setup(self):
        pass
    def run(self):
        self.setup()
        method = self.__getattribute__(self.name)
        method()
        self.teardown()
    def teardown(self):
        pass

class WasRun(TestCase):
    def setup(self):
        self.log = ['setup']
    def test_method(self):
        self.log.append('running')
    def teardown(self):
        self.log.append('teardown')

