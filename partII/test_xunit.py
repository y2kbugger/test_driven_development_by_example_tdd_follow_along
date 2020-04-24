from xunit import TestCase, TestCase, TestResult, TestSuite

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
    def setup(self):
        self.result = TestResult()
    def test_template_method(self):
        test = WasRun('test_method')
        test.run(self.result)
        assert test.log[0] == 'setup'
        assert test.log[1] == 'running'
        assert test.log[2] == 'teardown'
    def test_result(self):
        test = WasRun('test_method')
        test.run(self.result)
        assert '1 run, 0 failed' == self.result.summary()
    def test_failed_result_formatting(self):
        self.result.test_starting()
        self.result.test_failed("fake exception and trackback")
        assert '1 run, 1 failed' == self.result.summary()
    def test_result_failed(self):
        test = WasRun('test_failed_method')
        test.run(self.result)
        assert "1 run, 1 failed" == self.result.summary()
    def test_result_failed_during_setup(self):
        test = WasRunBadSetup('Doesnt_matter')
        test.run(self.result)
        assert "1 run, 1 failed" == self.result.summary()
    def test_summary_includes_exceptions(self):
        test = WasRun('test_failed_method')
        test.run(self.result)
        assert any("Fake Error" in e for e in self.result.exceptions())
    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun('test_method'))
        suite.add(WasRun('test_failed_method'))
        suite.run(self.result)
        assert "2 run, 1 failed" == self.result.summary()

tests = [
    'test_template_method',
    'test_result',
    'test_failed_result_formatting',
    'test_result_failed',
    'test_result_failed_during_setup',
    'test_summary_includes_exceptions',
    'test_suite',
    ]

ts = TestSuite()
r = TestResult()
for t in tests:
    ts.add(TestCaseTest(t))
ts.run(r)
print(r.summary())
for e in r.exceptions():
    print(e)
    print()
