from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks, Deferred


def sleep(secs):
    d = Deferred()
    reactor.callLater(secs, d.callback, None)
    return d


@inlineCallbacks
def hello():
    yield sleep(3)
    print('Hello!')
    reactor.stop()


if __name__ == '__main__':
    reactor.callWhenRunning(hello)
    reactor.run()