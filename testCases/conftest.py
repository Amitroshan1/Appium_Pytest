from appium import webdriver
from appium.options.android import UiAutomator2Options
import pytest
from time import sleep

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    udid='eb90285c',
    ignoreHiddenApiPolicyError = 'true',
    noReset = 'true',
    newCommandTimeout= 600
      )
appium_server_url = 'http://localhost:4723'
@pytest.fixture()
def setup():
    driver=webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    return driver



capabilitie = dict(
    platformName='Android',
    automationName='uiautomator2',
    udid='fa499298',
    ignoreHiddenApiPolicyError = 'true',
    noReset = 'true',
    newCommandTimeout= 600
      )
appium_ser_url = 'http://localhost:4723'


@pytest.fixture()
def setup2():
    driver2=webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilitie))
    return driver2



