
"""
This module contains the implementation of the command group 'greeting'
"""

import click
from greeter.greeter import pass_configuration


@click.group('greetings', short_help='Command for greetings')
def cli():
    """
    Command generates a message
    """
    pass


@cli.command('morning', help='Good morning to ...')
@click.option('--name', '-n', default=None, help='Greetings to')
@pass_configuration
def morning(cfg, name):
    message = 'Good morning %s' % (cfg.username if name is None else name)
    print(message)


@cli.command('evening', help='Good evening to ...')
@click.option('--name', '-n', default=None, help='Greetings to')
@pass_configuration
def evening(cfg, name):
    message = 'Good evening %s' % (cfg.username if name is None else name)
    print(message)