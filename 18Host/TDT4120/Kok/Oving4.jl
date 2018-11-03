function counting_sort_letters(A, position)
	c = Array{Int, 1}(undef, 26)
    for i in 1:26
        c[i] = 0
    end
	for i in A
        c[abs(Int(i[position]) - 97) % 26 + 1] += 1
	end
	for i in 2:26
		c[i] += c[i - 1]
	end
	ret = Array{String, 1}(undef, length(A))
	for i in length(A) : -1 : 1
        ret[c[abs(Int(A[i][position]) - 97) % 26 + 1]] = A[i]
        c[abs(Int(A[i][position]) - 97) % 26 + 1] -= 1
	end
	return ret
end

function counting_sort_length(A::Array)
	max_len = 0
	for i in A
		if max_len < length(i)
			max_len = length(i)
		end
	end
	c = Array{Int, 1}(undef, max_len + 1)
	for i in 1 : max_len + 1
		c[i] = 0
	end

	for i in A
		c[length(i) + 1] += 1
	end

	for i in 2 : max_len + 1
		c[i] += c[i - 1]
	end

	ret = Array{String, 1}(undef, length(A))

	for i in length(A) : -1 : 1
		ret[c[length(A[i]) + 1]] = A[i]
		c[length(A[i]) + 1] -= 1
	end
	return ret
end

function copy_into!(to, from, p, r)
	for i in p : r
		to[i] = from[i - p + 1]
	end
end


function flexradix(A::Array, max_len)
	A = counting_sort_length(A)

	num_empty = 0

	for i in A
		if length(i) == 0
			num_empty += 1
		end
		if max_len < length(i)
			max_len = length(i)
		end
	end

	if max_len == 0
		return A
	end

	c = zeros(Int, max_len + 1)

	for i in A
		c[length(i) + 1] += 1
	end

	for i in max_len : -1 : 1
		c[i] += c[i + 1]
	end

	r = length(A)
	
    for cur_len in (max_len + 1) : -1 : 2
		p = r - c[cur_len] + 1

		if r - p > 0
			copy_into!(A, counting_sort_letters(A[p : r], cur_len - 1), p, r)
		end
	end
	
	copy_into!(A, counting_sort_letters(A[(num_empty + 1) : r], 1), (num_empty + 1), r)

	return A
end
