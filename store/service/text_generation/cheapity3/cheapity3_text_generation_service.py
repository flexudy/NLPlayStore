import os
from typing import List

import gradio as gr

from store.meta.service_types import ServiceType
from store.service.service import Service as ServiceInterface


class Service(ServiceInterface):
    __NAME = "cheapity3"

    __AUTHORS = ["Flexudy Education"]

    __DESCRIPTION = "A GPT3-like text generation library"

    __SUPPORTED_LANGUAGES = ["en", "fr", "de"]

    __EXAMPLE = (
        "@param: text: The input text, e.g 'Philosophy is the science of'"
        "\n@param: num_words_to_generate: The number of words to generate e.g 10\n"
        "@return: List of generated texts e.g ['.. the mind that provides a guide not only of ideas from other disciplines but also of human thought.', '..']"
    )

    def __init__(self):
        from cheapity3.start import TextGeneratorFactory

        self.__text_generator = TextGeneratorFactory.get_text_generator()

    def play(self, text: str, num_words_to_generate: int) -> List[str]:
        generated_texts = self.__text_generator.generate_text(
            text, num_words_to_generate=num_words_to_generate
        )

        return generated_texts

    def play_to_string(self, text: str, num_words_to_generate: float) -> str:
        generated_texts = self.play(text, int(num_words_to_generate))

        outputs = list()

        for generated_text in generated_texts:
            outputs.append(text + " " + generated_text)

        return "\n\n".join(outputs)

    def play_on_screen(self) -> None:

        max_words = gr.inputs.Slider(
            minimum=1, maximum=64, default=25, step=1, label="Max number of words"
        )

        interface = gr.Interface(
            fn=self.play_to_string, inputs=["text", max_words], outputs="text"
        )

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
        return ServiceType.TEXT_GENERATION

    @staticmethod
    def get_supported_languages() -> List[str]:
        return Service.__SUPPORTED_LANGUAGES

    @staticmethod
    def get_example() -> str:
        return Service.__EXAMPLE

    @staticmethod
    def install() -> None:
        requirements_file_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "requirements.txt"
        )

        os.system("pip3 install -r {}".format(requirements_file_path))

    @staticmethod
    def launch():
        return Service()

    @staticmethod
    def uninstall() -> None:
        os.system("pip3 uninstall cheapity3")
