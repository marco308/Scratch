
import numpy as np

zoe = 2
marcus = 2
jack = 4
jess = 4
bob = 2
sid = 2


class player: 
    def __init__(self, name, chukkas_t):
        self.name = name 
        self.chukkas_t = chukkas_t
        self.chukkas_left = chukkas_t
        self.ckukka_list = []


def get_next_player(players):
    next_player = players[0]
    for  player in players:
        if player.chukkas_left > next_player.chukkas_left:
            next_player = player
        return next_player

def get_av_player(players):
    av_players = []
    for player in players:
        if player.chukkas_left > 0:
            av_players.append(player)
    return av_players

def order_players(players):
    

# players
zoe = player('zoe', 1)
marcus = player('marcus', 2)
bob = player('bob', 3)
jaz = player('jaz', 4)

players = [zoe, marcus, bob, jaz]

# team size 
team_size = 2



print(zoe.chukkas_left)




t = get_next_player(players)

print(t.name)