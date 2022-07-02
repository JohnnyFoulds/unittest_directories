import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

import unittest
import app

class TestMainModule(unittest.TestCase):
    def test_main_hello(self):
        self.assertEqual(app.main_hello(), "hello main")