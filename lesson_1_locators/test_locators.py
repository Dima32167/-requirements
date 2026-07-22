from playwright.sync_api import Page, expect
from time import sleep
import re

def test_role_page(page: Page):
    page.goto('https://shop.renlife.ru/')
    locator_nacoplenia = page.locator('//a[@href="/nakopitelnoe-strahovanie-zhizni"]').locator('nth=0')
    locator_nacoplenia.click()
    button = page.get_by_role('link', name='Главная')
    expect(button).to_be_visible()

def test_text_locators(page: Page):
    page.goto('https://shop.renlife.ru/')
    button = page.get_by_text('Инвестиции')
    expect(button).to_be_visible()
    button.click()
    sleep(9)

def test_placeholder_locators(page: Page):
    page.goto('https://shop.renlife.ru/')
    page.get_by_role("link", name="Инвестиции").nth(0).click()
    sleep(9)

def test_dz_1(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    username = page.get_by_role('textbox', name='username')
    password = page.get_by_role('textbox', name='password')
    username.fill('username')
    password.fill('password')
    expect(username).to_have_value('username')
    expect(password).to_have_value('password')
    login = page.get_by_role('button', name=' Login')
    login.click()
    # sleep(1)
    expect(page.locator("#flash")).to_contain_text('Your username is invalid!')
    # sleep(1)
    expect(username).to_have_value('')
    expect(password).to_have_value('')

def test_dz_2(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')


