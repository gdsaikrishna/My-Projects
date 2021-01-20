email = str(input("Enter your email : "))
if(email.find("@") != -1):
    username = email[:email.index("@")]
    domain_name = email[email.index("@")+1:]
    format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
    print(format_)
else:
    print("Enter a valid email id")