from typing import List
from store.meta.service_types import ServiceType


class Service:

    @staticmethod
    def get_name() -> str:
        pass

    @staticmethod
    def get_authors() -> List[str]:
        pass

    @staticmethod
    def get_description() -> str:
        pass

    @staticmethod
    def get_type() -> ServiceType:
        pass

    @staticmethod
    def get_supported_languages() -> List[str]:
        pass

    @staticmethod
    def get_example() -> str:
        pass

    @staticmethod
    def install() -> None:
        pass

    @staticmethod
    def launch():
        return Service()

    @staticmethod
    def uninstall() -> None:
        pass

    def play(self, **kwargs):
        pass

    def play_on_screen(self) -> None:
        pass
