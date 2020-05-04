text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(" ")

ss=text[pos:]

ss=ss.strip()
ss=float(ss)
print(ss)
