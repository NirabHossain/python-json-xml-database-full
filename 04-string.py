text = "X-DSPAM-Confidence:    0.8475"
number=text.find('0')
num=float(text[number:number+6])
print(num)
