import requests
import random
import string
from random import randint

url = 'https://chk05be.ml/api/login'
chars = string.ascii_letters + string.digits + '!@#$%^&*()'



def main():

    randomuser = ''.join(random.choice(string.digits) for i in range(random.randint(5, 10)))
    randompass = ''.join(random.choice(chars) for i in range(8))
    data = {
        'Username': randomuser,
        'Password': randompass
        }

    response = requests.post(url, data=data).text

    print(response)

main()
