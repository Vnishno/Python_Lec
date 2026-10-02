student = {
    "name": "Ana",
    "contacts": {
        "email": "ana@example.com",
        "phone": "555-123-456"
    },
    "courses": {
        "python": {
            "score": 90,
            "passed": True
        },
        "web": {
            "score": 50,
            "passed": False
        }
    }
}

print(student["contacts"]["email"])

print(student["courses"]["python"]["score"])

student["courses"]["web"]["passed"] = True
student["courses"]["web"]["score"] = 65

student["contacts"].pop("phone")