"""Модуль с тестами для страницы Customers"""

import allure
import pytest

from pages.CustomersPage import CustomersPage


@allure.feature("Тестирование страницы Customers")
class TestCustomersPage:
    """Класс тестов страницы Customers"""

    @pytest.fixture(autouse=True)
    def setup(self, driver_setup):
        """Инициализация драйвера из фикстуры"""
        self.driver = driver_setup
        self.customers_page = CustomersPage(self.driver)

    @allure.story("Сортировка клиентов по имени (First Name)")
    def test_customers_sort(self):
        """Проверяет корректность сортировки клиентов в обратном и прямом порядке."""

        before_sort = self.customers_page.get_fnames()
        self.customers_page.sort_by_fname()
        after_sort = self.customers_page.get_fnames()

        with allure.step("Проверка отсортированности в обратном порядке"):
            print(f"python sorted: {sorted(before_sort, reverse=True)}")
            print(f"service sorted: {after_sort}")
            assert sorted(before_sort, reverse=True) == after_sort

        with allure.step("Проверка отсортированности в прямом порядке"):
            self.customers_page.sort_by_fname()
            after_sort = self.customers_page.get_fnames()
            print(f"python sorted: {sorted(before_sort, reverse=False)}")
            print(f"service sorted: {after_sort}")
            assert sorted(before_sort, reverse=False) == after_sort

    @allure.story("Удаление клиента с длинной First Name, ближайшей к среднему значению длин всех First Name")
    def test_remove_particular_customer(self):
        """Тест на удаление клиента с длиной First Name,
        ближайшей к среднему значению длин всех First Name.
        """
        before_remove = self.customers_page.get_fnames()
        self.customers_page.remove_customer_with_avg_fname_len()
        after_remove = self.customers_page.get_fnames()
        assert len(before_remove) - 1 == len(after_remove)

    @allure.story("Удаление всех оставшихся клиентов")
    def test_remove_all(self):
        """Проверяет, что после удаления всех клиентов список клиентов пуст."""
        fnames = self.customers_page.get_fnames()
        for fname in fnames:
            self.customers_page.remove_customer(fname)
        fnames = self.customers_page.get_fnames()

        assert len(fnames) == 0
