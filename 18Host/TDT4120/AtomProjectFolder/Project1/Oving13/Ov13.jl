

certifysubsetsum(subsetindices, set, sum_) = maximum(subsetindices) <= length(set) && sum([set[i] for i in subsetindices]) == sum_


function certifysubsetsum_long(subsetindices, set, sum_)
	s = 0
	for i in subsetindices
		if i > length(set)
			return false
		end
		s += set[i]
	end
	return s == sum_
end


function certifytsp(path, maxweight)

