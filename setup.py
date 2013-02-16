from distutils.core import setup
import pho

requires = []

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
    long_description=open('README.rst').read(),
    version=pho.__version__,
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
    license=open('LICENSE').read(),
    install_requires=requires,
    include_package_data=True,
)
