

function floyd_warshall(d, n, f, g)
	for k in 1 : n
		for i in 1 : n
			for j in 1 : n
				d[i, j] = f(d[i, j], g(d[i, k], d[k, j]))
			end
		end
	end
	return d
end


function transitive_closure(d, n)
	d .= reshape([i < Inf ? 1 : 0 for i in d], (n, n))
	or(a, b) = (a != 0 || b != 0) ? 1 : 0
	and(a, b) = (a != 0 && b != 0) ? 1 : 0
	return floyd_warshall(d, n, or, and)
end


function create_preference_matrix(b, v, c)
	ind(c)::Int = c - 'A' + 1
	chk_list::Array{Bool, 1} = Array{Bool, 1}(undef, c)
	ret::Array{Int, 2} = fill(0, c, c)
	for i in b
		fill!(chk_list, false)
		for j in i
			chk_list[ind(j)] = true
			for k in 1 : c
				if !chk_list[k]
					ret[ind(j), k] += 1
				end
			end
		end
	end
	return ret
end


function find_strongest_paths(p, c)
	for i in 1 : c - 1
		for j in i + 1 : c
			if p[i, j] < p[j, i]
				p[i, j] = 0
			else
				p[j, i] = 0
			end
		end
	end
	floyd_warshall(p, c, max, min)
	for i in 1 : c
		p[i, i] = 0
	end
	return p
end


find_schulze_ranking(sp, c) = String([i[2] for i in sort([(sum([sp[j, i] > sp[i, j] ? 0 : 1 for i in 1 : c]), Char(j + 64)) for j in 1 : c])])

