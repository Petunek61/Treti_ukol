import pytest
from playwright.sync_api import Page, expect


def test_cookies(page: Page):
    page.goto("https://www.wilsonka.cz/")

    # Očekáváme zobrazení tlačítka "Rozumím"
    reject_button = page.locator("body > div.cc_banner-wrapper > div > a.cc_btn.cc_btn_accept_all")
    reject_button.wait_for(timeout=10000)
    reject_button.click()

    # Ověření, že cookie lišta zmizela
    cookie_div = page.locator("body > div.cc_banner-wrapper > div")
    expect(cookie_div).not_to_be_visible()

def test_hledat(page: Page):
    page.goto("https://www.wilsonka.cz/")
    input = page.locator("#hlavni > div.hlavicka.home > form > fieldset > input.fraze")    
    input.fill("Provozní řád")
    input.press("Enter")
    page.wait_for_timeout(3000)
    assert page.url == "https://www.wilsonka.cz/search/"


def test_title(page: Page):
    page.goto("https://www.wilsonka.cz/")
    
    with page.expect_popup() as popup:
        button = page.locator("#hlavni > div.obsah.home > div.home_vpravo > a:nth-child(6) > img")
        button.click()

    new_page = popup.value
    assert new_page.url.startswith("https://www.facebook.com/people/Autocamp-Wilsonka")


    