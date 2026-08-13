from playwright.sync_api import Page, expect

def test_auth(page: Page):
    page.goto('https://stepik.org/catalog?auth=login')
    expect(page.get_by_role("link", name="Войти").nth(0)).to_be_visible()
    page.get_by_placeholder("E-mail").fill('Dima199718@mail.ru')
    page.get_by_placeholder("Пароль").fill('dima199718')
    page.get_by_role("button", name="Войти").click()
    expect(page.get_by_role("link", name="Войти").nth(0)).to_be_hidden()
    page.context.storage_state(path="storage_state.json")

