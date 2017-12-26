"""
Main module of the click demo program
"""
import getpass
import os
import click


class Configuration(object):
    """
    Class provides configuration parameters to all commands and sub commands
    """

    def __init__(self):
        self.username = getpass.getuser()
        self.email = getpass.getuser()+'@localhost'


pass_configuration = click.make_pass_decorator(Configuration, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'commands'))


class ComplexCLI(click.MultiCommand):
    """
    Class is responsible for the discovery of the available command/ python
    files in the commands folder
    """

    def list_commands(self, cfg):
        """
        This method checks if the Python files in the command folder are loadable
        and adds them to the set of available commands
        """
        commandset = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and '__init__' not in filename:
                commandset.append(filename[:-3])
        commandset.sort()
        return commandset

    def get_command(self, cfg, name):
        """
        This method tries to load the module via the specified name

        :param cfg: Instance of Configuration
        :type cfg: Configuration
        :param name: Name of the command
        :type name: str
        :return: function object
        """
        try:
            mod = __import__('greeter.commands.' + name, None, None, ['cli'])
        except ImportError:
            return
        return mod.cli


@click.command(cls=ComplexCLI)
def cli():
    """
    This application shows the usage of the click framework for complex CLI applications
    """
    pass
