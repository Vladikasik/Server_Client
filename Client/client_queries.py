import json


def msg(query_type, data):
    if query_type == 'PubKey':
        try:
            query = {"Type": "PubKey",
                     "Message": {"PubKey": data[0],
                                 "Id": data[1]
                                 }
                     }
            to_send = json.dumps(query)
            to_send = to_send.encode()
            return to_send
        except Exception as ex:
            to_send = str(ex).encode()
            return to_send
