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

def is_height(hgt):
  if not (hgt.endswith("cm") or hgt.endswith("in")):
    return False
  try:
    n = int(hgt[:-2])
    unit = hgt[-2:]
    if unit == "cm":
      if 150 <= n <= 193:
        return True
    elif unit == "in":
      if 59 <= n <= 76:
        return True
    return False
  except ValueError:
    return False

def is_hair_color(hcl):
  if len(hcl) != 7 or not hcl.startswith("#"):
    return False
  if any(ch not in "0123456789abcdef" for ch in hcl[1:]):
    return False
  return True

def is_passport_id(pid):
  if len(pid) != 9:
    return False
  if any(ch not in "0123456789" for ch in pid):
    return False
  return True

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
def is_valid(passport):
  if any((k not in passport for k in ("ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"))):
    return False
  byr = passport["byr"]
  iyr = passport["iyr"]
  eyr = passport["eyr"]
  hgt = passport["hgt"]
  hcl = passport["hcl"]
  ecl = passport["ecl"]
  pid = passport["pid"]

  try:
    if not (len(byr) == 4 and 1920 <= int(byr) <= 2002):
      return False
    if not (len(iyr) == 4 and 2010 <= int(iyr) <= 2020):
      return False
    if not (len(eyr) == 4 and 2020 <= int(eyr) <= 2030):
      return False
    if not is_height(hgt):
      return False
    if not is_hair_color(hcl):
      return False
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
      return False
    if not is_passport_id(pid):
      return False
  except ValueError:
    return False

  return True

print(len([p for p in passports if is_valid(p)]))