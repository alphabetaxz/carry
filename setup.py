from setuptools import setup, find_packages

import carry

# http://setuptools.readthedocs.io/en/latest/setuptools.html
setup(
    name='carry',

    version=carry.__version__,

    description='Carry is an utility ETL(extract-transform-load) tool',
    long_description='',

    url='https://github.com/toaco/carry',

    author='Jeffrey',
    author_email='Jeffrey.S.Teo@gmail.com',

    license='GPL-3.0',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Operating System :: OS Independent',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    platforms='any',

    keywords=['ETL', 'extract-transform-load', 'utility'],

    packages=find_packages(exclude=['test*']),

    install_requires=['tqdm', 'pandas', 'sqlalchemy'],

    python_requires='==2.7.*',
)
