from store.service_management import ServiceManager

input_text = "Hello, this is NLPlay. Your favorite store on Github."

service_manager = ServiceManager()

# Get a list of all services available
services_available = service_manager.get_service_names()

language_detector = service_manager.get_service("Flexudy-Fasttext-Language-Detector")

# Feel free to read the description
service_description = language_detector.get_description()

language_detector.install()

language_detector = language_detector.launch()

language_detector.play_on_screen()

# Destroy service you don't need
language_detector.uninstall()
