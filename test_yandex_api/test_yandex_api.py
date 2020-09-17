import unittest
import requests

YD_API_KEY = 'OAuth <токен>'
YD_URL = 'https://cloud-api.yandex.net/v1/disk/resources'


class Test(unittest.TestCase):
    def test_create_folder(self):
        name = 'Test'
        headers = {'Authorization': YD_API_KEY}
        params = {'path': name}
        URL = YD_URL + '?path=' + name
        resp = requests.put(URL, headers=headers, params=params)
        answer = str(resp)
        if answer == '<Response [409]>':
            print(f'Папка {name} уже существует.')
        else:
            self.assertEqual('<Response [201]>', answer)
            print(f'Папка {name} создана.')


if __name__ == '__main__':
    unittest.main()
