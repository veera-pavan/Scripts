def main():
    print("welcome to the email slicer")
    print("")

    email_input=input("enter email id: ")
    (username, domain) = email_input.split("@")
    (domain,extension) = domain.split(".")

    print("user name =" + username)
    print("domain name = " + domain)
    print("extension = " + extension)
while True:
    main()