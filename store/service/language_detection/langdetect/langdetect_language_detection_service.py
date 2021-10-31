from store.service.service import Service as ServiceInterface
from store.meta.service_types import ServiceType
from typing import List
import gradio as gr
import os


class Service(ServiceInterface):
    __NAME = "langdetect"

    __AUTHORS = ["Michal Mimino Danilak"]

    __DESCRIPTION = "Port of Nakatani Shuyo's language-detection library (version from 03/03/2014) to Python."

    __SUPPORTED_LANGUAGES = ["af", "ar", "bg", "bn", "ca", "cs", "cy", "da", "de", "el", "en", "es", "et", "fa", "fi",
                             "fr", "gu", "he", "hi", "hr", "hu", "id", "it", "ja", "kn", "ko", "lt", "lv", "mk", "ml",
                             "mr", "ne", "nl", "no", "pa", "pl", "pt", "ro", "ru", "sk", "sl", "so", "sq", "sv", "sw",
                             "ta", "te", "th", "tl", "tr", "uk", "ur", "vi", "zh-cn", "zh-tw"]

    __EXAMPLE = "Input Text: 'The goat is on the tree.'\n" \
                "Output Language: 'en'"

    def play(self, text: str) -> str:
        from langdetect import detect

        return detect(text)

    def play_on_screen(self) -> None:
        interface = gr.Interface(fn=self.play, inputs="text", outputs="text")

        interface.launch()

    @staticmethod
    def get_name() -> str:
        return Service.__NAME

    @staticmethod
    def get_authors() -> List[str]:
        return Service.__AUTHORS

    @staticmethod
    def get_description() -> str:
        return Service.__DESCRIPTION

    @staticmethod
    def get_type() -> ServiceType:
        return ServiceType.LANGUAGE_DETECTION

    @staticmethod
    def get_supported_languages() -> List[str]:
        return Service.__SUPPORTED_LANGUAGES

    @staticmethod
    def get_example() -> str:
        return Service.__EXAMPLE

    @staticmethod
    def install() -> None:
        requirements_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")

        os.system("pip3 install -r {}".format(requirements_file_path))

    @staticmethod
    def launch():
        return Service()

    @staticmethod
    def uninstall() -> None:
        os.system("pip3 uninstall langdetect")
