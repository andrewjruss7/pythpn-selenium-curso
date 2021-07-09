import request
import random


class ApiDataMock:
    response = request.get(
        'https://my.api.mockaroo.com/python_api_curso.json?key=7f200b40')
    data = response.json()

    i = random.randint(0, 99)

    first_name = data[i]['first_name']
    last_name = data[i]['last_name']
    email_address = data[i]['email_address']
    password = data[i]['password']
