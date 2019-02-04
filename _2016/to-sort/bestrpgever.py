#-*-coding: utf-8 -*-

from pygraph.classes.graph import graph

ROOMS = {
         1: 'Sauna. Someone is layng on the bench. Long black hair... Oh wait it is a man!',
         2: 'Not your hotel room! You are checking out the fridge... empty.',
         3: 'Reception',
         4: 'Some drunk programmers in a lobby',
         5: "Loo (WOMEN's - AAAA! Get out you prevert!)",
         6: "Eagle's nest (Fly Pythonista, Fly)",
         7: 'Dining hall. Smells funny...',
         8: 'Workshop Room',
         9: 'Bar'}

class Labyrinth(object):
    def __init__(self):
        self.passages = graph()
        self.passages.add_nodes([1, 2, 3, 4, 5])
        self.passages.add_nodes([6, 7, 8, 9, 10])
        self.passages.add_edge((1, 2))
        self.passages.add_edge((2, 3))
        self.passages.add_edge((3, 4))
        self.passages.add_edge((4, 5))
        self.passages.add_edge((3, 8))
        self.passages.add_edge((6, 7))
        self.passages.add_edge((7, 8))
        self.passages.add_edge((8, 9))
        self.passages.add_edge((9, 10))
    
    def possible_moves(self, room):
        return self.passages.neighbors(room)
    
    def print_moves(self, moves):
        return 'Exits: \n' + '\n'.join(['%s:' % n + 'Room %s' % n for n in moves])


class GameLoop(object):
    def __init__(self):
        self.lab = Labyrinth()
        self.player = Player('Pythonista')
        self.end = False
        self.dest = 9
        
    def loop(self):
        
        self.player.name = input('What is your name? ')
        print("Good news! You are on PyConPL 2013 in a derelict hotel, 'ORLE GNIAZDO'")
        print("You are at the hotel reception. You need to get to the BAR")
        
        while not self.end:
            print('\nYou are in: %s \n' % ROOMS.get(self.player.room,
                                            'Generic room %s' % (self.player.room,)))
            moves = self.lab.possible_moves(self.player.room)
            try:
                next_move = input(self.lab.print_moves(moves) + '\n')
            except EOFError:
                print("\nBye....")
                break
            except:
                print("\n...What?")
                continue
            try:
                if int(next_move) in moves:
                    self.player.room = int(next_move)
                else:
                    print("\nThis is a wall. You're drunk already.")
                if self.player.room == self.dest:
                    print('YOU WON %s! Now DRINK!' %self.player.name)
                    self.end = True
            except Exception:
                # Errors should never pass silently.
                print("Try harder")
    

class Player(object):    
    def __init__(self, name):
        self.room = 3
        self.health = 100
        self.name = name

if __name__ == '__main__':
    loop = GameLoop()
    loop.loop()

