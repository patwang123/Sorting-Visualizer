import random
import time

class Algorithm:
	def __init__(self,size,name):
		self.name = name
		self.size = size
		self.arr = [1+x for x in random.sample(range(size),size)]
		self.color = ['b' for b in self.arr]
		self.swaps = 0
		self.comparisons = 0
	def start(self):
		self.time = time.time()
		yield from self.sort()
class QuickSort(Algorithm):
	def __init__(self,size):
		super().__init__(size,'Quick Sort')
	def sort(self,p=0,q=-100):
		if q == -100:
			yield from self.sort(0,self.size-1)
			return
		self.comparisons += 1
		if p == q:
			yield [[p,'g']]
		if p >= q:
			return
		piv = self.arr[q]
		idx = p
		for i in range(p,q):
			self.comparisons += 1
			if self.arr[i] < piv:
				self.swaps += 1
				self.arr[i],self.arr[idx] = self.arr[idx],self.arr[i]
				yield [[i,self.arr[i]],[idx,self.arr[idx]]]
				idx += 1
		self.swaps += 1
		self.arr[q],self.arr[idx] = self.arr[idx],self.arr[q]
		yield [[q,self.arr[q]],[idx,self.arr[idx]],[idx,'g']]
		yield from self.sort(p,idx-1)
		yield from self.sort(idx+1,q)

class InsertionSort(Algorithm):
	def __init__(self,size):
		super().__init__(size,'Insertion Sort')
	def sort(self):
		for i in range(1,len(self.arr)):
			piv = self.arr[i]
			j = i-1
			while j >= 0 and self.arr[j] > piv:
				self.comparisons += 2
				self.arr[j+1] = self.arr[j]
				self.swaps += 1
				yield [[j+1,self.arr[j+1]]]
				j -= 1
			self.arr[j+1] = piv
			self.swaps += 1
			yield [[j+1,piv]]
		for i in range(len(self.arr)):
			yield [[i,'g']]
class MergeSort(Algorithm):
	def __init__(self,size):
		super().__init__(size,'Merge Sort')
	def arr_sort(self):
		pass
class HeapSort(Algorithm):
	def __init__(self,size):
		super().__init__(size,'Heap Sort')
	def arr_sort(self):
		pass
class SelectionSort(Algorithm):
	def __init__(self,size):
		super().__init__(size,'Heap Sort')
	def arr_sort(self):
		pass
class CountingSort(Algorithm):
	def __init__(self,size):
		super().__init__(size,'Counting Sort')
	def arr_sort(self):
		pass