"""
Created on 13 Nov 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

api auth:
{"org-id": "south-coast-science-dev", "api-key": "43308b72-ad41-4555-b075-b4245c1971db"}

device auth:
{"user-id": "southcoastscience-dev", "client-id": "5873", "client-password": "d4MctQFa"}
"""

from scs_core.osio.client.rest_client import RESTClient
from scs_core.osio.data.device import Device


# --------------------------------------------------------------------------------------------------------------------

class DeviceManager(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, http_client, api_key):
        """
        Constructor
        """
        self.__rest_client = RESTClient(http_client, api_key)


    # ----------------------------------------------------------------------------------------------------------------

    def find(self, org_id, client_id):
        path = '/v1/orgs/' + org_id + '/devices/' + client_id

        # request...
        self.__rest_client.connect()

        try:
            response_jdict = self.__rest_client.get(path)
        except RuntimeError:
            response_jdict = None

        self.__rest_client.close()

        device = Device.construct_from_jdict(response_jdict)

        return device


    def find_for_name(self, org_id, name):                  # used by: osio/device
        devices = self.find_all_for_org(org_id)

        for device in devices:
            if device.name == name:
                return self.find(org_id, device.client_id)  # get the full-fat version

        return None


    def find_all_for_user(self, user_id):                   # used by: osio/device_list
        path = '/v1/users/' + user_id + '/devices'

        # request...
        self.__rest_client.connect()

        try:
            response_jdict = self.__rest_client.get(path, {'user-id': user_id})

        finally:
            self.__rest_client.close()

        devices = [Device.construct_from_jdict(jdict) for jdict in response_jdict] if response_jdict else []

        return devices


    def find_all_for_org(self, org_id):                     # used by: osio/device_list
        path = '/v1/orgs/' + org_id + '/devices'

        # request...
        self.__rest_client.connect()

        try:
            response_jdict = self.__rest_client.get(path)

        finally:
            self.__rest_client.close()

        devices = [Device.construct_from_jdict(jdict) for jdict in response_jdict] if response_jdict else []

        return devices


    # ----------------------------------------------------------------------------------------------------------------

    def create(self, user_id, device):
        path = '/v1/users/' + user_id + '/devices'

        # request...
        self.__rest_client.connect()

        try:
            response_jdict = self.__rest_client.post(path, device.as_json())
        finally:
            self.__rest_client.close()

        device = Device.construct_from_jdict(response_jdict)

        return device


    def update(self, org_id, device_id, device):
        path = '/v1/orgs/' + org_id + '/devices/' + device_id

        # request...
        self.__rest_client.connect()

        try:
            self.__rest_client.put(path, device.as_json())
        finally:
            self.__rest_client.close()


    def delete(self, user_id, client_id):
        path = '/v1/users/' + user_id + '/devices/' + client_id

        # request...
        self.__rest_client.connect()

        try:
            self.__rest_client.delete(path)
        finally:
            self.__rest_client.close()


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "DeviceManager:{rest_client:%s}" % self.__rest_client
