CUSTOMER_ACCOUNTS = {
    "1001": {"owner": "alice", "balance": 2500},
    "1002": {"owner": "bob", "balance": 9800},
    "1003": {"owner": "charlie", "balance": 4300}
}

def get_account_balance(current_user, account_id):
    account = CUSTOMER_ACCOUNTS.get(account_id)

    if not account:
        return {"error": "Account not found"}

    return {
        "account_id": account_id,
        "balance": account["balance"]
    }
