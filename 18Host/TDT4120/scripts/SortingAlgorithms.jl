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

function quicksort!(data::Array, start=-1, stop=-1, lowest=-1, highest=-1)
	if start == -1
		start = 1
		stop = length(data)
		pivot = 0
		lowest = data[1]
		highest = data[1]
		for i in 2 : stop
			if data[i] < lowest
				lowest = data[i]
			end
			if data[i] > highest
				highest = data[i]
			end
		end
	end
	
	pivot = (highest + lowest) / 2
	
#=	print(start)
	print(", ")
	print(stop)
	print(", ")
	print(pivot)
	print(", ")
	print(lowest)
	print(", ")
	println(highest)
=#	
	if highest == lowest
		return
	end
	
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
#			println(data)
			return
		end
		
		if stop - start == 1
			if data[start] > data[start + 1]
				buffer = data[start]
				data[start] = data[start + 1]
				data[start + 1] = buffer
			end
#			println(data)
			return
		end
		
		if stop - start == 0
			return
		end
	end
	
	leftPointer = start
	rightPointer = stop
	
	leftHighest = lowest
	rightLowest = highest
	
	done = false
	
	while !done
#=		print(leftPointer)
		print(", ")
		println(rightPointer)
=#	
		checkForLeftExtreme = false
		checkForRightExtreme = false
	
		left = data[leftPointer] <= pivot
		right = data[rightPointer] > pivot
		
		if rightPointer - leftPointer <= 0
			done = true
		elseif !left && !right
			buffer = data[leftPointer]
			data[leftPointer] = data[rightPointer]
			data[rightPointer] = buffer
			if rightPointer - leftPointer > 1
				checkForLeftExtreme = true
				checkForRightExtreme = true
				leftPointer += 1
				rightPointer -= 1
			else
				done = true
				if data[leftPointer] > leftHighest
					leftHighest = data[leftPointer]
				end
				if data[rightPointer] < rightLowest
					rightLowest = data[rightPointer]
				end
			end
		elseif !left && right
			rightPointer -= 1
			checkForRightExtreme = true
		elseif left && !right
			leftPointer += 1
			checkForLeftExtreme = true
		elseif rightPointer - leftPointer > 1
			leftPointer += 1
			rightPointer -= 1
			checkForLeftExtreme = true
			checkForRightExtreme = true
		else
			done = true
		end
		
		if checkForLeftExtreme
			if data[leftPointer - 1] > leftHighest
				leftHighest = data[leftPointer - 1]
			end
		end
		if checkForRightExtreme
			if data[rightPointer + 1] < rightLowest
				rightLowest = data[rightPointer + 1]
			end
		end
		
#		println(data)
	end
	
	pivotPointer = leftPointer
	
	if leftPointer == rightPointer
		if data[leftPointer] > pivot
			pivotPointer -= 1
			if data[leftPointer] < rightLowest
				rightLowest = data[leftPointer]
			end
		else
			if data[leftPointer] > leftHighest
				leftHighest = data[leftPointer]
			end
		end
	else
		if data[leftPointer] > leftHighest
			leftHighest = data[leftPointer]
		end
		if data[rightPointer] < rightLowest
			rightLowest = data[rightPointer]
		end
	end
	
	quicksort!(data, start, pivotPointer, lowest, leftHighest)
	quicksort!(data, pivotPointer + 1, stop, rightLowest, highest)
end
