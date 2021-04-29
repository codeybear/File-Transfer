import unittest
import sync

class TestSync(unittest.TestCase):
    def setUp(self):
        # Specify test data folder
        self.test_folder = "test_Files"

    def test_file_count(self):
        runner = sync.DirScanner(self.test_folder, 100)
        files = runner.scan()
        self.assertEqual(len(files), 7)


