import sys


def main():
	max_size = int(sys.stdin.readline())

	if max_size == 0:
		for line in sys.stdin:
			line = line.strip()
			if not line:
				continue
			if line.startswith('push'):
				sys.stdout.write('ok\n')
			elif line.startswith('pop'):
				sys.stdout.write('error\n')
			elif line.startswith('count'):
				sys.stdout.write('0\n')
			elif line.startswith('exit'):
				sys.stdout.write('bye\n')
				break
		return

	# Основной случай: max_size > 0
	arr = [0] * max_size
	head = 0
	tail = 0
	count = 0

	for line in sys.stdin:
		line = line.strip()
		if not line:
			continue

		if line.startswith('push'):
			_, val_str = line.split()
			val = int(val_str)

			if count == max_size:
				head = (head + 1) % max_size
				count -= 1

			arr[tail] = val
			tail = (tail + 1) % max_size
			count += 1
			sys.stdout.write('ok\n')

		elif line.startswith('pop'):
			if count == 0:
				sys.stdout.write('error\n')
			else:
				last_idx = (tail - 1) % max_size
				sys.stdout.write(str(arr[last_idx]) + '\n')
				tail = last_idx
				count -= 1

		elif line.startswith('count'):
			sys.stdout.write(str(count) + '\n')

		elif line.startswith('exit'):
			sys.stdout.write('bye\n')
			break


if __name__ == '__main__':
	main()