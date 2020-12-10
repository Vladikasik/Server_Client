import json
import rsa


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
            print("Error in creating message")
            print(ex)
    elif query_type == 'Message':
        try:
            encrypted_data = rsa.encrypt(data[1].encode('utf-8'), data[2])
            # print(str(encrypted_data))
            query = {"Type": "Message",
                     "Message": {"Id": data[0],
                                 "Data": encrypted_data
                                 }
                     }
            to_send = json.dumps(query)
            to_send = to_send.encode()
            return to_send
        except Exception as ex:
            print("Error in creating message")
            print(ex)
        except Exception as ex:
            to_send = str(ex).encode()
            return to_send
