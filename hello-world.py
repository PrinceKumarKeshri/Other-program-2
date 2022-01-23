# -*- coding: utf-8 -*-
"""
Created on Sun May  9 14:35:53 2021

@author: 0526p
"""

# print('hello world')
#name = input("Enter Name : ")
#for i in name:
#    print(i)
 
class Node(object):
    
    def __init__(self, data):
        
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None
        


class AVL(object):
    
    def __init__(self):
        
        self.root = None
        
    
    
    def insert(self, data):
        
        self.root = self.insertNode(data, self.root)
        
    
    
    def insertNode(self, data, node):
        
        if not node:
            return Node(data)
        
        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild)
        
        else:
            node.rightChild = self.insertNode(data, node.rightChild)
            
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        
        return self.settleViolation(data, node)
    
    
    
    def settleViolation(self, data, node):
        
        balance = self.calcBalance(node)
        
        # case 1 --> left left heavy situation
        if balance > 1 and data < node.leftChild.data:
            print("Left left heavy situation ...")
            return self.rotateRight(node)
        
        # case 2 --> right right heavy situation --> single left rotation
        if balance < -1 and data > node.rightChild.data:
            print("Right right heavy situation ...")
            return self.rotateLeft(node)
        
        if balance > 1 and data > node.leftChild.data:
            print("Left right heavy situation ...")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)
        
        if balance < -1 and data < node.rightChild.data:
            print("Right left heavy situation ...")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)
        
        return node
    
    
    
    
    def remove(self, data):
        
        if self.root:
            self.root = self.removeNode(data, self.root)
    
    
    
    def removeNode(self, data, node):
        
        if not node:
            return node
    
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
            
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        
        else:
            
            if not node.leftChild and not node.rightChild:
                print("Removing a leaf node...")
                del node
                return None
            
            if not node.leftChild:
                print("Removing a node with a right child ...")
                tempNode = node.rightChild
                del node
                return tempNode
            
            elif not node.rightChild:
                print("Removing a node with a left child ...")
                tempNode = node.leftChild
                del node
                return tempNode
            
            print("Removing node with two children....")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)
    
        if not node:
            return node # if the tree had just a single node

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        balance = self.calcBalance(node)

        #doubly left heavy situation
        if balance > 1 and self.calcBalance(node.leftChild) >= 0:
            return self.rotateRight(node)

        #left right case
        if balance > 1 and self.calcBalance(node.leftChild) < 0:
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        #right right case
        if balance < -1 and self.calcBalance(node.rightChild) <= 0:
            return self.rotateLeft(node)
        
        #right left case
        if balance < -1 and self.calcBalance(node.rightChild) > 0:
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)
        
        return node
            
    
    def getPredeccessor(self, node):
        
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        
        return node
    
    
    def calcHeight(self, node):
        
        if not node:
            return -1
        
        return node.height
    
    
    
    # if it returns value > 1 it means it is a left heavy tree --> right rotation
    # ------------------- < -1 right heavy tree --> left rotation
    
    def calcBalance(self, node):
        
        if not node:
            return 0
        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)
    
    
    def traverse(self):
        
        if self.root:
            self.traverseInOrder(self.root)
            
    
    def traverseInOrder(self, node):
        
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
            
        print(node.data)
        
        if node.rightChild:
            self.traverseInOrder(node.rightChild)
        
        
    
    def rotateRight(self, node):
        
        print(f"Rotating to the right on node =  {node.data}")
        
        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild
        
        tempLeftChild.rightChild = node
        node.leftChild = t
        
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) + 1
        
        return tempLeftChild
    
    
    
    def rotateLeft(self, node):
        
        print(f"Rotating to the left on node = {node.data}")
        
        tempRightChild = node.rightChild
        t = tempRightChild.leftChild
        
        tempRightChild.leftChild = node
        node.rightChild = t
        
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightChild)) + 1
        
        return tempRightChild
    
    
    
    
avl = AVL()   

avl.insert(10)
avl.insert(20)
avl.insert(5)
avl.insert(4)
avl.insert(15)
avl.traverse()
print()
avl.remove(5)
print()
avl.remove(4)
print()
avl.traverse()


i  = 'prince kumar'
l = i.split(' ')
l
l.reverse()
l
l = ' '.join(l)
l
type(l)
for i in l:
    print(i)
