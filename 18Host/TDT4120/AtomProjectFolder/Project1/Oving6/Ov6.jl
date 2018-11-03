

function cumulative(weights::Array{Int, 2})
	ret = copy(weights)
	dim = size(weights)
	for i in 2 : dim[1]
		for j in 1 : dim[2]
			min = ret[i - 1, j]
			if j > 1 && ret[i - 1, j - 1] < min
				min = ret[i - 1, j - 1]
			end
			if j < dim[2] && ret[i - 1, j + 1] < min
				min = ret[i - 1, j + 1]
			end
			ret[i, j] += min
		end
	end
	return ret
end


function back_track(weights::Array{Int, 2})
	dim = size(weights)

	buffer::Array{Int, 1} = ones(Int, dim[1])

	buffer[1] = 1
	for i in 2 : dim[2]
		if weights[dim[1], i] < weights[dim[1], buffer[1]]
			buffer[1] = i
		end
	end

	for i in dim[1] - 1 : -1 : 1
		k = dim[1] - i + 1
		j = buffer[k - 1]
		buffer[k] = j
		if j > 1 && weights[i, j - 1] < weights[i, buffer[k]]
			buffer[k] = j - 1
		end
		if j < dim[2] && weights[i, j + 1] < weights[i, buffer[k]]
			buffer[k] = j + 1
		end
	end

	ret::Array{Tuple{Int, Int}, 1} = Array{Tuple{Int, Int}, 1}(undef, dim[1])
	
	for i in 1 : dim[1]
		ret[i] = dim[1] - i + 1, buffer[i]
	end
	
	return ret
end
