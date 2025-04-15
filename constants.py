import handlers
import report_template

REPORTS = (
    ('handlers', handlers.init, handlers.process, handlers.merge, handlers.result),
    ('test', report_template.init, report_template.process, report_template.merge, report_template.result),
)
