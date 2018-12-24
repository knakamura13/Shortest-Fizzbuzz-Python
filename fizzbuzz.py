# 
# A simple fizzbuzz program with the fewest number of lines possible,
# 	while also maintaining readability and code excellence!
# 

def fb(i, res):
  if i%3==0: res = res + "Fizz"
  if i%5==0: res = res + "Buzz"
  return res or i
for i in range(100): print(fb(i, ""))
