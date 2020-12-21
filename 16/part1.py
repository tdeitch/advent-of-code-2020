import os
import sys

def parse_rule(line):
    name, rules = line.split(':')
    ranges = rules.split(' or ')
    return (name, tuple(tuple(int(i) for i in r.split('-')) for r in ranges))

def parse_ticket(line):
    return tuple(int(s) for s in line.split(','))

def load_input():
    rules = []
    other_tickets = []
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        for line in f:
            if line.strip() == '':
                break
            rules.append(parse_rule(line.strip()))
        for _i in range(4):
            f.readline()
        for line in f:
            other_tickets.append(parse_ticket(line.strip()))
    return rules, other_tickets

rules, other_tickets = load_input()
ranges = [range for rule in rules for range in rule[1]]

invalid = 0
for ticket in other_tickets:
    for num in ticket:
        for range in ranges:
            if num >= range[0] and num <= range[1]:
                break
        else:
            invalid += num

print(invalid)
