class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity=capacity
        self.queue=[]
        self.cache={}

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        else:
            return -1
        # Retrieve item from provided key. Return -1 if nonexistent. 

    def set(self, key, value):
        if len(self.cache)==0:
            self.cache[key]=value
            self.queue.append(key)
        elif len(self.cache) <= self.capacity:
            self.queue.append(key)
            self.cache[key]=value
        else:
            to_delete=self.queue.pop(0)
            del self.cache[to_delete]
            self.cache[key]=value


our_cache = LRU_Cache(5)
our_cache2 = LRU_Cache(4)
our_cache3 = LRU_Cache(3)
our_cache4 = LRU_Cache(2)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

our_cache2.set(1, 1)
our_cache2.set(2, 2)
our_cache2.set(3, 3)
our_cache2.set(4, 4)


our_cache3.set(1, 1)
our_cache3.set(2, 2)
our_cache3.set(3, 3)
our_cache3.set(4, 4)

our_cache4.set(1, 1)
our_cache4.set(2, 2)
our_cache4.set(3, 3)
our_cache4.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache


print(our_cache2.get(1))       # returns 1
print(our_cache2.get(2))       # returns 2
print(our_cache2.get(9))      # returns -1 because 9 is not present in the cache


print(our_cache3.get(1))       # returns 1
print(our_cache3.get(2))       # returns 2
print(our_cache3.get(9))      # returns -1 because 9 is not present in the cache


print(our_cache4.get(1))       # returns 1
print(our_cache4.get(2))       # returns 2
print(our_cache4.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      