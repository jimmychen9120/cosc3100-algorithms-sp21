import random

class Node:
    def __init__(self, key, value, next_node):
        self.key = key
        self.value = value
        self.next_node = next_node

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, key, value):
        new_node = Node(key, value, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        elif self.head.key > key: 
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.key < key:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
            if not new_node.next_node:
                self.tail = new_node
            

    def update_by_value(self, old_value, new_value):
        current = self.head
        while(current):
            if current.value == old_value:
                current.value = new_value
                return
            current = current.next_node

    def update(self, key, new_value):
        current = self.head
        while(current):
            if current.key == key:
                current.value = new_value
                return
            current = current.next_node

    def write(self):
        print("Head {}: {}".format(self.head.key, self.head.value))
        print("Tail {}: {}".format(self.tail.key, self.tail.value))
        current_node = self.head
        while current_node:
            print("{}: {}".format(current_node.key, current_node.value))
            current_node = current_node.next_node



records = [ (1,'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'),
            (6, 'six'), (7, 'seven'), (8, 'eight'), (9, 'nine'), (10, 'ten'),
            (11, 'eleven'), (12, 'twelve') ]
for _ in range(5):
    lista = List()
    random.shuffle(records)
    for r in records:
        lista.insert(* r)
    lista.write()
    print(10*'-')

