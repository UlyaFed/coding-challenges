def valid_username(username):
    if len(username) < 6:
        return False
    if "_" not in username:
        return False
    else:
        return True
    
def process_username(username):
    if not valid_username(username):
        return "Invalid username. Please enter a valid username."
    
    year_group = username[:2]
    initial = username[2]
    lastname = username[3:username.index("_")]
    role = username[username.index("_")+1:]
    
    if role not in ["S","T","A"]:
        return "Invalid username. Please enter a valid username."
    if role == "S":
        user_type ="Student"
        year_group_t = f"Year Group:{year_group}"
    elif role == "A":
        user_type ="Admin Staff"
        year_group_t = ""
    else:
        user_type ="Teacher"
        year_group_t = ""
    
    return f"{user_type}\nInitial: {initial}\nLast Name: {lastname}\n{year_group_t}"

def check():
    username = input("Enter your username(example:09kJohnson_S):") 
    result = process_username(username)
    print(result)
    
check()
