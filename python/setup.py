from setuptools import setup, find_packages

setup(
    name='google-custom-search',
    version='1.0.0',
    description='Python SDK for Google Custom Search JSON API',
    author='OpenAI',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    python_requires='>=3.6',
    url='https://www.googleapis.com/customsearch/v1'
)
