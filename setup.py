from setuptools import setup, find_packages

setup(
    name="selenium_browser",
    version="v0.1.0",
    author="Eren Mustafa Özdal",
    author_email="eren.060737@gmail.com",
    packages=find_packages(),
    install_requires=["selenium>>=4.18.1", "webdriver-manager>=4.0.1"],
)
