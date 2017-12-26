"""
Module contains some simple unit tests for the CLI command 'whoami'
"""

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from unittest import TestCase
from click.testing import CliRunner
from greeter.greeter import cli


class WhoAmITest(TestCase):
    """
    Test class for the whoami command
    """

    def test_cli_normal_call(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['whoami'])
        self.assertEqual(result.exit_code, 0)

    def test_cli_with_mail(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['whoami','-e'])
        self.assertEqual(result.exit_code, 0)

    def test_cli_with_invalid_parameter(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['whoami','-x'])
        self.assertNotEqual(result.exit_code, 0)