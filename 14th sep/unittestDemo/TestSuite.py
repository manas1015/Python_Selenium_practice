import unittest
from TC01 import TestCase01
from TC02 import TestCase02
booleanTC01 = True
booleanTC02 = True

suite_TC01 = unittest.TestLoader().loadTestsFromTestCase(TestCase01)
suite_TC02 = unittest.TestLoader().loadTestsFromTestCase(TestCase02)

mainSuite= ""
if booleanTC01 and booleanTC02 :
    mainSuite = unittest.TestSuite([suite_TC01, suite_TC02])
else:
    mainSuite = unittest.TestSuite([suite_TC01])

unittest.TextTestRunner(verbosity=2).run(mainSuite)