import traceback

class TestCase:
    def __init__(self, name):
        self.name = name
    def setup(self):
        pass
    def run(self):
        testresult = TestResult()
        testresult.test_starting()
        try:
            self.setup()
        except Exception as e:
            testresult.test_failed(e)
            return testresult
        try:
            method = self.__getattribute__(self.name)
            method()
        except Exception as e:
            testresult.test_failed(e)

        self.teardown()
        return testresult
    def teardown(self):
        pass

class TestResult:
    def __init__(self):
        self.run_count = 0
        self.failed_count = 0
        self._exceptions = []
    def test_starting(self):
        self.run_count += 1
    def test_failed(self, exception):
        s = traceback.format_exc()
        self._exceptions.append(s)
        self.failed_count += 1
    def summary(self):
        return f"{self.run_count} run, {self.failed_count} failed"
    def exceptions(self):
        return self._exceptions

class TestSuite():
    def add(self, testcase):
        pass
