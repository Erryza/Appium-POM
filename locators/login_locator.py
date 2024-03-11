from appium.webdriver.common.appiumby import AppiumBy


class LoginLocator:
    option_login_btn = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Btn6']")
    input_email = (
        AppiumBy.XPATH,
        "//android.widget.EditText[@resource-id='com.code2lead.kwad:id/Et4']",
    )
    input_password = (
        AppiumBy.XPATH,
        "//android.widget.EditText[@resource-id='com.code2lead.kwad:id/Et5']",
    )
    login_btn = (
        AppiumBy.XPATH,
        "//android.widget.Button[@resource-id='com.code2lead.kwad:id/Btn3']",
    )
