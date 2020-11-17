# Sorting-Visualizer
Visualizes sorting algorithms using pyplot/matplotlib and python.

Implemented algorithms: Quick sort, Merge Sort, Selection sort, Insertion sort, Bubble sort, Heap sort, Counting sort

To be implemented: Radix sort, Bucket sort, Pigeonhole Sort, Comb sort (and maybe more)

This visualizer uses matplotlib.animation.FuncAnimation in order to visually update the matplotlib bar graph. However, this makes the correlation between the time complexities of the sorting algorithms a bit random and misleading. For example, quick sort is by far faster than selection sort (nlogn vs n^2), but since many frames are passed into quick sort, while in selection sort only a few are, selection sort runs much faster due to the nature of FuncAnimation. There is not exactly a good or efficient way to fix this problem in matplotlib, so it is best to compare the speeds of each algorithm based roughly on the number of swaps and comparisons.
