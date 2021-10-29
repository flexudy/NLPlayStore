from typing import List
from store.service.service import Service
from store.meta.service_registration import ServiceRegistrar
from store.meta.service_types import ServiceType
import logging

logger = logging.getLogger(__name__)


class ServiceManager:

    def __init__(self):
        self.__service_names = list(ServiceRegistrar.SERVICES.keys())

        self.__service_types = [str(service_type.value) for service_type in ServiceType]

    def get_service_names(self) -> List[str]:
        return self.__service_names.copy()

    def get_service(self, service_name: str) -> Service:
        if service_name not in self.__service_names:
            raise Exception("Service: " + service_name + " is unknown.")

        return ServiceRegistrar.SERVICES[service_name]["class"]

    def get_types_of_services(self) -> List[str]:
        return self.__service_types.copy()
