import sys
import heapq
class Node(object):
    def __init__(self,frequency,character):
        self.character=character
        self.frequency=frequency
        self.left_child=None
        self.right_child=None
        self.bit=None
        
    def __lt__(self, other):
        return self.frequency < other.frequency

    def __eq__(self, other):
        if other is None:
            return False

        if not isinstance(other, Node):
            return False
        return self.frequency == other.frequency

# character, frequency, left child, and right child.


class Huffman:
    def __init__(self):
        self.heap=[]
        self.tree=[]
        self.frequency={}
        self.huffman_code={}

    def calculate_frequency(self,data):
        '''
        This function loops through a list of strings to return a frequency table.

        INPUTS: 
        * data string
        OUTPUTS:
            * a dictionary show the frequery of occurence of Alphaphet Key(Alphabet):Value(frequency)  \
        '''
        table={}
        for el in data:
            if el in table:
                table[el] += 1
            else:
                table[el] = 1
        return table

    def make_heap(self,table):
        for key in table:
            node = Node(table[key],key)
            heapq.heappush(self.heap, node)
            self.tree.append(node)
            self.tree = sorted(self.tree)
    def creat_node(self):
        # Pop-out two nodes with the minimum frequency from the priority queue created in the above step.
        # Create a new node with a frequency equal to the sum of the two nodes picked in the above step
        while len(self.heap) > 1:
            first_node=heapq.heappop(self.heap) # 
            second_node=heapq.heappop(self.heap)
            new_node= Node(first_node.frequency + second_node.frequency,None)
            new_node.left_child=first_node
            new_node.right_child=second_node
            self.tree.append(new_node)
            heapq.heappush(self.heap,new_node)
    # For each node, in the Huffman tree, assign a bit 0 for
    #  left child and a 1 for right child. See the final Huffman tree for our example:
    def assign_bit(self):
        for elements in self.tree:
            if elements.character is None:
                elements.left_child.bit = 0
                elements.left_child.bit = 1
    def generate_huffman_code(self):
        # if self.tree==None:
        #     return
        if len(self.tree) > 0:
            current_code = ""
            root_node= self.tree[len(self.tree)-1]
            self.calculate_huffman_code(root_node,current_code) 

    def calculate_huffman_code(self, root_node,current_code):
         if root_node==None:
             return
         if root_node.character !=None:
             self.huffman_code[root_node.character]=current_code
             return
         self.calculate_huffman_code( root_node.left_child, current_code +"0")
         self.calculate_huffman_code( root_node.right_child, current_code +"1")

    def encode_text(self,text):
        encoded_output=""
        for chr in str(text):
            encoded_output += self.huffman_code[chr]
        return encoded_output

    def decode_string(self,encoded):
        encoded_list=[]
        if len(self.tree) < 1:
            return
        for item in encoded:
            encoded_list.append(item)

        current_code=encoded_list.pop(0)
        root = self.tree[len(self.tree) - 1]
        output=""
        while (encoded_list):
          
            if root.character is None:
                if current_code==0:
                    root=root.left_child
                else:
                    root=root.left_child
            else:
                output += root.character
                root = self.tree[len(self.tree) - 1]
            current_code=encoded_list.pop(0)
        return output

         

data = 'AAAAAAABBBCCCCCCCDDEEEEEE'


def huffman_encoding(data):
    heap = Huffman()
    heaps = heap.calculate_frequency(data)
    print(heaps)
    
    heap.make_heap(heaps)
    heap.creat_node()
    heap.assign_bit()
    heap.generate_huffman_code()
    # exit()
    return (heap.encode_text(data), heap.tree)

        


a_great_sentence = "The bird is the word"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

def decode_string(data, tree):
    output_string = ""
    if len(tree) > 0:
        root = tree[len(tree) - 1]
        current_node = root
        for bit in data:
            while current_node.character is None:
                if bit == '0':
                    current_node = current_node.left_child
                    break
                else:
                    current_node = current_node.right_child
                    break
            if current_node.character is not None:
                output_string += current_node.character
                current_node = root
    return output_string
decoded_data = decode_string(encoded_data, tree)
print(" Decoded DATA 1 ",decoded_data)

sentence_2= 'This project is tough although I was happy I could solved it'
sentence_3= 'I need to play FIFA 21 !!!!!'
sentence_4= 'a'
sentence_5= ''
sentence_6= 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

encoded_data_2, tree2 = huffman_encoding(a_great_sentence)


print ("The size of the data is: {}\n".format(sys.getsizeof(sentence_2)))
print ("The content of the data is: {}\n".format(sentence_2))

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data_2, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data_2))

decoded_data_2 = decode_string(encoded_data_2, tree2)
print(" Decoded DATA 2 ",decoded_data_2)

encoded_data_3, tree3 = huffman_encoding(sentence_3)

print ("The size of the data is: {}\n".format(sys.getsizeof(sentence_3)))
print ("The content of the data is: {}\n".format(sentence_3))

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data_3, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data_3))


decoded_data_3 = decode_string(encoded_data_3, tree3)
print(" Decoded DATA 3 ",decoded_data_3)


encoded_data_4, tree4 = huffman_encoding(sentence_4)

print ("The size of the data is: {}\n".format(sys.getsizeof(sentence_4)))
print ("The content of the data is: {}\n".format(sentence_4))

print(encoded_data_4)
# print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data_4, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data_4))

decoded_data_4 = decode_string(encoded_data_4, tree4)
print(" Decoded DATA 4 ",decoded_data_4)

encoded_data_5, tree5 = huffman_encoding(sentence_5)

print ("The size of the data is: {}\n".format(sys.getsizeof(sentence_5)))
print ("The content of the data is: {}\n".format(sentence_5))

# print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data_5, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data_5))


decoded_data_5 = decode_string(encoded_data_5, tree5)
print(" Decoded DATA 5 ",decoded_data_5)


encoded_data_6, tree6 = huffman_encoding(sentence_6)

print ("The size of the data is: {}\n".format(sys.getsizeof(sentence_6)))
print ("The content of the data is: {}\n".format(sentence_6))

# print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data_6, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data_6))


decoded_data_6 = decode_string(encoded_data_6, tree6)
print(" Decoded DATA 6 ",decoded_data_6)
