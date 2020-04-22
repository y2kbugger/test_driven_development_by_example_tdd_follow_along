from xunit import WasRun, TestCase

class TestCaseTest(TestCase):
    def test_template_method(self):
        self.test = WasRun("test_method")
        self.test.run()
        assert self.test.log[0] == 'setup'
        assert self.test.log[1] == 'running'
        assert self.test.log[2] == 'teardown'

TestCaseTest('test_template_method').run()
