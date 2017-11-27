ClassList = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '4b', 'scores': [5, 3, 3, 2, 5]},
    {'school_class': '4v', 'scores': [4, 4, 2, 5, 1]}
]
NewSum = 0
for ViewList in ClassList:
    print(sum(ViewList['scores']))