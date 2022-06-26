from setuptools import setup, find_packages


setup(
    name             = 'MailChimp Data Extractor by folderID',
    version          = '0.0.1',
    description      = 'You can extract MailChimp data only by folder ID',
    long_description = open('README.md').read(),
    author           = 'Eunbin Park',
    author_email     = 'parkeb417@gmail.com',
    install_requires = ['requests'],
    packages         = find_packages(exclude = ['docs', 'example']),
    keywords         = ['bot', 'study', 'api'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3.6',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
    python_requires='>=3.6'
)