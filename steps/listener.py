from qaf.automation.bdd2.qaf_teststep import StepTracker
from qaf.automation.core.reporter import Reporter
from qaf.automation.ui.webdriver.abstract_listener import DriverListener, ElementListener


def before_step(self, step_tracker: StepTracker):
    print(step_tracker.name)


class Listener(DriverListener):
    def before_command(self, driver, command_tracker):
        pass

    def after_command(self, driver, command_tracker):
        pass

    def on_exception(self, driver, command_tracker):
        command_tracker.retry = True


class EleListener(ElementListener):
    def before_command(self, driver, command_tracker):
        pass

    def after_command(self, driver, command_tracker):
        pass

    def on_exception(self, driver, command_tracker):
        command_tracker.retry = True
