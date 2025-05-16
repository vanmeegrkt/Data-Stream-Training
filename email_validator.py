# You are given a list of employee records (full name and email). You need to:
# - Validate the email (must start with a letter and contain @company.com)
# - Generate a lowercase username in the format firstname.lastname

employees = [
    {"name": "Alice Johnson", "email": "Alice.J@company.com"},
    {"name": "Bob Smith", "email": "bob.smith@company.com"},
    {"name": "  Carol Lee", "email": "carol.lee@otherdomain.com"},
]

for emp in employees:
    name = emp["name"].strip()
    email = emp["email"].strip().lower()

    # Validate email
    if not email.startswith(name[0].lower()):
        print(f"Invalid email for {name}: {email} - must start with {name[0].lower()}")
        continue
    if not email.endswith("@company.com"):
        print(f"Invalid domain for {name}: {email} - must end with @company.com")
        continue

    # Generate username
    parts = name.lower().split()
    if len(parts) >= 2:
        username = f"{parts[0]}.{parts[1]}"
    else:
        username = f"{parts[0]}"

    # Output result
    print(f" Name: {name} | Email: {email.replace('@company.com', '@altimetrik.com')} | Username: {username}")