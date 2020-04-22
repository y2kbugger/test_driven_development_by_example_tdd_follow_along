class TestCase:
    def __init__(self, name):
        self.name = name
    def setup(self):
        pass
    def run(self):
        testresult = TestResult()
        testresult.test_starting()
        self.setup()
        method = self.__getattribute__(self.name)

        try:
            method()
        except:
            testresult.test_failed()

        self.teardown()
        return testresult
    def teardown(self):
        pass

class TestResult:
    def __init__(self):
        self.run_count = 0
        self.failed_count = 0
    def test_starting(self):
        self.run_count += 1
    def test_failed(self):
        self.failed_count += 1
    def summary(self):
        return f"{self.run_count} run, 0 failed"

class WasRun(TestCase):
    def setup(self):
        self.log = ['setup']
    def test_method(self):
        self.log.append('running')
    def test_failed_method(self):
        raise RuntimeError("Fake Error")
    def teardown(self):
        self.log.append('teardown')

