from setuptools import setup, find_packages
setup(
    name='google-custom-search-sdk',
    version='1.0.0',
    description='Python SDK for Google Custom Search JSON API',
    author='',
    author_email='',
    packages=find_packages(),
    install_requires=[
        'requests>=2.20.0'
    ],
    python_requires='>=3.6',
    include_package_data=True,
)
