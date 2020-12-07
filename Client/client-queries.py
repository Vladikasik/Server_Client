import json

def msg(type, data):

    if type == 'PubKey':
        try:
            query = {"Type": "PubKey",
                    "Message": {"PubKey": data[0],
                                "Id": data[0]
                                }
                    }
            to_send = json.dumps(query)
        except Exception as ex:
            to_send  = str(ex)
        finally:
            return to_send
