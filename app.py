from controller.healthservicehandler import HandleService

handler = HandleService()

handler.service = "https://google.com"

print(handler.check_service(handler.service))