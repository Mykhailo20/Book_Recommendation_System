ONE_BOOK_RS_RECOMMEND_BOOKS_NO = 5

DB_INTEGRITY_ERROR_PATTERNS = {
    "username_unique": {
        "pattern": r'Key \(username\)=\((.+?)\) already exists',
        "answer_func": lambda username: f"User with username '{username}' already exists."
    },
    "email_unique": {
        "pattern": r'Key \(email\)=\((.+?)\) already exists',
        "answer_func": lambda email: f"User with email '{email}' already exists."
    },
    "email_check": {
        "pattern": r'relation \"user\" violates check constraint \"user_email_check\"',
        "answer_func": lambda email: f"The email '{email}' is not valid."
    }
}