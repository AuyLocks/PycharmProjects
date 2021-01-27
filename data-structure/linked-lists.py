"""
https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
"""

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
        # print(middleNode.nextval)
        NewNode = Node(newdata)

        NewNode.nextval = middleNode.nextval
        middleNode.nextval = NewNode

    def RemoveNode(self, removeKey):
        HeadVal = self.headval

        if (HeadVal is not None):
            if (HeadVal.dataval == removeKey):
                self.headval = HeadVal.nextval
                HeadVal = none
                return

        while (HeadVal is not None):
            if HeadVal.dataval == removeKey:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextval

        if (HeadVal == None):
            return

        prev.nextval = HeadVal.nextval

        HeadVal = None




llist = SingleLinkedList()
llist.AtBeginning("Mon")
llist.AtBeginning("Tue")
llist.AtBeginning("Wed")
llist.AtBeginning("Thu")
llist.RemoveNode("Tue")
print(llist.headval.dataval)
llist.listprint()