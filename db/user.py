from db import user

'''
find user profile by id
{uid}: str
rtype: dict: {
    'userId': 'u123',
    'name': 'aryon',
    'win': 10,
    'all': 20,
    'staged': [['c123', 'c234'], ['c345', 'c456']],
    'pool': [['c123', 'c234'], ['c345', 'c456']]
}
'''
def find_user_by_id(uid):
    pass

def win_user_by_id(uid):
    pass

def lose_user_by_id(uid):
    pass

'''
update user's staged cards
{uid}: str
{staged}: list[list[str]]
rtype: bool
'''
def update_user_staged_by_id(uid, staged):
    pass

'''
add a new user
{user}: dict: {
    'userId': 'u123',
    'name': 'aryon',
}
rtype: bool
'''
def add_user(user):
    pass
