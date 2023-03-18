# python3
import heapq

def parallel_processing(n, m, data):
    output = []
    laiks = [0] * n
    rinda = []
    
    for i in range(n):
        rinda.append((0, i))
    heapq.heapify(rinda)

    for i in range(m):
        laiks2 = data[i]
        sakums, a = heapq.heappop(rinda)
        output.append((a, sakums))
        sakums = sakums + laiks2
        laiks[a] = sakums
        heapq.heappush(rinda, (sakums, a))
    return output

def main():
    n, m = map(int, input().split())
    data = [int(x) for x in input().split()]

    result = parallel_processing(n,m,data)
    
    for a, sakums in result:
        print(a, sakums)


if __name__ == "__main__":
    main()
