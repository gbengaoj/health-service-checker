import os
import requests, urllib.request, json
import datetime

class HandleService():
    """Class To Handle Request passed"""

    service = None

    uptime = None # Uptime For Microservice Availability 
    downtime = None # Downtime For Microservice Not Available
    output = {
        'service': service,
        'message': None,
        'uptime': uptime,
        'downtime': downtime
        }

    def check_service(self, service):
        if self.service is None:
            self.output['message'] = 'Please Provide Service!'
            return self.output
        else:
            self.check_service_status(service)
            return self.output


    def check_service_status(self, service):
        return_bool = None
        res = requests.get(service) # get the respond code
        res_code = res.status_code # respond code from service check
        if res_code == 200:
            # Request Response is OK
            self.output['message'] = "This Service is Available and Working Fine"
        elif res_code == 404:
            self.output['message'] = "This Service is Not Found! - Does Not Exist!"
        return return_bool

    def calculate_uptime(self):
        pass

    def calculate_downtime(self):
        pass
