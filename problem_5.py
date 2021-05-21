
import hashlib
class Node:
    def __init__(self, timestamp,data,previous_hash):
        self.block = BlockChain(timestamp,data,previous_hash)
        self.next = None        
class BlockChain:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()


    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = "We are going to encode this string of data!".encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

class LinkedList:
    def __init__(self):
        self.head=None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += " TIME STAMP : "+ str(cur_head.block.timestamp) + "\n DATA : "+ str(cur_head.block.data) +"\n PREVIOUS HASH:  "+ str(cur_head.block.previous_hash)+"\n CURRENT HASH: "+str(cur_head.block.hash)+" -> "
            out_string += "\n\n"
            cur_head = cur_head.next
        return out_string

        # self.next=None
        # self.previous=None

    def append(self,timestamp, data):

        if self.head is None:
            self.head = Node(timestamp,data,0)
            return

        node = self.head
        previous_hash = self.head.block.hash
        while node.next:
            node = node.next
        node.next = Node(timestamp,data,previous_hash)


chain=LinkedList()
chain.append("10:20 16/5/2021", "First Data")
chain.append("10:21 16/5/2021", "Second Data")
chain.append("10:22 16/5/2021","Third  Data")
print(chain)