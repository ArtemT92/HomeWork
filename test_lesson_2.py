import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def test_selene():
    browser.open('https://google.com')

    yield


@pytest.fixture()
def test_size():
    browser.set_window_size(800, 600)



def test_1(test_selene):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_2(test_selene):
    browser.element('[name="q"]').should(be.blank).type('цвцвцвцвцвцвцвцвцвцвцапапапапапа').press_enter()
    browser.element('[id="search"]').should(have.text('По запросу ничего не найдено.'))
