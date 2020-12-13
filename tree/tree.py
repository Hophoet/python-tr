""" Binary tree management module"""

#node class
class Node:

    #constructor
    def __init__(self, value):
        """ node constructor """
        self.__value = value
        self.__right_node = None
        self.__left_node = None

    #getters and setters
    def get_value(self): return self.__value
    def get_right_node(self): return self.__right_node
    def get_left_node(self): return self.__left_node
    
    def set_value(self, new_value): self.__value = new_value
    def set_right_node(self, new_right_node): self.__right_node = new_right_node
    def set_left_node(self, new_left_node): self.__left_node = new_left_node


    #add node method
    def add_node(self, node):
        """ add node method """
        #node alraidy exists case
        if self.__value == node.get_value():
            return
        #node to add > to the  current node
        if node.get_value() > self.__value:
            #right node exists case
            if self.__right_node:
                self.__right_node.add_node(node)
            #right node not exists yet case
            else:
                self.set_right_node(node)
        #node to add < to the current node
        elif node.get_value() < self.__value:
            #left node exists case
            if self.__left_node:
                self.__right_node.add_node(node)
            #left node not exists yet case
            else:
                self.set_left_node(node)

    #search node method
    def search_node(self, node):
        """ search node method """
        #node find
        if node.get_value() == self.__value:
            return True
        #search node > to the current node
        elif node.get_value() > self.__value:
            # right node exists case
            if self.__right_node:
                return self.__right_node.search_node(node)
            # right node not exists case
            else:
                return False
        #search node < to the current node
        elif node.get_value() < self.__value:
            #left node exists case
            if self.__left_node:
                return self.__left_node.search_node(node)
            #left node not exists case
            else:
                return False

    #heigh
    @classmethod
    def height(cls, node):
        if not node:
            return 0
        else:
            return 1+ max(Node.height(node.get_left_node()), Node.height(node.get_right_node()))

        
    #max
    @classmethod
    def max(cls, node):
        if not node.get_right_node():
            return node.get_value()
        else:
            return Node.max(node.get_right_node())

    #min 
    @classmethod
    def min(cls, node):
        if not node.get_left_node():
            return node.get_value()
        else:
            return Node.min(node.get_left_node())


    #is binary tree
    @classmethod
    def is_binary_tree(cls, node):
        if node.get_left_node():
            if node.get_left_node().get_value() > node.get_value():
                return False
            else:
                return cls.is_binary_tree(node.get_left_node())
        if node.get_right_node():
            if node.get_right_node().get_value() < node.get_value():
                return False
            else:
                return cls.is_binary_tree(node.get_right_node())
        return True
            
        


