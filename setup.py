from setuptools import setup

setup(
    name='hive-django-storage-swift',
    version='1.2.11',
    description='OpenStack Swift storage backend for Django',
    long_description=open('README.rst').read(),
    url='http://github.com/nilliams/django-storage-swift',
    author='Dennis Vermeulen',
    author_email='blacktorn@gmail.com',
    license='MIT',
    packages=['swift'],
    install_requires=[
        'python-swiftclient>=1.4.0',
        'python-keystoneclient>=0.2.3',
        'six',
        'python-magic>=0.4.10',
    ],
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
)
