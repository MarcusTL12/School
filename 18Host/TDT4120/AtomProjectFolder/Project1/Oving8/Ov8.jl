

using DataStructures


mutable struct Node
    id::Int
    neighbours::Array{Node}
    color::Union{String, Nothing}
    distance::Union{Int, Nothing}
    predecessor::Union{Node, Nothing}
end
Node(id) = Node(id, [], nothing, nothing, nothing)


function makenodelist(adjlist::Array)::Array{Node, 1}
	ret::Array{Node, 1} = Array{Node, 1}(undef, length(adjlist))

	for i in 1 : length(adjlist)
		ret[i] = Node(i)
	end

	for i in 1 : length(adjlist)
		for j in adjlist[i]
			push!(ret[i].neighbours, ret[j])
		end
	end

	return ret
end


function isgoalnode(node::Node)::Bool
	return node.id == 8
end


function bfs!(nodes::Array{Node, 1}, start::Node)::Union{Node, Nothing}
	que::Queue{Node} = Queue{Node}()
	
	for i in nodes
		i.color = "white"
	end

	enqueue!(que, start)
	start.color = "gray"
	start.distance = 0

	while length(que) > 0
		cur_node = dequeue!(que)
		if cur_node.predecessor != nothing
			cur_node.distance = cur_node.predecessor.distance + 1
		end

		if isgoalnode(cur_node)
			return cur_node
		end

		for i in cur_node.neighbours
			if i.color == "white"
				enqueue!(que, i)
				i.predecessor = cur_node
				i.color = "gray"
			end
		end

		cur_node.color = "black"
	end

	return nothing
end


function makepathto(goalnode::Node)::Array{Int, 1}
	ret::Array{Int, 1} = [goalnode.id]

	while goalnode.predecessor != nothing
		goalnode = goalnode.predecessor
		push!(ret, goalnode.id)
	end
	reverse!(ret)
	return ret
end

