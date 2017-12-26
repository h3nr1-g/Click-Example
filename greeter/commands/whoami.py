"""
This module contains the implementation of the command 'whoami'
"""

import click
from greeter.greeter import pass_configuration


@click.command('whoami', help='Shows who you are')
@click.option('--e-mail','-e', is_flag=True, help='If set show e-mail address of the user')
@pass_configuration
def cli(cfg, e_mail):
    """
    Command shows who you are
    """
    print(cfg.username)
    if e_mail:
        print(cfg.email)