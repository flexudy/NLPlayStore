from enum import Enum, auto


class ServiceType(Enum):
    LANGUAGE_DETECTION = auto(),

    @staticmethod
    def from_str(service_type):

        if service_type is None:
            raise Exception("Pass a string as argument. Not a 'None' value.")

        if ServiceType.LANGUAGE_DETECTION.name == service_type:

            return ServiceType.LANGUAGE_DETECTION

        else:
            raise ValueError("The type {} is unknown".format(service_type))
