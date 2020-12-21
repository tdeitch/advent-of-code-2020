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
        f.readline()
        my_ticket = parse_ticket(f.readline().strip())
        f.readline()
        f.readline()
        for line in f:
            other_tickets.append(parse_ticket(line.strip()))
    return rules, my_ticket, other_tickets

def valid_rules(rules, num):
    valid = set()
    for name, ranges in rules:
        for lower, upper in ranges:
            if num >= lower and num <= upper:
                valid.add(name)
    return valid

def valid_tickets(rules, tickets):
    ranges = [range for rule in rules for range in rule[1]]
    valid = []
    for ticket in tickets:
        for num in ticket:
            for lower, upper in ranges:
                if num >= lower and num <= upper:
                    break
            else:
                break
        else:
            valid.append(ticket)
    return valid

def only(one_element_set):
    return next(iter(one_element_set))

def initial_matches(rules, tickets):
    matches = dict()
    for pos in range(len(tickets[0])):
        possible = set(i for i in range(len(rules)))
        valid = set(name for name, ranges in rules)
        for ticket in tickets:
            val = ticket[pos]
            valid &= valid_rules(rules, val)
        matches[pos] = valid
    return matches

def find_matches(rules, matches):
    processed = set()
    while True:
        for pos, rules in matches.items():
            if len(rules) == 1 and only(rules) not in processed:
                found_rule = only(rules)
                break
        else:
            break
        for pos, rules in matches.items():
            if len(rules) > 1:
                rules.remove(found_rule)
        processed.add(found_rule)
    return matches

def departure_fields(matches):
    fields = []
    for pos, names in matches.items():
        if only(names).startswith('departure'):
            fields.append(pos)
    return fields

rules, my_ticket, other_tickets = load_input()
valid = valid_tickets(rules, other_tickets)
init_matches = initial_matches(rules, valid)
matches = find_matches(rules, init_matches)
fields = departure_fields(matches)

product = 1
for field in fields:
    product *= my_ticket[field]
print(product)
