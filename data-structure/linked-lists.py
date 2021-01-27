class Node:

    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SingleLinkedList:

    def __init__(self):
        self.headval = None

    # Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    # Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode

    #  Inserting a new element at the beginning
    def AtBeginning(self, newdata):
        NewNode = Node(newdata)

        # Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

    # Inserting in between two Data Nodes
    def InBetween(self, middleNode, newdata):
        if middleNode is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middleNode.nextval
        middleNode.nextval = NewNode




list = SingleLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2
e2.nextval = e3

list.AtEnd("Thu")
list.AtBeginning("Sun")

list.listprint()
