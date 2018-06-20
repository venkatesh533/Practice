
s = input('Enter a string\n')
s = str(s)
r = ''
i=0;l=len(s);
while i <= l-1:
    r = r+s[l-i-1]
    i = i+1
if r == s:
    print 'Palindrome'
else:
    print 'Not Palindrome'

