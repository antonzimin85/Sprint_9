import os
import pytest
from faker import Faker
from selenium import webdriver

from pages.create_recipe_page import CreateRecipePage
from pages.recipe_page import RecipePage
from pages.recipes_page import RecipiesPage
from pages.sign_in_page import SignInPage
from pages.sign_up_page import SignUpPage


@pytest.fixture(scope="function")
def driver(request):
    selenoid_url = os.getenv("SELENOID_URL", "http://selenoid:4444/wd/hub")

    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument("--start-maximized")

    options.set_capability(
        "selenoid:options",
        {
            "enableVNC": True
        })

    driver = webdriver.Remote(
        command_executor=selenoid_url,
        options=options
    )

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def new_user_data():
    faker = Faker()
    first_name = faker.first_name()
    last_name = faker.last_name()
    user_name = faker.user_name()
    email = faker.safe_email()
    password = faker.password(
        length=8, special_chars=False, upper_case=False, digits=False
    )
    new_user_data = {
        "first_name": first_name,
        "last_name": last_name,
        "user_name": f"{user_name}tstzim",
        "email": f"{email}tstzim",
        "password": password,
    }
    return new_user_data


@pytest.fixture(scope="function")
def sign_in_page(driver):
    sign_in_page = SignInPage(driver)
    sign_in_page.open_sign_in_page()
    return sign_in_page


@pytest.fixture(scope="function")
def sign_up_page(driver):
    sign_up_page = SignUpPage(driver)
    return sign_up_page


@pytest.fixture(scope="function")
def recipies_page(driver):
    recipies_page = RecipiesPage(driver)
    return recipies_page


@pytest.fixture(scope="function")
def recipe_page(driver):
    recipe_page = RecipePage(driver)
    return recipe_page


@pytest.fixture(scope="function")
def create_recipe_page(driver):
    create_recipe_page = CreateRecipePage(driver)
    return create_recipe_page


@pytest.fixture(scope="function")
def create_account(sign_in_page, sign_up_page, new_user_data):
    sign_in_page.click_on_create_account_button()
    sign_up_page.create_account(
        new_user_data["first_name"],
        new_user_data["last_name"],
        new_user_data["user_name"],
        new_user_data["email"],
        new_user_data["password"],
    )


@pytest.fixture(scope="function")
def create_account_and_login(sign_in_page, sign_up_page, recipies_page, new_user_data):
    sign_in_page.click_on_create_account_button()
    sign_up_page.create_account(
        new_user_data["first_name"],
        new_user_data["last_name"],
        new_user_data["user_name"],
        new_user_data["email"],
        new_user_data["password"],
    )
    sign_in_page.wait_sign_in_page_is_loaded()
    sign_in_page.enter_email(new_user_data["user_name"])
    sign_in_page.enter_password(new_user_data["password"])
    sign_in_page.click_on_enter_button()
    recipies_page.wait_recipies_page_is_loaded()
