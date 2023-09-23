n = int(input())
set_first = set()
set_second = set()

max_len_intersection = 0
max_intersection = None

for _ in range(n):
    ranges = input().split('-')

    first_start, first_end = [int(x) for x in ranges[0].split(',')]
    second_start, second_end = [int(x) for x in ranges[1].split(',')]

    set_first.clear()
    set_second.clear()
    for i in range(first_start, first_end+1):
        set_first.add(i)
    for i in range(second_start, second_end+1):
        set_second.add(i)

    intersection = list(set_first.intersection(set_second))
    intersection_length = len(intersection)

    if intersection_length > max_len_intersection:
        max_len_intersection = intersection_length
        max_intersection = intersection

print(f"Longest intersection is {max_intersection} with length {max_len_intersection}")
