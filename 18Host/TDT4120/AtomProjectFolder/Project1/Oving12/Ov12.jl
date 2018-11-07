
using DataStructures


function find_augmenting_path(source::Int, sink::Int, nodes::Int, flows::Matrix{Number}, capacities::Matrix{Number})::Union{Vector{Int}, Nothing}
	function create_path(source::Int, sink::Int, parent::Int)::Vector{Int}
		# creates a path from source to sink using parent list
		node = sink
		path = Vector{Int}([sink])
		while node ≠ source
			node = parent[node]
			push!(path, node)
		end
		return reverse(path)
	end

	discovered = zeros(Bool, nodes)
	parent = zeros(Int, nodes)
	queue = Queue{Int}()
	enqueue!(queue, source)

	# BFS to find augmenting path, while keeping track of parent nodes
	while !isempty(queue)
		node = dequeue!(queue)
		if node == sink
			return create_path(source, sink, parent)
		end

		for neighbour ∈ 1:nodes
			if !discovered[neighbour] && flows[node, neighbour] < capacities[node, neighbour]
				enqueue!(queue, neighbour)
				discovered[neighbour] = true
				parent[neighbour] = node
			end
		end
	end

	return nothing # no augmenting path found
end
  
function max_path_flow(path::Vector{Int}, flows::Matrix{Number}, capacities::Matrix{Number})::Number
	# find max flow to send through a path
	n = length(path)
	flow = Inf
	for i in 2 : n
		u, v = path[i - 1], path[i]
		flow = min(flow, capacities[u, v] - flows[u, v])
	end
	return flow
end
  
function send_flow!(path::Vector{Int}, flow::Number, flows::Matrix{Number})
	n = length(path)
	for i in 2 : n
		u, v = path[i - 1], path[i]
		flows[u, v] += flow
		flows[v, u] -= flow
	end
end


function max_flow(source, sink, nodes, capacities)
	flows = zeros()
end


