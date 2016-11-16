import string
import random

def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def order_id_generator(size=16, chars=string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
