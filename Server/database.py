import json
import pandas as pd


class Database:

    def __init__(self):
        self.filename = 'Server/persistance-users.json'

    def write_new_id(self, user_id, pubkey, server_pubkey, server_priv_key):
        users = self.get_users()  # loading users from database
        users_df = pd.DataFrame(users)  # dataframe of user from database (to be faster than for loop)
        df_users_ids = list(users_df["Id"])  # list of users ids to find if id already exists

        server_pubkey, server_priv_key = self.get_str_keys(server_pubkey, server_priv_key)  # rsa keys to str

        new_user_set = {"Id": user_id, "PubKey": pubkey, "ServerPubKey": server_pubkey, "ServerPrivKey": server_priv_key}  # dict to add in  df

        # check if user already exists
        if user_id in df_users_ids:
            print("user exists")
            # raw from dataframe with exists user values
            df_wrong_user_dict = users_df[users_df["Id"] == user_id].to_dict(orient="Records")[0]
            new_df = users_df.replace(df_wrong_user_dict,
                                      new_user_set)  # replacing exists user with new PubKey
        else:
            print('new user')
            new_df = users_df.append(new_user_set, ignore_index=True)  # adding new user to df

        to_write = new_df.to_dict(orient='records')  # converting to json
        self.write_users(to_write)

    # getting data from database
    # TODO: Change json to SQL
    def get_users(self):
        try:
            with open(self.filename, 'r') as file:
                data_to_send = json.load(file)
            return data_to_send
        except Exception as ex:
            print("Error in opening db")
            print(ex)
            data_to_send = []
            return data_to_send

    # writing data to database
    # TODO: Change json to SQL
    def write_users(self, data):
        with open(self.filename, 'w') as file:
            file.write(json.dumps(data, indent=4))

    # converting rsa keys to str by pkcs1 algrythm?
    def get_str_keys(self, pub, priv):
        pub = pub.save_pkcs1().decode()
        priv = priv.save_pkcs1().decode()
        return pub, priv

    # if user exists check
    def user_exists(self, data):
        user_id = data["Message"]["Id"]
        users = self.get_users()  # loading users from database
        users_df = pd.DataFrame(users)  # dataframe of user from database (to be faster than for loop)
        df_users_ids = list(users_df["Id"])  # list of users ids to find if id already exists

        # check if user already exists
        if user_id in df_users_ids:
            return 1
        else:
            return 0
