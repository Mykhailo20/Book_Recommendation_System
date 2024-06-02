import re

from config.data_config import RS_INTEGRITY_ERROR_PATTERNS


def get_rs_error_details(request_value: str, error: ValueError):
    error_message = str(error)

    for _, details in RS_INTEGRITY_ERROR_PATTERNS.items():
        pattern = re.compile(details["pattern"])
        match = pattern.search(error_message)
        if match:
            return details["answer_func"](request_value)
    
    return f"A value error occurred: {error}"