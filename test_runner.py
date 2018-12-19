import unittest.suite
import sys
from tests import testhomepage
import HtmlTestRunner


if __name__ == '__main__':

    if len(sys.argv) > 1:
        if sys.argv[1] == 'chrome':
            # runs on chrome
            suite = unittest.TestLoader().loadTestsFromTestCase(testhomepage.TestHomePageChrome)
        elif sys.argv[1] == 'firefox':
            # runs on firefox
            suite = unittest.TestLoader().loadTestsFromTestCase(testhomepage.TestHomePageFirefox)
        else:
            print(sys.argv[1], "is not a supported driver")
            sys.exit()
    else:
        # runs on all drivers
        suite = unittest.TestLoader().loadTestsFromModule(testhomepage)

    # using JamesMTSloan branch of HTMLTestRunner to combine reports and show traceback
    HtmlTestRunner.HTMLTestRunner(combine_reports="True").run(suite)
