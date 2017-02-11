import datetime
import json


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


def dump(objects, stream):
    json.dump(sorted(objects, key=lambda elm: elm['metadata']['date']),
              stream, cls=JSONEncoder)
