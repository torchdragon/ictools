import datetime
import json
import logging
import re
import sys

import bs4

from ictools import cli


TIME_FORMAT = '%b-%d %H:%M:%S'
_TIME_PATTERN = r'...-\d\d \d\d:\d\d:\d\d'


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
        when=local_time.strftime(TIME_FORMAT),
        message=html_to_confluence(message),
        source=html_to_confluence(source)))


def html_to_confluence(s):
    url_re = re.compile(r'(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))', re.S)
    encoded_string = url_re.sub(lambda m: m.group().replace('&', '%26'), s)

    soup = bs4.BeautifulSoup(encoded_string, 'html.parser')
    for anchor in soup.find_all('a'):
        anchor.replace_with('[{}|{}]'.format(anchor.string, anchor['href']))
    return soup.text


def combine_tables():
    cli.configure_logging()
    logger = logging.getLogger('combine_tables')

    patn = re.compile(r'\| (?P<timestamp>' + _TIME_PATTERN + r') \|')
    lines = []
    for line in sys.stdin:
        m = patn.match(line)
        if not m:
            logger.error('failed to parse "%s"', line)
            continue
        timestamp = datetime.datetime.strptime(m.groupdict()['timestamp'],
                                               TIME_FORMAT)
        lines.append((timestamp, line))

    for _, line in sorted(lines):
        sys.stdout.write(line)
