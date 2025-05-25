import os

valid_user = {
    "name": os.getenv("SECRET_NAME"),
    "email": os.getenv("SECRET_EMAIL"),
    "password": os.getenv("SECRET_PASSWORD"),
    "address": "123 Test St, QA City",
    "first_name": "John",
    "last_name": "Smith",
    "company": "Google",
    "state": "California",
    "city": "Cupertino",
    "zip": "94024",
    "mobile_number": "+987654321",
    "subject": "Test Subject",
    "message": "Test Message",

}

invalid_user = {
    "email": "johntestexample@proton.me",
    "password": "12345",
    "address": ""
}