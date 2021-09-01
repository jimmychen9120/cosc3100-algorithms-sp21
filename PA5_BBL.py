import random

class Node:
    def __init__(self, key, value):
        self.key=key
        self.value=value
        self.nextptr=None
        self.downptr=None

class BBL:
    def __init__(self, key, value):
        self.head=Node(-1, '')
        self.head.downptr=Node(-1, '')

    def insert(self, current, key, value, down):
        newNode=Node(key, value)
        newNode.nextptr=current.nextptr
        current.nextptr=newNode
        if down:
            newNode.downptr=Node(key, value)
        
    def get_value(self, key, value):
        prob=2/3
        current=self.head
        while True:
            if current.nextptr and current.nextptr.key<key:
                current=current.nextptr
            elif current.nextptr and current.nextptr.key>key:
                if current.downptr:
                    if random.random()>prob:
                        down=True
                        self.insert(current, key, value, down)
                    current=current.downptr
                else:
                    self.insert(current, key, value, False)
                    break;
            else:
                self.insert(current, key, value, False)
                break;

    def printBBL(self):
        print("BBL:")
        nextNode=self.head
        while nextNode:
            print("{}: {}".format(nextNode.key, nextNode.value))
            nextNode=nextNode.nextptr

nodea=BBL(-1, '')
nodea.get_value(3, 'three')
nodea.get_value(6, 'six')
nodea.get_value(5, 'five')
nodea.get_value(18, 'eighteen')
nodea.get_value(12, 'twelve')
nodea.get_value(1, 'one')
nodea.printBBL()
