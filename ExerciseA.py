def bellman_ford(n, edges):
    INF = float('inf')
    dist = [INF] * n
    dist[0] = 0  # Começamos do nó 0
    
    # Relaxa as arestas n-1 vezes
    for _ in range(n - 1):
        for x, y, t in edges:
            if dist[x] != INF and dist[x] + t < dist[y]:
                dist[y] = dist[x] + t

    # Verifica se tem ciclos negativos
    for x, y, t in edges:
        if dist[x] != INF and dist[x] + t < dist[y]:
            return "possible"  # Tem um ciclo negativo

    return "not possible"

cases = int(input().strip())
for _ in range(cases):
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(bellman_ford(n, edges))
