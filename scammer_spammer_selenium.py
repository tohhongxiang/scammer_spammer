import string, random
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()



url = r'http://rewardfreegift2019-garena.ga/index.php?code=SG'
# var pw = document.loginForm.password.value;
#             document.loginForm.password2.value=RSA(pw); he uses rsa encryption

first_names = []
last_names = []
chars = string.ascii_letters + string.digits + r"!@#$%^&*(){}[]-=\|;:'\,<.>/?"

with open('names.txt', 'r') as f:
    content = f.readlines()

content = [w.replace('\n', '').split(' ') for w in content]
for w in content:
    first_names.append(w[0])
    last_names.append(w[1])


driver.get(url)
first_click = driver.find_element_by_class_name("bg-cover")
first_click.click()
sleep(1)
ok_btn = driver.find_element_by_class_name("swal-button")
ok_btn.click()

while True:
    username_field = driver.find_element_by_name('username')
    password_field = driver.find_element_by_name('password')

    name = (random.choice(first_names) + random.choice(last_names) + ''.join(random.choice(string.digits) for i in range(random.randint(0, 5)))).lower()
    password = ''.join(random.choice(chars) for i in range(random.randint(8, 15)))

    username_field.send_keys(name)
    password_field.send_keys(password)

    login_btn = driver.find_element_by_name("submit_button")
    login_btn.click()


