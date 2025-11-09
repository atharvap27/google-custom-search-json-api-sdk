from setuptools import setup, find_packages

setup(
    name='google-customsearch-sdk',
    version='2.0.0',
    description='Python SDK for Google Custom Search JSON API (v2)',
    author='Google & SDK Bot',
    author_email='',
    url='https://github.com/googleapis/google-customsearch-sdk',
    packages=find_packages(),
    install_requires=[
        'requests>=2.23.0'
    ],
    python_requires='>=3.6',
    license='Apache-2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
    ],
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
)
