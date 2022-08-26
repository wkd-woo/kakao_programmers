from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    for city in cities:
        city = city.lower()
        if city not in cache:
            answer += 5
        else:
            answer += 1
            cache.remove(city)
        if cache and len(cache) >= cacheSize:
            cache.popleft()
        if cacheSize > len(cache): 
            cache.append(city)
        
    return answer