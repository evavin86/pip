import re #Модуль регулярных выражений (для проверки текста)
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    #переходит по ссылке, чтобы начать тестирование
    page.goto("https://demo.playwright.dev/todomvc/#/")
    # Ожидается, что заголовок будет содержать строчку
    expect(page).to_have_title(re.compile("Python"))

def test_get_started_link(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")

    # Нажмет ссылку «Начать»
    page.get_by_role("link", name="Docs").click()
    #Ожидается, что страница будет иметь заголовок с названием «Установка»
    expect(page).to_have_url(re.compile("docs"))
