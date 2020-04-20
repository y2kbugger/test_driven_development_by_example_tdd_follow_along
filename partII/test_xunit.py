from xunit import test_method

test = WasRun("test_method")
print(test.was_run)
test.test_method()
print(test.was_run)
