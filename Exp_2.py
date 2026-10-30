# user_module.py

def format_user_profile(name, age, profession):
    """Takes user data and formats it into a clean profile string."""
    profile = (
        f"--- USER PROFILE ---\n"
        f"Name:       {name.title()}\n"
        f"Age:        {age}\n"
        f"Profession: {profession.capitalize()}\n"
        f"--------------------"
    )
    return profile