import requests, urllib.request

class HandleService():
    """Class To Handle Request passed"""
    service = 'https://google.com'
    output = {
        'service':service,
        'message':None
        }

    def check_service(self, service):
        if service is None:
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
