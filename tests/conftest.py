import pytest
from selenium import webdriver
import json
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture(scope='session')
def browser_config():

    with open('config.json') as f:
        config = json.load(f)
    return config
    
@pytest.fixture
def browser(browser_config):
    if browser_config['browser'].casefold() == "chrome":
        options = ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        b=webdriver.Chrome(options=options, )
    elif browser_config['browser'].casefold() == "firefox":
        b=webdriver.Firefox()
    elif browser_config['browser'].casefold() == "safari":
        b=webdriver.Safari()
    b.maximize_window()
    b.implicitly_wait(browser_config["implicit_wait"])
    yield b
    b.quit()
