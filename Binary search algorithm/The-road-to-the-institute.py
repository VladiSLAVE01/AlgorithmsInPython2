# let's get started!!!
import math


def solve():
	# Чтение входных данных
	V_o, V_s = map(int, input().split())
	S = int(input())

	# Вычисление координаты границы города
	a = 1 - S / 100.0

	# Функция времени пути для заданной точки въезда x
	def time(x):
		# Расстояние от дома (0,1) до точки въезда (x,a)
		dist_outside = math.sqrt(x * x + (a - 1) * (a - 1))
		# Расстояние от точки въезда (x,a) до института (1,0)
		dist_inside = math.sqrt((1 - x) * (1 - x) + a * a)
		# Общее время
		return dist_outside / V_o + dist_inside / V_s

	# Производная функции времени (для проверки знака)
	def derivative(x):
		if x == 0:
			# В точке 0 производная может быть определена по пределу
			# Но бинарный поиск не будет вызывать с x=0, кроме начальной проверки
			term1 = 0
		else:
			term1 = x / (V_o * math.sqrt(x * x + (a - 1) * (a - 1)))

		if x == 1:
			term2 = 0
		else:
			term2 = (1 - x) / (V_s * math.sqrt((1 - x) * (1 - x) + a * a))

		return term1 - term2

	left, right = 0.0, 1.0

	# поиск
	for _ in range(100):  # 100 итераций для высокой точности
		mid = (left + right) / 2
		if derivative(mid) < 0:
			left = mid
		else:
			right = mid

	# Оптимальное x - середина интервала
	optimal_x = (left + right) / 2

	# Выводим результат с 6 знаками после запятой
	print(f"{optimal_x:.6f}")


if __name__ == "__main__":
	solve()

