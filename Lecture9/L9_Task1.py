def create_user_profile(first_name, last_name, role="Student", is_active=True):
    user_profile = {
        "First_name": first_name,
        "Last_name": last_name,
        "role": role,
        "is_active": is_active
    }
    return user_profile

user1 = create_user_profile("Giorgi", "Nishnianidze")
print(user1)

user2 = create_user_profile("Nino", "Kapanadze", role="Teacher", is_active=False)
print(user2)