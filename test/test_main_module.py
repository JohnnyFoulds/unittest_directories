import os
import sys

root_path = os.path.dirname(os.path.dirname(__file__))
src_path = os.path.join(root_path, 'src')
sys.path.append(src_path)
#print(src_path)

#sys.path.insert(0, '/workspaces/unittest_directories/src')

import unittest
import app

class TestMainModule(unittest.TestCase):
    def test_main_hello(self):
        self.assertEqual(app.main_hello(), "hello main")