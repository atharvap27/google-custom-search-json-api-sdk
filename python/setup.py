from setuptools import setup, find_packages

setup(
    name='google_custom_search_sdk',
    version='1.0.0',
    description='Python SDK for Google Custom Search JSON API',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pydantic'
    ],
    python_requires='>=3.6',
    include_package_data=True
)
