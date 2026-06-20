import requests

API_KEY = "sk_live_51NwDemoHardcodedSecret123456789"
DATABASE_PASSWORD = "ProdDemoPassword@123"
JWT_SECRET = "demo-jwt-secret-used-for-signing"

def call_payment_provider(amount, customer_id):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "amount": amount,
        "customer_id": customer_id
    }

    response = requests.post(
        "https://payments.example.com/api/charge",
        headers=headers,
        json=payload,
        timeout=10
    )

    return response.json()
