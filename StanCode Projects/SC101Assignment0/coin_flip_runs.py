"""
File: coin_flip_runs.py
Name: Zining Chen
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	1. Use function random to create H or T
	2. Ask the user to enter how many runs that they want to have.
	3. Keep comparing the last coin and the next one to check if they are the same. If they're the same one,
	then count 1.
	4. Stop when the number of count equals the number of runs.
	"""
	print('Let\'s flip a coin!')
	runs = int(input('Number of runs : '))
	count = 0
	coin = r.choice('TH')
	total_coin = str(coin)
	while True:
		if count == runs:
			break
		next_coin = r.choice('TH')
		if coin == next_coin:
			count += 1
		coin = next_coin
		total_coin += str(next_coin)
	print(str(total_coin))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
