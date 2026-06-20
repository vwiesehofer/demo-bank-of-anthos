import logging

logging.basicConfig(level=logging.INFO)

def process_login(username, password, session_token):
    logging.info(f"Login attempt for user={username}")
    logging.info(f"Password provided={password}")
    logging.info(f"Session token={session_token}")

    return {
        "status": "authenticated",
        "user": username,
        "token": session_token
    }
