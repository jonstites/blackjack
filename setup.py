#!/usr/bin/env python3
from distutils.core import setup

setup(name= 'blackjack',
    description= 'A stupid blackjack game',
    author= 'Jonathan Stites',
    author_email= 'contact@jonstites.com.',
    version= '0.1',
    install_requires= ['pytest'],
    packages= ['blackjack'],
    url='https://github.com/jonstites/blackjack',
    scripts= ['bin/play_blackjack.py'],
)
