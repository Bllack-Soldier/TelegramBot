class Func():
    
    def get_all_usernames(user_dict):
        usernames=[]
        for user_identifier, user_data in user_dict.items():
            usernames.append(user_data["username"])
        return usernames