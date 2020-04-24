from xunit import TestCase, TestCase, TestResult

class WasRun(TestCase):
    def setup(self):
        self.log = ['setup']
    def test_method(self):
        self.log.append('running')
    def test_failed_method(self):
        raise RuntimeError("Fake Error")
    def teardown(self):
        self.log.append('teardown')

class WasRunBadSetup(WasRun):
    def setup(self):
        super().__init__()
        raise RuntimeError("Fake SetUpError")

class TestCaseTest(TestCase):
    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert test.log[0] == 'setup'
        assert test.log[1] == 'running'
        assert test.log[2] == 'teardown'
    def test_result(self):
        test = WasRun("test_method")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()
    def test_failed_result_formatting(self):
        result = TestResult()
        result.test_starting()
        result.test_failed()
        assert "1 run, 1 failed" == result.summary()
    def test_result_failed(self):
        test = WasRun("test_failed_method")
        result = test.run()
        assert "1 run, 1 failed" == result.summary()
    def test_result_failed_during_setup(self):
        test = WasRunBadSetup("Doesnt_matter")
        result = test.run()
        assert "1 run, 1 failed" == result.summary()

tests = [
    'test_template_method',
    'test_result',
    'test_failed_result_formatting',
    'test_result_failed',
    'test_result_failed_during_setup',
    ]

for t in tests:
    r = TestCaseTest(t).run()
    print(r.summary())
