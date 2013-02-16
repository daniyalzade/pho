from setuptools import setup

requires = [
        'lxml'
        ]

packages = [
    'pho',
]

setup(
    name='pho',
    author='Eytan Daniyalzade',
    author_email='eytan@stylrapp.com',
    url='http://stylrapp.com',
    packages=packages,
    description='High performance HTML parser built on lxml',
    install_requires=requires,
    version='0.0.1',
    data_files=[
        ('', ['README.rst', 'LICENSE']),
        ],
    package_dir={
        'pho': 'pho'
        },
    package_data={
        'pho': [
            #'*.html',
            #'*.css',
            ],
        },
    include_package_data=True,
)
