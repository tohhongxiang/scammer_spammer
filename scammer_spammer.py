import bs4, requests, random
import string
# import rsa

url = r'http://rewardfreegift2019-garena.ga/account-login.php'

# var pw = document.loginForm.password.value;
#             document.loginForm.password2.value=RSA(pw); ???

# (private_key, public_key) = rsa.newkeys(256, accurate=False)
first_names = []
last_names = []
chars = string.ascii_letters + string.digits + r"!@#$%^&*(){}[]-=\|;:'\,<.>/?"

with open('names.txt', 'r') as f:
    content = f.readlines()

content = [w.replace('\n', '').split(' ') for w in content]
for w in content:
    first_names.append(w[0])
    last_names.append(w[1])

for i in range(10000):
    name = (random.choice(first_names) + random.choice(last_names) + ''.join(random.choice(string.digits) for i in range(random.randint(0,5)))).lower()
    password = ''.join(random.choice(chars) for i in range(random.randint(8, 15)))
    # password2 = rsa.encrypt(password.encode('utf-8'), public_key)
    password2 = ''.join(random.choice(string.digits+string.ascii_lowercase) for i in range(256))
    requests.post(url, allow_redirects=False, data={
        'username': name,
        'password': password,
        'password2': password2
    })
    print("Username: {}, password: {}, password2: {}".format(name, password, password2))


