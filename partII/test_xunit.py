from xunit import WasRun, TestCase

class TestCaseTest(TestCase):
    def test_template_method(self):
        self.test = WasRun("test_method")
        self.test.run()
        assert self.test.log[0] == 'setup'
        assert self.test.log[1] == 'running'
        assert self.test.log[2] == 'teardown'
    def test_result(self):
        self.test = WasRun("test_method")
        result = self.test.run()
        assert "1 run, 0 failed" == result.summary()
    def test_result_failed(self):
        self.test = WasRun("test_failed_method")
        result = self.test.run()
        assert "1 run, 1 failed" == result.summary()


TestCaseTest('test_template_method').run()
TestCaseTest('test_result').run()
TestCaseTest('test_result_failed').run()
