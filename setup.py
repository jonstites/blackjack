try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A stupid blackjack game',
    'author': 'Jonathan Stites',
    'author_email': 'contact@jonstites.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': [],
    'scripts': [],
    'name': 'blackjack'
}

setup(**config)