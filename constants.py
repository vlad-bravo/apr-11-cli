import handlers
import report_template

REPORTS = (
    ('handlers', handlers.init, handlers.process, handlers.result),
    ('test', report_template.init, report_template.process, report_template.result),
)
