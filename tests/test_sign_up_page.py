import allure


class TestSignUpPage:

    @allure.title("Проверка создания аккаунта")
    @allure.description("Проверка, что можно создать аккаунт")
    def test_create_account_signin_page_is_opened(
        self, sign_in_page, sign_up_page, new_user_data
    ):
        sign_in_page.click_on_create_account_button()
        sign_up_page.create_account(
            new_user_data["first_name"],
            new_user_data["last_name"],
            new_user_data["user_name"],
            new_user_data["email"],
            new_user_data["password"],
        )
        sign_in_page.wait_sign_in_page_is_loaded()
        sign_in_page.check_authorization_form_is_displayed()
        sign_in_page.check_sign_in_page_url()
