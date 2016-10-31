import unittest
from unittest.mock import Mock, patch

from scrapeo.CLI import CLI
from scrapeo.core import Scrapeo

class CLITest(unittest.TestCase):

    def setUp(self):
        pass

    def test_sends_search_params_to_find_tag(self):
        mock_args = Mock()
        cli = CLI(mock_args, dom_interface=Scrapeo(''))
        with patch.object(Scrapeo, 'find_tag') as mock_find_tag:
            cli.searches.append(['meta', {'name': 'description'}])
            for query in cli.searches:
                cli.run_search(query)
            mock_find_tag.assert_called_with('meta', name='description')

    def test_sends_shortcut_search_params_to_find_tag(self):
        mock_args = Mock()
        cli = CLI(mock_args, dom_interface=Scrapeo(''))
        with patch.object(Scrapeo, 'find_tag') as mock_find_tag:
            cli.searches.append(['title', {}])
            for query in cli.searches:
                cli.run_search(query)
            mock_find_tag.assert_called_with('title')
