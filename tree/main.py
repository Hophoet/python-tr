from tree import Node


if __name__ == '__main__':
    n1 = Node(1)
    n1.add_node(Node(5))
    n1.add_node(Node(8))
    n1.add_node(Node(-4))
    n1.add_node(Node(0))
    n1.add_node(Node(12))
    n1.add_node(Node(2))
    # n3 = Node(3)
    # n3.set_right_node(Node(-23))
    # n1.add_node(n3)
    # print(n1.search_node(Node(3)))

    print('height:', Node.height(n1))
    print('max:', Node.max(n1))
    print('min:', Node.min(n1))
    print('is binary tree:', Node.is_binary_tree(n1))