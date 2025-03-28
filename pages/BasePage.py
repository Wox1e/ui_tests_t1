"""Модуль предоставляющий базовый класс для страниц"""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для страниц, предоставляющий общие методы для взаимодействия с элементами."""

    def __init__(self, driver):
        """Инициализация базовой страницы."""

        self.driver = driver
        self.base_url = ""

    def find_element(self, locator: tuple, time: int = 10) -> WebElement:
        """Выполняет поиск элемента по локатору"""
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Не получается найти элемент: {locator}",
        )

    def fill_element(self, element: WebElement, text: str) -> None:
        """Заполняет элемент текстом"""

        element.send_keys(text)

    def click_on_element(self, element: WebElement) -> None:
        """Нажимает на элемент."""
        element.click()

    def is_alert_appeared(self, timeout_sec: int) -> bool:
        """Проверяет, появился ли алерт.

        Args:
            timeout_sec: Время ожидания в секундах.

        Returns:
            bool: True, если алерт появился, иначе False.
        """
        try:
            WebDriverWait(self.driver, timeout_sec).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            print("alert accepted")
            return True
        except TimeoutException:
            print("no alert")
            return False
