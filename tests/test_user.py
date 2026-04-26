from tests.conftest import user_service
import allure

@allure.title("get users")
@allure.description("Test /users endpoint, validate response status code and number of users returned")
def test_get_users(user_service):

    with allure.step("Call GET method from /users"):
        user_ids, status = user_service.get_users()

    with allure.step("Validate response status code and number of users returned"):
        assert status == 200
        assert len(user_ids) == 10