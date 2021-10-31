from distutils.core import setup
import setuptools

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name="NLPlayStore",
    version="0.0.2",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
        "store.service.language_detection.langdetect": ["requirements.txt"],
        "store.service.language_detection.fasttext": ["requirements.txt"],
    },
    url="https://flexudy.com",
    license="Apache-2.0 License",
    author="Flexudy Education",
    author_email="support@flexudy.com",
    description="Install, use and uninstall Machine Learning models, functions and more.",
    install_requires=REQUIREMENTS,
)
