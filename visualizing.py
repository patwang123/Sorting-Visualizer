import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from sorting import *

def main():
	n = int(input("Size of array: "))
	al = int(input("Choose sorting algorithm (0: QuickSort, 1: MergeSort, 2: InsertionSort): "))

	sort_dict = {0: QuickSort, 1: MergeSort, 2: InsertionSort, 3: SelectionSort, 4: HeapSort, 5: CountingSort}
	sorter = sort_dict[al](n)
	frames = sorter.start()

	fig, ax = plt.subplots()
	ax.set_title(sorter.name)

	bar = ax.bar(range(len(sorter.arr)), sorter.arr, align='edge')

	ax.set_xlim(0, n)
	ax.set_ylim(0, n)
	text = ax.set_xlabel('Swaps: 0')

	def animate(frames, bar=bar):
		for f in frames:
			if type(f[1]) == str:
				bar[f[0]].set_color(f[1])
			else:
				bar[f[0]].set_height(f[1])
				text.set_text("Swaps: {0}, Comparisons: {1}, Time: {2} seconds".format(\
					sorter.swaps,sorter.comparisons,"%.2f" % round(time.time()-sorter.time,2)))

	animation = anim.FuncAnimation(fig, func=animate, frames=frames, interval=5, repeat=False,cache_frame_data=False)
	plt.show()
if __name__ == "__main__":
    main()