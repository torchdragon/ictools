import unittest

import ictools.io as icio


class IOTests(unittest.TestCase):

    # Test to ensure that a raw URL is wrapped in hard braces to prevent issues with Confluence importing.
    def test_html_to_confluence_wraps_raw_urls_with_hard_braces(self):
        expected_input = 'Bob Builder: https://arbitrary.website.com/path?param=1&otherParam&thirdParam=foo&here=now'
        expected_output = 'Bob Builder: [https://arbitrary.website.com/path?param=1&otherParam;&thirdParam;=foo&here;=now]'

        output = icio.html_to_confluence(expected_input)

        self.assertEquals(expected_output, output)

    # Test that an already wrapped URL in braces is not re-wrapped in braces.
    def test_html_to_confluence_does_not_double_wrap_raw_urls_with_hard_braces(self):
        expected_input = 'Bob Builder: [https://arbitrary.website.com/path?param=1&otherParam&thirdParam=foo&here=now]'
        expected_output = 'Bob Builder: [https://arbitrary.website.com/path?param=1&otherParam;&thirdParam;=foo&here;=now]'

        output = icio.html_to_confluence(expected_input)

        self.assertEquals(expected_output, output)

    # Test that an <a> tagged url is only wrapped correctly on the outside.
    def test_html_to_confluence_does_not_wrap_a_tags_with_hard_braces(self):
        expected_input = 'Bob Builder: <a href="https://arbitrary.website.com/path?param=1&otherParam&thirdParam=foo&here=now">Website Link</a>'
        expected_output = 'Bob Builder: [Website Link|https://arbitrary.website.com/path?param=1&otherParam&thirdParam=foo&here=now]'

        output = icio.html_to_confluence(expected_input)

        self.assertEquals(expected_output, output)
