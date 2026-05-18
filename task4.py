email = input("Enter email: ").strip()
def validate_email(email_str):
    return "@" in email_str and "." in email_str

print("Valid email" if validate_email(email) else "Invalid email")