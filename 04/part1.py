import os
import sys

passports = []

with open(os.path.join(sys.path[0], 'input.txt')) as f:
  for passport in f.read().split("\n\n"):
    parsed = {}
    for field in passport.replace(" ", "\n").split("\n"):
      k, v = field.strip().split(":")
      parsed[k] = v
    passports.append(parsed)

def is_valid(passport):
  return all((k in passport for k in ("ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt")))

print(len([p for p in passports if is_valid(p)]))