from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Browser:

    def __init__(self):
        self.browser = None

    def open_firefox(self, url):
        self.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.browser.get(url)

    def open_chrome(self, url):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get(url)

    def close_browser(self):
        if self.browser is not None:
            self.browser.quit()
