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
        return TestResult()
    def teardown(self):
        pass

class TestResult:
    def summary(self):
        return "1 run, 0 failed"

class WasRun(TestCase):
    def setup(self):
        self.log = ['setup']
    def test_method(self):
        self.log.append('running')
    def teardown(self):
        self.log.append('teardown')

