from enum import Enum, auto


class ServiceType(Enum):
    LANGUAGE_DETECTION = (auto(),)
    TEXT_GENERATION = (auto(),)

    @staticmethod
    def from_str(service_type):

        if service_type is None:
            raise Exception("Pass a string as argument. Not a 'None' value.")

        if ServiceType.LANGUAGE_DETECTION.name == service_type:

            return ServiceType.LANGUAGE_DETECTION

        if ServiceType.TEXT_GENERATION.name == service_type:
            return ServiceType.TEXT_GENERATION

        else:
            raise ValueError("The type {} is unknown".format(service_type))
