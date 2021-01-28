# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 18:40:20 2020

@author: James
"""

#Priority Queue
class Node: #node initialise
    def __init__(self, content=None, priority = None, next=None): #initialise, including priority
        self.content = content #content intialiser
        self.next  = next     #next in queue initialiser
        self.priority = priority #priority initialiser

class PriorityQueue:
    def __init__(self):     #initialise queue
        self.length = 0     #queue length
        self.head = None    #first in sequence

    def is_empty(self):
        return self.length == 0 #true/false if length exists

    def clear(self):
        self.length = 0 #length set back to zero
        self.head = None #remove all nodes
        
    def insertInQueue(self, content, priority):   
        node = Node(content, priority) #input a node
        if self.head == None: #if the node is the first node in queue
            self.head = node #set head of queue as node
        else: #otherwise if not the first node in queue
            if priority < self.head.priority: #see if the new node's priority 
                                                #is smaller than the current smallest
                node.next = self.head #if self.head is bigger, set as the next node
                self.head = node #set the current node as the new self.head (first in queue)
            else: #otherwise if priority > self.head.priority
                smallest = self.head #current smallest stays the same (new node is not kept as smallest)
                while smallest.priority <= priority: #move through current queue whilst finding a position
                                                        #for the new node
                    prev = smallest #the previous queue position moved back
                    smallest = smallest.next  #new smallest updated (second smallest)
                    if smallest == None: #if it reaches the end of the queue (== None), break out (ironically would be the biggest)
                        break
                prev.next = node #once the new node has found its position, record it between the previous smallest
                node.next = smallest #and the bigger smallest (confusing I know)
        self.length = self.length + 1 #update the length of the queue

    def removeFromQueue(self):  #remove the nodes in their priority order (1 to n)
        content = self.head.content #record the content of the current front of the queue
        self.head = self.head.next #record next of the queue
        self.length = self.length - 1 #remove length of the queue
        return content #return the content of the head of the queue



