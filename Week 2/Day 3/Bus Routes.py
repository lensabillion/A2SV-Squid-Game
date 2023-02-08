class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        seen = set()
        adj = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                adj[stop].append(i)
        bus = 1
        q = deque([source])
       
        while q:
            for _ in range(len(q)):
                curr  = q.popleft()
                
                for nxt_route in adj[curr]:
                    if nxt_route not in seen:
                        seen.add(nxt_route)
                        for nxt_stop in routes[nxt_route]:
                            
                                if nxt_stop == target:
                                    return bus
                                q.append(nxt_stop)
            bus += 1

        return -1