import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def test_selene():
    browser.open('https://google.com')

    yield


@pytest.fixture(scope="function", autouse=True)
def test_size():
    browser.config.window_width = 1680
    browser.config.window_height = 1050



def test_1(test_selene):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_2(test_selene):
    browser.element('[name="q"]').should(be.blank).type('цвцвцвцвцвцвцвцвцвцвцапапапапапа').press_enter()
    browser.element('[id="search"]').should(have.text('По запросу ничего не найдено.'))
