#wap to perform set operation like union,intersection,differnece

sets1 = {1,2,3,4,5,6,7,8,9,10}
sets2 = {7,8,9,10,11,12,13,14}

print(f'Union {sets1 | sets2}')
print(f'Intersection {sorted(sets1 & sets2)}')
print(f'difference {sets1 - sets2}')