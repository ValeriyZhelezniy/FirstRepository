import requests

class GitHub:
    def get_user_defunkt(self):
        r = requests.get('http://api.github.com/users/defunkt')
        body = r.json()

        return body