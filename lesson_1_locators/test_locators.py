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
    first_name = page.get_by_role('textbox', name='first Name')
    first_name.fill('Dima')
    last_name = page.get_by_role('textbox', name='last name')
    last_name.fill('Artamonov')
    email = page.get_by_placeholder('name@example.com')
    email.fill('dima1993@mail.com')
    gender = page.get_by_role('radio', name='Female')
    gender.click()
    mobile = page.get_by_role('textbox', name='Mobile Number')
    mobile.fill('9117728820')
    data_locator = page.locator('#dateOfBirthInput')
    data_locator.click()
    page.locator(".react-datepicker__day--023").click()
    expect(page.locator(".react-datepicker")).to_be_hidden()
    subjects = page.locator("#subjectsInput")
    subjects.fill("English")
    page.get_by_text("English", exact=True).click()
    hobbies = page.get_by_role('checkbox', name='Music')
    hobbies.click()
    button = page.get_by_role('button', name='Submit')
    button.click()
    sleep(3)




