# conftest.py
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption("--tags",action="store",default=None,help="Run tests matching this tag")


def pytest_collection_modifyitems(items, config):
    tag_filter = config.getoption("--tags")
    if not tag_filter:
        return

    selected = []
    deselected = []

    for item in items:
        marker = item.get_closest_marker("tags")
        if marker and tag_filter in marker.args:
            selected.append(item)
        else:
            deselected.append(item)

    if selected:
        config.hook.pytest_deselected(items=deselected)
        items[:] = selected

@pytest.fixture
def driver():
    options = Options()

    # Disable password manager popups
    options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})

    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)  # if you still have this — otherwise skip

    yield driver

    driver.quit()