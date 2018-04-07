from db import card

'''
find card profile by id
{cid}: str
rtype: dict: {
    'cardId': 'c123',
    'name': 'dark flame master',
    'atk': 10,
    'cost': 3,
    'property': 'dark',
    'growth': ['marshal'],
    'effect': 'It can fool rival, emmm...'
    'description': 'a monster in anime Chuunibyou Demo Koi Ga Shitai.'
}
'''
def find_card_by_id(cid):
    pass

'''
add a new card
{card}: dict: {
    'name': 'Blue-Eyes White Dragon',
    'atk': 3000,
    'cost': 8,
    'property': 'light',
    'growth': ['marshal'],
    'effect': 'Nothing',
    'description': 'This legendary dragon is a powerful engine of destruction.
                   'Virtually invincible, very few have faced this awesome
                   'creature and lived to tell the tale.'

}
rtype: str: cardId
'''
def add_card(card):
    pass
