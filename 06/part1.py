import os
import sys

forms = []
with open(os.path.join(sys.path[0], 'input.txt')) as f:
  form = []
  for line in f.readlines():
    if line.strip() == "":
      forms.append(form)
      form = []
    else:
      form.append(line.strip())

total = 0
for form in forms:
  qs = set()
  for person in form:
    for ch in person:
      qs.add(ch)
  total += len(qs)
print(total)