from typing import Union
from selenium.webdriver.chrome.webdriver import WebDriver


class Browser:

    driver: Union[None, WebDriver] = None
    logger = None

    def __new__(cls):

        # logger object is created
        if not cls.logger:
            pass

        # driver object is created
        if not cls.driver:
            pass

        return super().__new__(cls)
