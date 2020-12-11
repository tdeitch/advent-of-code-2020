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
    result.append((int(num), name))
  return result


bags = dict()
bag_re = re.compile('^([a-z ]+) bags contain [0-9]+ [a-z ]+ bags?,? ?')
no_bag_re = re.compile('^([a-z ]+) bags contain no other bags.$')
with open(os.path.join(sys.path[0], 'input.txt')) as f:
  for line in f.readlines():
    if bag_re.match(line):
      bags[bag_re.match(line.strip()).groups()[0]] = split_bags(line.strip().split(" contain ")[1].split(", "))
    elif no_bag_re.match(line):
      bags[no_bag_re.match(line.strip()).groups()[0]] = ()

# Count bags _inside_ the given bag
def count(bag_name):
  total = 0
  for inner_num, inner_name in bags[bag_name]:
    total += inner_num * (1 + count(inner_name))
  return total

print(count(goal))