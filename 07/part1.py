import os
import re
import sys

goal = "shiny gold"

def split_bags(bs):
  result = []
  for b in bs:
    r = b.replace(".", "")
    r = r.replace(" bags", "")
    r = r.replace(" bag", "")
    num, name = r.split(" ", 1)
    result.append(name)
  return result


bags = dict()
bag_re = re.compile('^([a-z ]+) bags contain [0-9]+ [a-z ]+ bags?,? ?')
no_bag_re = re.compile('^([a-z ]+) bags contain no other bags.$')
with open(os.path.join(sys.path[0], 'input.txt')) as f:
  for line in f.readlines():
    if bag_re.match(line):
      bags[bag_re.match(line.strip()).groups()[0]] = split_bags(line.strip().split(" contain ")[1].split(", "))
    elif no_bag_re.match(line):
      bags[no_bag_re.match(line.strip()).groups()[0]] = []

reachable = {}
def is_reachable(bag):
  if bag in reachable:
    return reachable[bag]
  for inner_bag in bags[bag]:
    if is_reachable(inner_bag) or inner_bag == goal:
      reachable[bag] = True
      return True
  reachable[bag] = False
  return False

total = 0
for bag in bags:
  if is_reachable(bag):
    total += 1
print(total)