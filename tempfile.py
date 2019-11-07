import tempfile

with tempfile.TemporaryDirectory() as dir:
    print(dir)
    print(type(dir))
    print('Exiting')