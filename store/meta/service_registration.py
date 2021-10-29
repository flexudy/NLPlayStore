from store.service.language_detection.langdetect.langdetect_language_detection_service import \
    Service as Langdetect


class ServiceRegistrar:
    SERVICES = {
        Langdetect.get_name(): {"type": Langdetect.get_type(),
                                "class": Langdetect},
    }
