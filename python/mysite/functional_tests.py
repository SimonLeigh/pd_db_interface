from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_retrieve_root_page(self):

        # We wish to check out the homepage
        self.browser.get('http://localhost:8000')

        # Check that the title is page not found for root
        self.assertEqual('Page not found at /', self.browser.title)


if __name__ == '__main__':
    unittest.main()
