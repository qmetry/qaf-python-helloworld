from time import sleep

from qaf.automation.core import get_bundle
from qaf.automation.step_def.common_steps import *
from qaf.automation.ui.webdriver.qaf_web_element import _
#from qaf.automation.bdd2 import step

class Navigation:
    @step("user navigates to login screen")
    def navigate_to_login_screen(self):
        get("/login.html")

    @step("login using {email} and {password}")
    def doLogin(self, email: str, password: str):
        _("loginpage.username.loc").send_keys("" + email)
        _("loginpage.password.loc").send_keys("" + password)
        _("loginpage.login.loc").click()
        # Reporter.log_with_screenshot("Login Form Submitted")


@step("verify {user} successfully logged in")
def verify_user_logged_in(user: str):
    """
    On successfully logg in user account screen should be displayed
    """
    _("useraccountpage.username.loc").assert_present()
    _("useraccountpage.username.loc").verify_text(user)


@step("verify login username error is {message}")
def verify_username_error(message):
    _verify_error("loginpage.username-error.loc", message)


@step("verify login password error is {message}")
def verify_password_error(message):
    _verify_error("loginpage.password-error.loc", message)


@step("verify login form error is {message}")
def verify_login_error(message):
    _verify_error("loginpage.login-error.loc", message)


@step("verify '{field}' error is '{message}'")
def _verify_error(field, message):
    if message:
        _(field).verify_text(message)
    else:
        _(field).verify_not_visible()

nav = Navigation()