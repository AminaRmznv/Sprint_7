import pytest

import helper


@pytest.fixture
def new_courier():
    return helper.register_new_courier_and_return_login_password()

