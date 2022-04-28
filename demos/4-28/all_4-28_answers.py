import random as r

r.seed(20220428)

# Flip 1,000 coins and count how many heads or tails your get
first_1000 = r.choices([0, 1], k=1000)
nh1 = first_1000.count(1)
print(nh1, 'heads in the frist 1000 coin flips, so the probability is {}'.format(nh1 / 1000))

# Flip 1,000 more and compare your results
second_1000 = r.choices([0, 1], k=1000)
nh2 = second_1000.count(1)
print(nh2, 'heads in the second 1000 coin flips, so the probability is {}'.format(nh2 / 1000))

# For a challenge: create an unfair coin, i.e., one where heads and tails are not equally probable
# let's say that heads is any value >= 2
# This gives us P(H) = 0.6, theoretically
possible_values = [0, 1, 2, 3, 4]
flips = r.choices(possible_values, k=1000)
nh3 = sum(f >= 2 for f in flips)
print(nh3, 'heads in 1000 flips of our unfair coin, so the probability is {}'.format(nh3 / 1000))
