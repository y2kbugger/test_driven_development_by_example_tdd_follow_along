class TestCase:
    def __init__(self, name):
        self.name = name
        self.setup()
    def setup(self):
        self.was_setup  = True
    def run(self):
        method = self.__getattribute__(self.name)
        method()

class WasRun(TestCase):
    def setup(self):
        self.was_run = False
        self.was_setup = True
    def test_method(self):
        self.was_run = True
