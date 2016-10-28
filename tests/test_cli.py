import unittest
from unittest.mock import Mock, patch

from scrapeo.CLI import CLI
from scrapeo.core import Scrapeo

class CLITest(unittest.TestCase):

    def setUp(self):
        pass

    def test_sends_find_tag_to_dom_interface(self):
        mock_args = Mock()
        mock_args.metatag_attr = 'name'
        mock_args.metatag_val = 'description'
        mock_args.command = 'meta'
        mock_args.seo_attr = None
        cli = CLI(mock_args, dom_interface=Scrapeo(''))
        with patch.object(Scrapeo, 'find_tag') as mock_find_tag:
            cli.dispatch_commands()
            mock_find_tag.assert_called_with('meta', name='description')

