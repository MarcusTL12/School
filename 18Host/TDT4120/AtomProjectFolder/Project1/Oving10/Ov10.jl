

using DataStructures


mutable struct Node
    ip::Int
    neighbours::Array{Tuple{Node,Int}}
    risk::Union{Float64, Nothing}
    predecessor::Union{Node, Nothing}
    probability::Float64
end


function initialize_single_source!(graph, start)
	for n in graph
		n.risk = typemax(Float64)
	end
	start.risk = 0
end


function relax!(from_node, to_node, cost)
	risk = from_node.risk + (cost / to_node.probability)
	if to_node.risk > risk
		to_node.risk = risk
		to_node.predecessor = from_node
	end
end


function find_min!(ls::Array{Node, 1})::Node
	min = ls[1]
	index = 1
	for i in 1 : length(ls)
		if ls[i].risk < min.risk
			min = ls[i]
			index = i
		end
	end
	deleteat!(ls, i)
	return min
end


function find(ls::Array{Node, 1}, node)::Int
	for i in 1 : length(ls)
		if ls[i] == node
			return i
		end
	end
	return 0
end


function dijkstra!(graph, start)
	initialize_single_source!(graph, start)
	que::Array{Node, 1} = []
	for i in graph
		push!(que, i)
	end
	while length(que) > 0
		u = find_min!(que)
		for j in u.neighbours
			relax!(u, j[1], j[2])
		end
	end
end


function bellman_ford!(graph, start)
	initialize_single_source!(graph, start)

	for k in 1 : length(graph) - 1
		for i in graph
			for j in i.neighbours
				relax!(i, j[1], j[2])
			end
		end
	end
	for i in graph
		for j in i.neighbours
			if j[1].risk > i.risk + j[2]
				return false
			end
		end
	end
	return true
end

