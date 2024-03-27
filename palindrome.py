n="madam"
i=0
j=len(n)-1
print(i)
print(j)
while i<j:
  if n[0]!=n[j]:
    print("its not a palindrome")
    break
  i=i+1
  j=i-1
else:
  print("its a palindrome")
