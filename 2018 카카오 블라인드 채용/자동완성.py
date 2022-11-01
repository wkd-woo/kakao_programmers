class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.frequency = 0


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
            current_node.frequency += 1
        current_node.data = string

    def search(self, string):
        current_node = self.head

        for i, char in enumerate(string):
            if current_node.frequency == 1:
                return i

            if char in current_node.children:
                current_node = current_node.children[char]

        return len(string)


def solution(words):
    answer = 0
    trie = Trie()
    for word in words:
        trie.insert(word)

    for word in words:
        answer += trie.search(word)

    return answer
