import consul

c = consul.Consul() #host
c.kv.put('key1', 'value1')
index, data = c.kv.get('key1')
print(index, data)

#update
c.kv.put('key1', 'value2')
#delete
c.kv.delete('key1')