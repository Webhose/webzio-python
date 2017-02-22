import requests


class Session(object):

    def __init__(self, token=None):
        self.next_call = None
        self.session = requests.Session()
        self.token = token

    def query(self, end_point_str, param_dict=None):

        if param_dict is not None:
            param_dict.update({"token": self.token})
        else:
            param_dict = {
                "format": "json",
                "token": self.token
            }



        response = self.session.get("http://webhose.io/" + end_point_str, params=param_dict)
        if response.status_code != 200:
            raise Exception(response.text)

        _output = response.json()
        self.next_call = _output['next']
        return _output

    def get_next(self):
        return self.query(self.next_call[1:])


__session = Session()


def config(token):
    __session.token = token


def query(end_point_str, param_dict=None):
    return __session.query(end_point_str, param_dict)


def get_next():
    return __session.get_next()


