import datetime
import json

import bs4


class JSONEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('indent', None)
        kwargs.setdefault('separators', (',', ':'))
        kwargs.setdefault('sort_keys', True)
        super(JSONEncoder, self).__init__(*args, **kwargs)

    def default(self, obj):
        try:
            obj = obj.datetime()
        except:
            pass

        if isinstance(obj, datetime.datetime):
            return obj.isoformat()

        return super(JSONEncoder, self).default(obj)


def dump_json(objects, stream):
    json.dump(sorted(objects, key=lambda elm: elm['metadata']['date']),
              stream, cls=JSONEncoder)


def write_confluence_row(when, message, source, stream):
    local_time = when.datetime(to_timezone='US/Eastern')
    stream.write('| {when} | {message} | {source} |\n'.format(
        when=local_time.strftime('%b-%d %H:%M:%S'),
        message=html_to_confluence(message),
        source=html_to_confluence(source)))


def html_to_confluence(s):
    soup = bs4.BeautifulSoup(s, 'html.parser')
    for anchor in soup.find_all('a'):
        anchor.replace_with('[{}|{}]'.format(anchor.string, anchor['href']))
    return soup.text
