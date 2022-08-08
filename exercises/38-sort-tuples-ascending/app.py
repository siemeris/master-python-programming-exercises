from operator import itemgetter, attrgetter

l = []

s = input()
l.append(tuple(s.split(",")))

print (sorted(l, key=itemgetter(0,1,2)))