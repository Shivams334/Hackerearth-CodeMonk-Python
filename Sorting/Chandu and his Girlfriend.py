    tc = input()
    for _ in range(tc):
        n = input()
        arr = map(eval, raw_input().split())
        arr.sort(reverse=True)
        some =  ' '.join(str(x) for x in arr)
        print some
