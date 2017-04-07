import unittest

import ictools.io as icio


class IOTests(unittest.TestCase):

    # This tests the case where the overly aggressive html parser will convert &<something> into &<something>;, which
    # will in turn confuse the heck out of Confluence's markup parser. Our conversion library should replace the &
    # literal values with the encoded value to prevent the aggressive replacement and maintain link functionality.
    def test_html_to_confluence_does_not_poorly_format_urls_with_ampersand(self):
        expected_input = '| Apr-05 15:35:49 | Bob Builder: https://arbitrary.website.com/path?param=1&otherParam&thirdParam=foo&here=now | #CodeRed |'
        expected_output = '| Apr-05 15:35:49 | Bob Builder: https://arbitrary.website.com/path?param=1%26otherParam%26thirdParam=foo%26here=now | #CodeRed |'

        output = icio.html_to_confluence(expected_input)

        self.assertEquals(expected_output, output)
