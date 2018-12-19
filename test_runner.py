import unittest
import sys
from tools.driverhelper import DriverHelper


def run_tests():
    # runs tests on all modules in tests folder
    suite = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'all':
            # loops through and tests on all supported browsers in DriverHelper
            for browser in DriverHelper.drivers.keys():
                DriverHelper.current_browser = browser
                run_tests()
        else:
            # runs tests on argument specified browser
            DriverHelper.current_browser = sys.argv[1]
            run_tests()
    else:
        # uses default browser for tests (currently defined as firefox in DriverHelper)
        run_tests()
