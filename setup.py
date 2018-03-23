import os
import re

from setuptools import find_packages, setup

with open('./xauth/__init__.py') as f:
    exec(re.search(r'VERSION = .*', f.read(), re.DOTALL).group())

setup(
    name='django-ajax-auth',
    version=__version__,
    author='Luke Hodkinson',
    author_email='luke.hodkinson@uptickhq.com',
    maintainer='Uptick',
    maintainer_email='dev@uptickhq.com',
    url='https://github.com/uptick/django-xauth',
    description='A simple Django application for AJAX authorisation.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['*.txt', '*.js', '*.html', '*.*']},
    install_requires=['setuptools'],
    zip_safe=False,
)
