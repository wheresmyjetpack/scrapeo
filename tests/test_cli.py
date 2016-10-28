import unittest
from unittest.mock import Mock, patch

from scrapeo.CLI import CLI
from scrapeo.core import Scrapeo

class CLITest(unittest.TestCase):

    def setUp(self):
        pass

    def test_sends_search_params_to_find_tag(self):
        mock_args = Mock(metatag_attr='name', metatag_val='description', command='meta', seo_attr=None)
        cli = CLI(mock_args, dom_interface=Scrapeo(''))
        with patch.object(Scrapeo, 'find_tag') as mock_find_tag:
            cli.dispatch_commands()
            mock_find_tag.assert_called_with('meta', name='description')

    def test_sends_shortcut_search_params_to_find_tag(self):
        mock_args = Mock(metatag_attr=None, metatag_val=None, command='meta', seo_attr=None, title_tag=True)
        cli = CLI(mock_args, dom_interface=Scrapeo(''))
        with patch.object(Scrapeo, 'find_tag') as mock_find_tag:
            cli.dispatch_commands()
            mock_find_tag.assert_called_with('title')
