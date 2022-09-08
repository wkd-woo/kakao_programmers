import heapq
from collections import defaultdict

INF = int(1e9)


def solution(n, s, a, b, fares):
    answer = 0
    db = defaultdict(list)
    for u, v, w in fares:
        db[u].append([v, w])
        db[v].append([u, w])

    def dijkstra(graph, start): 
        queue = []
        heapq.heappush(queue, (0, start))
        distance = [INF] * (n + 1)
        distance[start] = 0

        while queue:
            dist, node = heapq.heappop(queue)

            if distance[node] < dist:
                continue

            for next in graph[node]:
                cost = distance[node] + next[1]
                if cost < distance[next[0]]:
                    distance[next[0]] = cost
                    heapq.heappush(queue, (cost, next[0]))
        return distance
        
    answer = INF
    for i in range(1, n+1):
        answer = min(answer, dijkstra(db, s)[i] + dijkstra(db, i)[a] + dijkstra(db, i)[b])
    
    return answer