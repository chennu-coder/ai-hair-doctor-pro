memory = {}

def save_user(user_id, data):
    memory[user_id] = data

def get_user(user_id):
    return memory.get(user_id, {})