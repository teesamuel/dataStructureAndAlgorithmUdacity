class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union( llist_1, llist_2):
        
        if llist_1.size()==0:
            return llist_2
        elif linked_list_2.size()==0:
            return llist_1

        joint_list=LinkedList()
        llist_1=llist_1.head
        seen=set()
        
        while llist_1:
            if llist_1.value not in seen:
                joint_list.append(llist_1.value)
            seen.add(llist_1.value)
            llist_1=llist_1.next
        llist_2=llist_2.head
        while llist_2:
            if llist_2.value not in seen:
                joint_list.append(llist_2.value)
            seen.add(llist_2.value)
            llist_2=llist_2.next
        if joint_list.size()==0:
            return -1
        # Your Solution Here
        return joint_list

def intersection(llist_1, llist_2):
    # Your Solution Here
        if llist_1.size()==0:
            return -1
        elif linked_list_2.size()==0:
            return -1
        hashtable=set()
        seen=[]
        joint_list=LinkedList()

        llist_1=llist_1.head
        while llist_1:
            hashtable.add(llist_1.value)
            llist_1=llist_1.next

        llist_2=llist_2.head
        while llist_2:
            if llist_2.value in hashtable and llist_2.value not in seen :
               joint_list.append(llist_2.value)
               seen.append(llist_2.value) 
            llist_2=llist_2.next
        if joint_list.size()==0:
            return -1
        return joint_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]


for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ("TEST CASE 1 UNION")
print (union(linked_list_1,linked_list_2))
print ("TEST CASE 1 INTERSECTION")
print (intersection(linked_list_1,linked_list_2))
# exit()
# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ("TEST CASE 2 UNION")
print (union(linked_list_3,linked_list_4))
print ("TEST CASE 2 INTERSECTION")
print (intersection(linked_list_3,linked_list_4))





linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1,3,3]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print ("TEST CASE 3 UNION")
print (union(linked_list_5,linked_list_6))
print ("TEST CASE 3 INTERSECTION")
print (intersection(linked_list_6,linked_list_6))
