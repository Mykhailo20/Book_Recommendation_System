from datetime import datetime
from dateutil import parser

from db.models import DbBook


def update_book(response_dict: dict, book: DbBook):
    if 'publish_date' in response_dict.keys():
        try:
            parsed_date = parser.parse(response_dict['publish_date'])
            book.publication_year = parsed_date.year

        except Exception as e:
            print(f"Exception occurred while parsing publish_date: {e}")
            return False
    # if publication_year was successfully updated or no 'publish_date' in response - set updated_at as CURRENT_TIMESTAMP 
    book.updated_at = datetime.now()
    return True