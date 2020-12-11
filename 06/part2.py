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
  qs = set(ch for ch in form[0])
  for person in form:
    to_remove = set()
    for q in qs:
      if q not in person:
        to_remove.add(q)
    qs -= to_remove
  total += len(qs)
print(total)