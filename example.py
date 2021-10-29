from store.service_management import ServiceManager

input_text = "Hello, this is NLPlay. Your favorite store on Github."

service_manager = ServiceManager()

services_available = service_manager.get_service_names()

language_detector = service_manager.get_service(services_available[0])

language_detector.install()

language_detector = language_detector.launch()

print(language_detector.play(input_text))

language_detector.uninstall()
