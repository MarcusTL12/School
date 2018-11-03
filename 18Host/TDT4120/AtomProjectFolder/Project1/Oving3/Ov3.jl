function bisect_left(A, p, r, v)
	i = p
	if p < r
	   q = floor(Int, (p + r) / 2)
	   if v <= A[q]
		   i = bisect_left(A, p, q, v)
	   else
		   i = bisect_left(A, q + 1, r, v)
	   end
	end
	return i
end


function bisect_right(A, p, r, v)
	i = p
	if p < r
	   q = floor(Int, (p + r) / 2)
	   if v < A[q]
		   i = bisect_right(A, p, q, v)
	   else
		   i = bisect_right(A, q + 1, r, v)
	   end
	end
	return i
end


function find_median(a, low, upp)
	i_low = bisect_left(a, 1, length(a) + 1, low)
	i_upp = bisect_right(a, 1, length(a) + 1, upp)

	mid = floor(Int, (i_upp + i_low) / 2)
	if (i_upp - i_low) % 2 == 0
		return (a[mid] + a[mid - 1]) / 2
	else
		return a[mid]
	end
end
