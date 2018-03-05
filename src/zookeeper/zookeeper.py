from kazoo.client import KazooClient
from kazoo.client import KazooState

def my_listener(state):
    pass


zk = KazooClient()
zk.start()
zk.add_listener(my_listener)

all_znodes = zk.get_children('/')
for zn in all_znodes:
    print(zk.get('/' + zn))

zk.ensure_path('one/two')

zk.create('one/two/key', b'value1')

zk.exists('one/two/key')

zk.set('one/two/key', b'value2')

zk.delete('one/two/key', recurvise=True)
