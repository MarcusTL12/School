
mutable struct DisjointSetNode
    rank::Int
    p::DisjointSetNode
    DisjointSetNode() = (obj = new(0); obj.p = obj;)
end


findset(x::DisjointSetNode) = x == x.p ? x.p : x.p = findset(x.p)


function union!(x::DisjointSetNode, y::DisjointSetNode)
	xset = findset(x)
	yset = findset(y)
	if xset.rank > yset.rank
		yset.p = xset
		return
	elseif xset.rank == yset.rank
		yset.rank += 1
	end
	xset.p = yset
end


function hammingdistance(s1::String, s2::String)
	sum = 0
	for (i, j) in zip(s1, s2) sum += i == j ? 0 : 1 end
	return sum
end


function count_sets(nodes::Array{DisjointSetNode, 1})::Int
	sets::Array{DisjointSetNode, 1} = []
	for i in nodes
		if !(findset(i) in sets)
			push!(sets, findset(i))
		end
	end
	return length(sets)
end


function findclusters(E::Vector{Tuple{Int, Int, Int}}, n::Int, k::Int)
	edges_to_find::Int = length(E) - (k - 1)
	sort!(E)
	nodes::Array{DisjointSetNode, 1} = Array{DisjointSetNode, 1}(undef, n)
	for i in 1 : n
		nodes[i] = DisjointSetNode()
	end
	i = 1
	while count_sets(nodes) > k
		if findset(nodes[E[i][2]]) != findset(nodes[E[i][3]])
			union!(nodes[E[i][2]], nodes[E[i][3]])
		end
		i += 1
	end
	klusters::Dict{DisjointSetNode, Array{Int, 1}} = Dict()
	for i in 1 : n
		if !haskey(klusters, findset(nodes[i]))
			push!(klusters, findset(nodes[i]) => [i])
		else
			push!(klusters[findset(nodes[i])], i)
		end
	end
	return collect(values(klusters))
end


function findanimalgroups(animals::Vector{Tuple{String, String}}, k::Int64)
	E::Vector{Tuple{Int, Int, Int}} = []
	for i in 1 : length(animals)
		for j in i + 1 : length(animals)
			push!(E, (hammingdistance(animals[i][2], animals[j][2]), i, j))
		end
	end
	groups = findclusters(E, length(animals), k)
	animgroups::Array{Array{String, 1}, 1} = []
	for i in groups
		push!(animgroups, [])
		for j in i
			push!(animgroups[length(animgroups)], animals[j][1])
		end
	end
	return animgroups
end

