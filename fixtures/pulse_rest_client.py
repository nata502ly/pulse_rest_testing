import requests


class PulseRestAPI:
    def __init__(self, resource):
        self.host = "pulse-rest-testing.herokuapp.com"
        self.resource = resource
        self.url = 'http://{}/{}/'.format(self.host, self.resource)

    def create_object(self, obj):
        obj_data = obj.get_dict()
        response = requests.post(self.url, data=obj_data)
        if response.status_code == 201:
            obj.set_id(response.json()["id"])
        return response

    def get_objects(self):
        pass

    def get_object(self, obj):
        pass

    def modify_object(self, obj):
        pass

    def delete_object(self, obj):
        response = requests.delete(self.url + str(obj._id) + '/')
        return response
