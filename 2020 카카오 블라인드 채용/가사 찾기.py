class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.data:
            return True
        else:
            return False

    def starts_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words


def solution(words, queries):
    answer = []
    trie, btrie = Trie(), Trie()

    for word in words:
        trie.insert(word)
        btrie.insert(word[::-1])

    for i, query in enumerate(queries):
        cnt = 0
        if query[0] == '?':
            query_len, search_query = len(query), query.replace('?', '')[::-1]
            temp = btrie.starts_with(search_query)
            if temp != None:
                for each in temp:
                    if len(each) == query_len:
                        cnt += 1
        else:
            query_len, search_query = len(query), query.replace('?', '')
            temp = trie.starts_with(search_query)
            if temp != None:
                for each in temp:
                    if len(each) == query_len:
                        cnt += 1
        answer.append(cnt)

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "????o", "fr???", "fro???", "pro?"]))
