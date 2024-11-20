import re

y = "From steve@ucmo.edu is it 12 or 19. Where are you From: I amm from india"
y = re.findall('^From .*@([^ ]*)',y)
print(y)