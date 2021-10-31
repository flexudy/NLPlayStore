from store.service.language_detection.langdetect.langdetect_language_detection_service import \
    Service as Langdetect
from store.service.language_detection.fasttext.fasttext_language_detection_service import Service as FasttextDetector


class ServiceRegistrar:
    SERVICES = {
        Langdetect.get_name(): {"type": Langdetect.get_type(),
                                "class": Langdetect},
        FasttextDetector.get_name(): {"type": FasttextDetector.get_type(),
                                      "class": FasttextDetector},
    }
