from d20 import roll

while True:
    roll_result = roll(input(), allow_comments=True)
    print(str(roll_result))

# I will have to mess with this primarily, since I am adding so much functionality TODO