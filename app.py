from healthchecks.services.users import UserService

handler = UserService()
handler.create_service_url()
print(handler.process_services(handler.services))