import re
from sqlalchemy.exc import IntegrityError

from routers.schemas import UserBase
from config.data_config import DB_INTEGRITY_ERROR_PATTERNS



def get_db_error_details(request: UserBase, error: IntegrityError):
    error_message = str(error.orig)

    for field, details in DB_INTEGRITY_ERROR_PATTERNS.items():
        pattern = re.compile(details["pattern"])
        match = pattern.search(error_message)
        if match:
            value = getattr(request, field.split('_')[0]) if '_' in field else getattr(request, field)
            return details["answer_func"](value)
    
    return f"An integrity error occurred: {error}"