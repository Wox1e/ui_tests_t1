"""Тесты для страницы AddCustomer"""

import allure
import pytest

from pages.AddCustomerPage import AddCustomerPage



@allure.feature("Тесты страницы Add Customer (корректные)")
class TestAddCustomerPage_correct:
    """Класс корректных тестов для страницы Add Customer"""

    @pytest.fixture(autouse=True)
    def setup(self, driver_setup):
        """Инициализация драйвера из фикстуры"""
        self.driver = driver_setup
        self.add_customer_page = AddCustomerPage(self.driver)

    @allure.story("Тестирование добавления нового клиента")
    def test_add_customer(self):
        """Тест на добавление одного корректного клиента"""
        with allure.step("Заполнение поля First Name"):
            self.add_customer_page.fill_fname_by_post_code()

        with allure.step("Заполнение поля Last Name"):
            self.add_customer_page.fill_lname_by_post_code()

        with allure.step("Заполнение поля Post Code"):
            self.add_customer_page.fill_post_code()

        with allure.step("Нажатие на кнопку Add Customer"):
            self.add_customer_page.click_add_customer_button()

        with allure.step("Проверка появления алерта"):
            assert self.add_customer_page.is_alert_appeared(2)

    @allure.story("Тестирование добавления 15 новых клиентов")
    def test_add_many_customers(self):
        """Тест на добавление множества корректных клиентов"""
        for _ in range(15):
            self.test_add_customer()


@allure.feature("Тесты страницы Add Customer (не корректные)")
class TestAddCustomerPage_incorrect:
    """Класс некорректных тестов для страницы Add Customer"""

    @pytest.fixture(autouse=True)
    def setup(self, driver_setup):
        """Инициализация драйвера из фикстуры"""
        self.driver = driver_setup
        self.add_customer_page = AddCustomerPage(self.driver)

    @allure.story("Тестирование добавления клиента с пустым first name")
    def test_empty_fname(self):
        """Тест на добавление клиента с пустым полем First Name"""
        with allure.step("Заполнение поля First Name"):
            self.add_customer_page.fill_fname_by_value("")

        with allure.step("Заполнение поля Last Name"):
            self.add_customer_page.fill_lname_by_value("Testov")

        with allure.step("Заполнение поля Post Code"):
            self.add_customer_page.fill_post_code()

        with allure.step("Нажатие на кнопку Add Customer"):
            self.add_customer_page.click_add_customer_button()

        with allure.step("Проверка появления алерта"):
            assert not self.add_customer_page.is_alert_appeared(2)

    @allure.story("Тестирование добавления клиента с пустым last name")
    def test_empty_lname(self):
        """Тест на добавление клиента с пустым полем Last Name"""
        with allure.step("Заполнение поля First Name"):
            self.add_customer_page.fill_fname_by_value("Test")

        with allure.step("Заполнение поля Last Name"):
            self.add_customer_page.fill_lname_by_value("")

        with allure.step("Заполнение поля Post Code"):
            self.add_customer_page.fill_post_code()

        with allure.step("Нажатие на кнопку Add Customer"):
            self.add_customer_page.click_add_customer_button()

        with allure.step("Проверка появления алерта"):
            assert not self.add_customer_page.is_alert_appeared(1)

    @allure.story("Тестирование добавления клиента с пустым post code")
    def test_empty_postcode(self):
        """Тест на добавление клиента с пустым полем Post Code"""
        with allure.step("Заполнение поля First Name"):
            self.add_customer_page.fill_fname_by_value("Test")

        with allure.step("Заполнение поля Last Name"):
            self.add_customer_page.fill_lname_by_value("Testov")

        with allure.step("Заполнение поля Post Code"):
            self.add_customer_page.fill_post_code_by_value("")

        with allure.step("Нажатие на кнопку Add Customer"):
            self.add_customer_page.click_add_customer_button()

        with allure.step("Проверка появления алерта"):
            assert not self.add_customer_page.is_alert_appeared(1)

    @allure.story("Тестирование добавления клиента с некорректным first name")
    def test_incorrect_fname(self):
        """Тест на добавление клиента с некорректным полем First Name"""
        with allure.step("Заполнение поля First Name"):
            self.add_customer_page.fill_fname_by_value("123")

        with allure.step("Заполнение поля Last Name"):
            self.add_customer_page.fill_lname_by_value("Testov")

        with allure.step("Заполнение поля Post Code"):
            self.add_customer_page.fill_post_code()

        with allure.step("Нажатие на кнопку Add Customer"):
            self.add_customer_page.click_add_customer_button()

        with allure.step("Проверка появления алерта"):
            assert not self.add_customer_page.is_alert_appeared(1)

    @allure.story("Тестирование добавления клиента с некорректным last name")
    def test_incorrect_lname(self):
        """Тест на добавление клиента с некорректным полем Last Name"""
        with allure.step("Заполнение поля First Name"):
            self.add_customer_page.fill_fname_by_value("Test")

        with allure.step("Заполнение поля Last Name"):
            self.add_customer_page.fill_lname_by_value("123")

        with allure.step("Заполнение поля Post Code"):
            self.add_customer_page.fill_post_code()

        with allure.step("Нажатие на кнопку Add Customer"):
            self.add_customer_page.click_add_customer_button()

        with allure.step("Проверка появления алерта"):
            assert not self.add_customer_page.is_alert_appeared(1)

    @allure.story("Тестирование добавления клиента с некорректным post code")
    def test_incorrect_postcode(self):
        """Тест на добавление клиента с некорректным полем Post Code"""
        with allure.step("Заполнение поля First Name"):
            self.add_customer_page.fill_fname_by_value("Test")

        with allure.step("Заполнение поля Last Name"):
            self.add_customer_page.fill_lname_by_value("Testov")

        with allure.step("Заполнение поля Post Code"):
            self.add_customer_page.fill_post_code_by_value("not a numbers")

        with allure.step("Нажатие на кнопку Add Customer"):
            self.add_customer_page.click_add_customer_button()

        with allure.step("Проверка появления алерта"):
            assert not self.add_customer_page.is_alert_appeared(1)
