import heapq
from collections import defaultdict


def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    INF = int(1e9)
    answer = []
    summits = set(summits)
    for u, v, w in paths:
        graph[u].append([v, w])
        graph[v].append([u, w])

    def dijkstra():
        queue = []
        distance = [INF] * (n + 1)

        for gate in gates:  # 시작점은 제외
            distance[gate] = 0
            heapq.heappush(queue, (0, gate))

        while queue:
            dist, node = heapq.heappop(queue)

            if distance[node] < dist:
                continue

            if node in summits:  # 정상에 도달하면 넘김
                answer.append([distance[node], node])
                continue

            for next_node, next_dist in graph[node]:
                # 지금까지 경로 중 가장 비용이 큰 것을 저장
                cost = max(distance[node], next_dist)
                if cost < distance[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(queue, (distance[next_node], next_node))

        return distance

    dijkstra()
    answer.sort()  # 산봉우리의 번호가 가장 낮은 것 sorting
    return [answer[0][1], answer[0][0]]
