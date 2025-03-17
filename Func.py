import time
class Func():
    
    def get_all_usernames(user_dict):
        usernames=[]
        for user_identifier, user_data in user_dict.items():
            usernames.append(user_data["username"])
        return usernames
    
    def generate_unique_id(user_id):
        return f"{user_id}{int(time.time())}"