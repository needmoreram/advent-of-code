import re

rules = {}
invrules = {}
subbags = {}
exp = re.compile('(\d+) (\w+ \w+)')

with open('input/input-7.txt') as f:
    rule = f.readline()
    while rule:
        rule = rule.split(' bag')
        forbag = rule[0]
        rules[forbag] = []
        for hasbag in rule[1:]:
            m = exp.search(hasbag)
            if m:
                n = m.group(1)
                t = m.group(2)
                rules[forbag].append((int(n), t))
                if t not in invrules:
                    invrules[t] = []
                invrules[t].append(forbag)
        if rules[forbag] == []:
            subbags[forbag] = 0
        rule = f.readline()

q = invrules["shiny gold"]
ans = 0
explored = set()

while len(q) > 0:
    bag = q.pop(0)
    if bag in explored:
        continue
    explored.add(bag)
    ans += 1
    if bag not in invrules:
        continue
    for morebags in invrules[bag]:
        if morebags not in q:
            q.append(morebags)
print("part 1:", ans)

def explore_bag(bag_name):
    if bag_name in subbags:
        return subbags[bag_name]
    subbags[bag_name] = 0
    q = rules[bag_name]
    while len(q) > 0:
        bag = q.pop(0)
        v = explore_bag(bag[1]) + 1
        subbags[bag_name] += v * bag[0]
    return subbags[bag_name]
print("part 2:", explore_bag("shiny gold"))
