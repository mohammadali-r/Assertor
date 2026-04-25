from tests.coftest import user_service

def test_get_users(user_service):
    user_ids, status = user_service.get_users()

    assert status == 200
    assert len(user_ids) == 10