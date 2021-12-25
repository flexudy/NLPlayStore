from store.service.language_detection.langdetect.langdetect_language_detection_service import \
    Service as Langdetect
from store.service.language_detection.fasttext.fasttext_language_detection_service import Service as FasttextDetector
from store.service.text_generation.cheapity3.cheapity3_text_generation_service import Service as Cheapity3TextGenerator


class ServiceRegistrar:
    SERVICES = {
        Langdetect.get_name(): {
            "type": Langdetect.get_type(),
            "class": Langdetect},
        FasttextDetector.get_name(): {
            "type": FasttextDetector.get_type(),
            "class": FasttextDetector},
        Cheapity3TextGenerator.get_name(): {
            "type": Cheapity3TextGenerator.get_type(),
            "class": Cheapity3TextGenerator
        }
    }
