#program insertion sort

#fungsi insertion_sort

def insertion_sort(arr):
	#traverse dari 1 sampai len(arr)
	for i in range(1, len(arr)):
		key = arr[i]
		#print(key)
		# Pindahkan elemen arr[0...i-1], yang lebih besar
        # dari key, satu posisi ke kanan
        # dari posisi sekarang
		j = i-1
		#print(j)
		while j >= 0 and key < arr[j]:
			#print(arr[j])
			arr[j+1] = arr[j]
			#print(arr[j+1])
			j = j-1
			#print(j)
		arr[j+1] = key
		#print(arr[j+1])

#testing

# ar1 = [12,11,13,5,6]
# insertion_sort(ar1)
# print("Sorted Array: ")
# for i in range(len(ar1)):
# 	print(arr[i])

