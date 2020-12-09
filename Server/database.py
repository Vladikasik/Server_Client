import json
import pandas as pd


class Database:

    def __init__(self):
        self.filename = 'Server/persistance-users.json'

    def write_new_id(self, user_id, pubkey):
        users = self.get_users()  # loading users from database
        users_df = pd.DataFrame(users)  # dataframe of user from database (to be faster than for loop)
        df_users_ids = list(users_df["Id"])  # list of users ids to find if id already exists

        new_user_set = {"Id": user_id, "PubKey": pubkey}  # dict to add in  df

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
            print(ex)
            data_to_send = []
            return data_to_send

    # writing data to database
    # TODO: Change json to SQL
    def write_users(self, data):
        with open(self.filename, 'w') as file:
            file.write(json.dumps(data))
