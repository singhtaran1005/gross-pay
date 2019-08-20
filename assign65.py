text = "X-DSPAM-Confidence:    0.8475"
a =text.find(':')
p=text[a+2:]
v=float(p)
print(v)