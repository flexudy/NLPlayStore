from store.service.service import Service as ServiceInterface
from store.meta.service_types import ServiceType
from typing import List
import gradio as gr
import os


class Service(ServiceInterface):
    __NAME = "Flexudy-Fasttext-Language-Detector"

    __AUTHORS = ["Flexudy Education"]

    __DESCRIPTION = "A service that uses Fasttext to identify a text's language based on Fasttext by Facebook."

    __SUPPORTED_LANGUAGES = ['af', 'als', 'am', 'an', 'ar', 'arz', 'as', 'ast', 'av', 'az', 'azb', 'ba', 'bar', 'bcl',
                             'be', 'bg', 'bh', 'bn', 'bo', 'bpy', 'br', 'bs', 'bxr', 'ca', 'cbk', 'ce', 'ceb', 'ckb',
                             'co', 'cs', 'cv', 'cy', 'da', 'de', 'diq', 'dsb', 'dty', 'dv', 'el', 'eml', 'en', 'eo',
                             'es', 'et', 'eu', 'fa', 'fi', 'fr', 'frr', 'fy', 'ga', 'gd', 'gl', 'gn', 'gom', 'gu', 'gv',
                             'he', 'hi', 'hif', 'hr', 'hsb', 'ht', 'hu', 'hy', 'ia', 'id', 'ie', 'ilo', 'io', 'is',
                             'it', 'ja', 'jbo', 'jv', 'ka', 'kk', 'km', 'kn', 'ko', 'krc', 'ku', 'kv', 'kw', 'ky', 'la',
                             'lb', 'lez', 'li', 'lmo', 'lo', 'lrc', 'lt', 'lv', 'mai', 'mg', 'mhr', 'min', 'mk', 'ml',
                             'mn', 'mr', 'mrj', 'ms', 'mt', 'mwl', 'my', 'myv', 'mzn', 'nah', 'nap', 'nds', 'ne', 'new',
                             'nl', 'nn', 'no', 'oc', 'or', 'os', 'pa', 'pam', 'pfl', 'pl', 'pms', 'pnb', 'ps', 'pt',
                             'qu', 'rm', 'ro', 'ru', 'rue', 'sa', 'sah', 'sc', 'scn', 'sco', 'sd', 'sh', 'si', 'sk',
                             'sl', 'so', 'sq', 'sr', 'su', 'sv', 'sw', 'ta', 'te', 'tg', 'th', 'tk', 'tl', 'tr', 'tt',
                             'tyv', 'ug', 'uk', 'ur', 'uz', 'vec', 'vep', 'vi', 'vls', 'vo', 'wa', 'war', 'wuu', 'xal',
                             'xmf', 'yi', 'yo', 'yue', 'zh']

    __EXAMPLE = "Input Text: 'The goat is on the tree.'\n" \
                "Output Language: 'en'"

    def __init__(self):
        from flexudy_language_detector.start import FlexudyLanguageDetectorFactory

        self.__language_detector = FlexudyLanguageDetectorFactory.get_flexudy_language_detector()

    def play(self, text: str) -> str:
        language = self.__language_detector.get_language(text)

        return language

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
        os.system("pip3 uninstall flexudy_language_detector")
