from store.service_management import ServiceManager

input_text = "Artificial Thermo-Machine Learning is the study of"

service_manager = ServiceManager()

service = service_manager.get_service("cheapity3")

service.install()

service = service.launch()

service.play_on_screen()

# Destroy service you don't need
service.uninstall()
