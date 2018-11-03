function insertionsort!(data::Array{Int64})
	for i in 2 : length(data)
		current_value = data[i]
		for j in i - 1 : -1 : 1
			if current_value < data[j]
				data[j + 1] = data[j]
				if j == 1
					data[j] = current_value
				end
			else
				data[j + 1] = current_value
				break
			end
		end
	end
end

function builtinsort!(data::Array{Int64})
	sort!(data)
end

function quicksort!(data::Array, start=-1, stop=-1, pivot=-1)
	if start == -1
		start = 1
		stop = length(data)
		pivot = 0
		for i in data
			pivot += i
		end
		pivot = pivot / stop
	end
	
	print(start)
	print(", ")
	print(stop)
	print(", ")
	println(pivot)
	
	if stop - start <= 2
		if stop - start == 2
			if data[start] > data[start + 1]
				buffer = data[start]
				data[start] = data[start + 1]
				data[start + 1] = buffer
			end
			if data[start + 1] > data[start + 2]
				buffer = data[start + 1]
				data[start + 1] = data[start + 2]
				data[start + 2] = buffer
			end
			if data[start] > data[start + 1]
				buffer = data[start]
				data[start] = data[start + 1]
				data[start + 1] = buffer
			end
			println(data)
			return
		end
		
		if stop - start == 1
			if data[start] > data[start + 1]
				buffer = data[start]
				data[start] = data[start + 1]
				data[start + 1] = buffer
			end
			println(data)
			return
		end
		
		if stop - start == 0
			return
		end
	end
	
	leftPointer = start
	rightPointer = stop
	
	done = false
	
	while !done
		print(leftPointer)
		print(", ")
		println(rightPointer)
	
		left = data[leftPointer] <= pivot
		right = data[rightPointer] > pivot
		
		if rightPointer - leftPointer <= 0
			done = true
		elseif !left && !right
			buffer = data[leftPointer]
			data[leftPointer] = data[rightPointer]
			data[rightPointer] = buffer
			if rightPointer - leftPointer > 1
				leftPointer += 1
				rightPointer -= 1
			else
				done = true
			end
		elseif !left && right
			rightPointer -= 1
		elseif left && !right
			leftPointer += 1
		elseif rightPointer - leftPointer > 1
			leftPointer += 1
			rightPointer -= 1
		else
			done = true
		end
		println(data)
	end
	
	pivotPointer = leftPointer
	
	if leftPointer == rightPointer && data[leftPointer] > pivot
		pivotPointer -= 1
	end
	
	quicksort!(data, start, pivotPointer, pivot / 2)
	quicksort!(data, pivotPointer + 1, stop, pivot * 3 / 2)
end
