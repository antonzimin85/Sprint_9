from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    TIMEOUT = 20

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located(locator)
        )

    def click_on_element(self, locator, timeout=TIMEOUT):
        self.find_element(locator, timeout).click()

    def enter_text(self, locator, text, timeout=TIMEOUT):
        self.find_element(locator, timeout).send_keys(text)

    def return_element_text(self, locator, timeout=TIMEOUT):
        return self.find_element(locator, timeout).text

    def return_current_url(self):
        return self.driver.current_url

    def load_file(self, locator, file_path, timeout=TIMEOUT):
        self.find_element(locator, timeout).send_keys(file_path)

    def wait_element_is_visible(self, element_locator, timeout=TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(element_locator)
        ).is_displayed()

    def check_element_is_visible(self, element_locator, timeout=TIMEOUT):
        return (
            WebDriverWait(self.driver, timeout)
            .until(expected_conditions.visibility_of_element_located(element_locator))
            .is_displayed()
        )
