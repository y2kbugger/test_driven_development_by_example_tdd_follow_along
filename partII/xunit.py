class TestCase:
    def __init__(self, name):
        self.name = name
    def setup(self):
        self.was_setup  = True
    def run(self):
        self.setup()
        method = self.__getattribute__(self.name)
        method()

class WasRun(TestCase):
    def __init__(self, name):
        self.was_run = None
        super().__init__(name)
    def test_method(self):
        self.was_run = True
