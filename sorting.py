import random
import time

class Algorithm:
	def __init__(self,size,name):
		self.name = name
		self.size = size
		self.max_num = self.size
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
	def sort(self,p=0,q=None):
		if q == None:
			q = self.size-1
		if p == q:
			return
		piv = (p+q)//2
		yield from self.sort(p,piv)
		yield from self.sort(piv+1,q)
		left_list = self.arr[p:piv+1]
		right_list = self.arr[piv+1:q+1]
		count = p
		while left_list and right_list:
			self.comparisons += 1
			self.swaps += 1
			if left_list[0] < right_list[0]:
				self.arr[count] = left_list.pop(0)
				yield [[count,self.arr[count]]]
			else:
				self.arr[count] = right_list.pop(0)
				yield [[count,self.arr[count]]]
			count += 1
		if not left_list:
			self.arr[count:q+1] = right_list
			yield [[i,self.arr[i]] for i in range(count,q+1)]
		else:
			self.arr[count:q+1] = left_list
			yield [[i,self.arr[i]] for i in range(count,q+1)]
		if p == 0 and q == self.size-1:
			for i in range(len(self.arr)):
				yield [[i,'g']]

class HeapSort(Algorithm):
	def __init__(self,size):
		super().__init__(size,'Heap Sort')
	def sort(self):
		for i in range(self.size//2,-1,-1):
			yield from self.heapify(self.size,i)
		for i in range(self.size-1,0,-1):
			self.arr[i],self.arr[0] = self.arr[0],self.arr[i]
			self.swaps += 1
			yield [[i,self.arr[i]],[0,self.arr[0]]]
			yield from self.heapify(i,0)
		for i in range(self.size):
			yield [[i,'g']]
	def heapify(self,size,idx):
		largest = idx
		left = 2*idx+1
		right = 2*idx+2
		self.comparisons += 3
		if left < size and self.arr[left] > self.arr[largest]:
			largest = left
		if right < size and self.arr[right] > self.arr[largest]:
			largest = right
		if largest != idx:
			self.swaps += 1
			self.arr[idx],self.arr[largest] = self.arr[largest],self.arr[idx]
			yield [[idx,self.arr[idx]],[largest,self.arr[largest]]]
			yield from self.heapify(size,largest)
class SelectionSort(Algorithm):
	def __init__(self,size):
		super().__init__(size,'Selection Sort')
	def sort(self):
		for i in range(self.size):
			min_idx = i
			for j in range(i+1,self.size):
				self.comparisons += 1
				if self.arr[j] < self.arr[min_idx]:
					min_idx = j
			self.swaps += 1
			self.arr[min_idx],self.arr[i] = self.arr[i],self.arr[min_idx]
			#SelectionSort moves extremely quickly due to the nature that it's all computational and not many frames, so I separated it into 3 portions to slow it down a bit.
			yield [[i,self.arr[i]]]
			yield [[min_idx,self.arr[min_idx]]]
			yield [[i,'g']]
class CountingSort(Algorithm): #special type of sort, time complexity does not correspond to swap/comparisons and such
	def __init__(self,size):
		super().__init__(size,'Counting Sort -- note that time complexity O(n+k) does not correspond to swaps and comparisons')
	def sort(self):
		counts = [0 for _ in range(self.max_num+1)]
		for i in self.arr:
			counts[i] += 1
		before = 0
		for i, count in enumerate(counts):
			counts[i] = before
			before += count
		#for i in range(1,len(counts)):
			#counts[i] += counts[i-1]
		copy = self.arr[:]
		for i in copy:
			self.arr[counts[i]] = i
			self.swaps += 1
			yield [[counts[i],i],[counts[i],'g']]
			counts[i] += 1
class RadixSort(Algorithm):
	def __init__(self,size):
		super().__init__(size,'Radix Sort')
	def sort(self):
		pass
class BucketSort(Algorithm):
	def __init__(self,size):
		super().__init__(size,'Bucket Sort')
	def sort(self):
		pass
class PigeonholeSort(Algorithm):
	def __init__(self,size):
		super().__init__(size,'Pigeonhole Sort')
	def sort(self):
		pass
class CombSort(Algorithm):
	def __init__(self,size):
		super().__init__(size,'Comb Sort')
	def sort(self):
		new_gap = lambda g: max(1,int(g*10/13))
		gap = self.size
		swap = True
		self.comparisons += 2
		while gap > 1 or swap:
			self.comparisons += 2
			gap = new_gap(gap)
			swap = False
			for i in range(0,self.size-gap):
				self.comparisons += 1
				if self.arr[i] > self.arr[i+gap]:
					self.arr[i],self.arr[i+gap] = self.arr[i+gap],self.arr[i]
					self.swaps += 1
					swap = True
					yield [[i,self.arr[i]],[i+gap,self.arr[i+gap]]]
		for i in range(self.size):
			yield [[i,'g']]