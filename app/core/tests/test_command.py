"""
test custom Django management commands.
"""

from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.check')
class CommandTests(SimpleTestCase):
    """ test comnmands """


    def test_wait_for_db_ready(self, patched_check):
        """ test waiting for the db be ready """
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(database=['default'])

    def test_wait_for_db_delay(self, parched_check):
        """test waiting for db when getting operationalError"""