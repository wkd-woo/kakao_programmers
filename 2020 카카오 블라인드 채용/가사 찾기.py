from collections import defaultdict


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.number = defaultdict(int)


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head
        path = []

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            path.append(current_node)
            current_node = current_node.children[char]

        current_node.data = string

        icnt = 1
        for i in range(len(path) - 1, -1, -1):
            path[i].number[icnt] += 1
            icnt = icnt + 1

    def search(self, string):
        current_node = self.head
        temp = ''
        if not string:
            return 0

        for i, char in enumerate(string):
            if char in current_node.children:
                current_node = current_node.children[char]
            elif char == '?':
                temp = string[:i]
                break

        nums = string.count('?')
        if current_node.number[nums] == None:
            return 0
        return current_node.number[nums]


def solution(words, queries):
    answer = []
    trie, btrie = Trie(), Trie()

    for word in words:
        trie.insert(word)
        btrie.insert(word[::-1])

    for query in queries:
        if query[0] == '?':
            search_query = query[::-1]
            result = btrie.search(search_query)
        else:
            search_query = query
            result = trie.search(search_query)

        answer.append(result)

    return answer
