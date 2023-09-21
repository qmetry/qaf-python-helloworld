# from qaf import StepListener
# from qaf import pluginmagager
# from qaf.automation.bdd2.qaf_teststep import StepTracker
# from qaf.automation.core.reporter import Reporter
# from qaf.listeners import qafhook
#
#
# class StepListenerImpl(StepListener):
#     @qafhook
#     def before_step(self, step_tracker: StepTracker):
#         Reporter.info(f"StepListener: {step_tracker.name}")
#         print(step_tracker.name)
#
#
# pluginmagager.register(StepListenerImpl())
