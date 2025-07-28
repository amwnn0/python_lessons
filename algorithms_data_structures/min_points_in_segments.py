segms = []
points = []
for _ in range(int(input())):
    segms.append([int(i) for i in input().split()])
segms = list(sorted(segms))

end = segms[0][1]
for segment in segms:
    if segment[0] > end:
        points.append(end)
        end = segment[1]
    if segment[1] < end:
        end = segment[1]
points.append(end)


print(len(points))
print(*points)
