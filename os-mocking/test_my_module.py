import os.path
import unittest

try:
    from unittest import mock
except ImportError:
    import mock  # pip install mock

from my_module import my_remove


class NoMockingTestCase(unittest.TestCase):
    def test_provided_extension_should_be_used(self):
        filename = 'file.md'
        open(filename, 'w').close()
        self.assertTrue(os.path.isfile(filename))
        my_remove(filename)
        self.assertFalse(os.path.isfile(filename))

    def test_when_extension_is_missing_then_use_default_one(self):
        filename = 'file.txt'
        open(filename, 'w').close()
        self.assertTrue(os.path.isfile(filename))
        my_remove('file')
        self.assertFalse(os.path.isfile(filename))

    def test_when_file_is_missing_then_silence_the_exception(self):
        filename = 'file.md'
        self.assertFalse(os.path.isfile(filename))
        my_remove('file.md')


class PatchingTestCase(unittest.TestCase):
    @mock.patch('my_module.os')
    def test_provided_extension_should_be_used(self, os_mock):
        my_remove('file.md')
        os_mock.remove.assert_called_once_with('file.md')

    @mock.patch('my_module.os')
    def test_when_extension_is_missing_then_use_default_one(self, os_mock):
        my_remove('file')
        os_mock.remove.assert_called_once_with('file.txt')

    @mock.patch('my_module.os')
    def test_when_file_is_missing_then_silence_the_exception(self, os_mock):
        os_mock.remove.side_effect = OSError
        my_remove('file.md')
        os_mock.remove.assert_called_once_with('file.md')


if __name__ == "__main__":
    unittest.main()
