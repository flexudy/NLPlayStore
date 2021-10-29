from distutils.core import setup
import setuptools

setup(
    name='NLPlayStore',
    version='0.0.1',
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={'store.service.language_detection.langdetect': ['requirements.txt']},
    url='https://flexudy.com',
    license='Apache-2.0 License',
    author='Flexudy Education',
    author_email='support@flexudy.com',
    description='Install, use and uninstall Machine Learning models, functions and more.'
)
