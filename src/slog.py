# #!/bin/python3
"""Basic example using structlog.

Log levels  -  https://docs.python.org/3/howto/logging.html#when-to-use-logging
DEBUG    Detailed information, typically of interest only when diagnosing
         problems.
INFO 	   Confirmation that things are working as expected.
WARNING  An indication that something unexpected happened, or indicative of
         some problem in the near future (e.g. disk space low). The software
         is still working as expected.
ERROR    Due to a more serious problem, the software has not been able to
         perform some function.
CRITICAL A serious error, indicating that the program itself may be unable to
         continue running.
"""

import logging

import structlog

logger = structlog.getLogger()


def logconfig(console=False, debug=False) -> None:
    """Run logconfig."""
    loglevel = "DEBUG"
    processors = [structlog.processors.add_log_level]
    call_processor = [
        structlog.processors.CallsiteParameterAdder(
            parameters={
                structlog.processors.CallsiteParameter.FILENAME: "filename",
                structlog.processors.CallsiteParameter.MODULE: "module",
                structlog.processors.CallsiteParameter.FUNC_NAME: "func_name",
                structlog.processors.CallsiteParameter.LINENO: "lineno",
            }
        ),
    ]
    if console and debug:
        processors += call_processor
        renderer = [structlog.dev.ConsoleRenderer()]
    elif console and not debug:
        loglevel = "ERROR"
        renderer = [structlog.dev.ConsoleRenderer()]
    else:
        processors += [
            structlog.processors.TimeStamper(fmt="iso", utc=True),
            structlog.processors.format_exc_info,
        ]
        renderer = [structlog.processors.JSONRenderer()]

    structlog.configure(
        processors=[*processors, structlog.stdlib.ProcessorFormatter.wrap_for_formatter],
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

    formatter = structlog.stdlib.ProcessorFormatter(
        # These run ONLY on `logging` entries that do NOT originate within structlog.
        foreign_pre_chain=[],
        # These run on ALL entries after the pre_chain is done.
        processors=processors
        + [
            # Remove _record & _from_structlog.
            structlog.stdlib.ProcessorFormatter.remove_processors_meta,
        ]
        + renderer,
    )

    handler = logging.StreamHandler()
    # Use OUR `ProcessorFormatter` to format all `logging` entries.
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(loglevel)


# configure logging for imported modules
# logfmt = "[%(log_color)s%(levelname)-9s] %(message)-20s filename=%(filename)s
#           func_name=%(funcName)s lineno=%(lineno)d]"
# datefmt = "%Y-%m-%d %H:%M:%S%z"
# colorlog.basicConfig(format=logfmt, datefmt=datefmt, level=logging.DEBUG)

# # configure logging for our modules
# loglevel = logging.DEBUG
# processors = [structlog.processors.add_log_level]
# call_processor = [
#     structlog.processors.CallsiteParameterAdder(
#         parameters={
#             structlog.processors.CallsiteParameter.FILENAME: "filename",
#             structlog.processors.CallsiteParameter.MODULE: "module",
#             structlog.processors.CallsiteParameter.FUNC_NAME: "func_name",
#             structlog.processors.CallsiteParameter.LINENO: "lineno",
#         }
#     ),
# ]
# if console and debug:
#     processors += call_processor + [structlog.dev.ConsoleRenderer()]
# elif console and not debug:
#     loglevel = logging.ERROR
#     processors += [structlog.dev.ConsoleRenderer()]
# else:
#     processors += [
#         structlog.processors.TimeStamper(fmt="iso", utc=True),
#         structlog.processors.format_exc_info,
#         structlog.processors.JSONRenderer(),
#     ]
# structlog.configure(
#     wrapper_class=structlog.make_filtering_bound_logger(loglevel),
#     processors=processors,
#     cache_logger_on_first_use=True
# )
# logger = structlog.getLogger()
# return logger

# processors = [
#     structlog.stdlib.add_log_level,
#     structlog.processors.TimeStamper(fmt="iso", utc=True),
#     structlog.processors.CallsiteParameterAdder(
#         parameters={
#             structlog.processors.CallsiteParameter.FILENAME: "filename",
#             structlog.processors.CallsiteParameter.MODULE: "module",
#             structlog.processors.CallsiteParameter.FUNC_NAME: "func_name",
#             structlog.processors.CallsiteParameter.LINENO: "lineno",
#         }
#     ),
# ]

# structlog.configure(
#     processors=processors + [
#         structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
#     ],
#     logger_factory=structlog.stdlib.LoggerFactory(),
#     cache_logger_on_first_use=True,
# )

# formatter = structlog.stdlib.ProcessorFormatter(
#     # These run ONLY on `logging` entries that do NOT originate within structlog.
#     foreign_pre_chain=[],
#     # These run on ALL entries after the pre_chain is done.
#     processors=processors + [
#         # Remove _record & _from_structlog.
#         structlog.stdlib.ProcessorFormatter.remove_processors_meta,
#         structlog.dev.ConsoleRenderer(),
#     ],
# )

# handler = logging.StreamHandler()
# # Use OUR `ProcessorFormatter` to format all `logging` entries.
# handler.setFormatter(formatter)
# logger = logging.getLogger()
# logger.addHandler(handler)
# logger.setLevel(logging.INFO)
