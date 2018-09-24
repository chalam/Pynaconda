from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return '%s %d' % (self.name, self.score)

    def comparator(a, b):
        print('cmp', a.name, b.name, a.name < b.name)
        if a.score < b.score:
            return 1
        if a.score > b.score:
            return -1
        if a.name < b.name:
            return -1
        if a.name > b.name:
            return 1
        return 0

data = []
inputs = """amy 100
david 100
aakansha 75
heraldo 70
heraldo 50
aleksa 150"""
# n = int(inputs[0].rstrip())
for line in inputs.split('\n'):
    name, score = line.split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

print('unsorted', data)
data_sorted = sorted(data, key=cmp_to_key(Player.comparator))
for i in data_sorted:
    print(i.name, i.score)
data_sorted = sorted(data, key=lambda x: x.name )
for i in data_sorted:
    print(i.name, i.score)