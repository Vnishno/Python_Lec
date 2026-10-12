from functools import wraps


def require_role(allowed_role="admin"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_role = kwargs.get("user_role")

            if user_role == allowed_role:
                return func(*args, **kwargs)
            else:
                print("Permission Denied: User is not an admin.")
                return None

        return wrapper

    return decorator

@require_role(allowed_role="admin") 
def delete_database(user_role):
    return "Database deleted successfully!"

res1 = delete_database(user_role="admin")
print(res1)

res2 = delete_database(user_role="user")
print(res2)