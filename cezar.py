n = list(input())
shift = 1
ru_low = [1072, 1103]
ru_up = [1040, 1071]
en_up = [65, 90]
en_low = [97, 122]
language = ''
up = []
low = []
for i in n:
  if ru_up[0] <= ord(i) <= ru_low[1]:
    language = 'ru'
    up, low = ru_up, ru_low
    break
  elif en_low[0] <= ord(i) <= en_low[1] or en_up[0] <= ord(i) <= en_up[1]:
    language = 'en'
    up, low = en_up, en_low
    break
while shift != 0:
  m = n[:]
  shift = int(input())
  for i in range(len(m)):
    if m[i].isalpha() and m[i].islower():
        if low[0] <= ord(m[i]) + shift <= low[1]:
          m[i] = chr(ord(m[i]) + shift)
        else:
          if shift < 0:
            m[i] = chr(low[1] + 1 - (abs(shift) - (ord(m[i]) - low[0])))
          else:
            m[i] = chr(low[0] - 1 + (abs(shift) - (low[1] - ord(m[i]))))
    elif m[i].isalpha() and m[i].isupper():
        if up[0] <= ord(m[i]) + shift <= up[1]:
            m[i] = chr(ord(m[i]) + shift)
        else:
          if shift < 0:
            m[i] = chr(up[1] + 1 - (abs(shift) - (ord(m[i]) - up[0])))
          else:
            m[i] = chr(up[0] - 1 + (abs(shift) - (up[1] - ord(m[i]))))
  print(''.join(m))
