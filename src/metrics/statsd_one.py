import statsd

c = statsd.StatsClient('localhost', 8125)
c.incr('foo_counter')
c.timing('foo_timer', 320) #320ms
with c.timer('foo_timer2'):
    for i in range(100):
        i ** 2

c.gauge('foo_gauge', 70) # set gauge to 70
c.gauge('foo_gauge', 1, delta=True) # now at 71
c.gauge('foo_gauge', -3, delta=True) # now at 68