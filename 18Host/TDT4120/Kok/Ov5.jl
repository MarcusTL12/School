

struct Node
    children::Dict{Char,Node}
    posi::Array{Int}
end


function parse_string(sentence::String)::Array{Tuple{String,Int}}
	ret::Array{Tuple{String,Int}, 1} = []

	done = false

	i::Int = 1
	while !done
		if sentence[i] != ' '
			stop = i + 1
			while stop <= length(sentence) && sentence[stop] != ' '
				stop += 1
			end
			push!(ret, (sentence[i:stop - 1], i))
			i = stop + 1
		else
			i += 1
		end

		if i > length(sentence)
			done = true
		end
	end

	return ret
end


function build(list_of_words::Array{Tuple{String,Int}})::Node
	top::Node = Node(Dict([]), [])

	for i in list_of_words
		cur_node = top
		
		for j in i[1]
			if !haskey(cur_node.children, j)
				push!(cur_node.children, j => Node(Dict([]), []))
			end

			cur_node = cur_node.children[j]
		end

		push!(cur_node.posi, i[2])
	end
	
	return top
end


function positions(word::String, node::Node, index::Int=1)::Array{Int}
	indices::Array{Int, 1} = []

	if index > length(word)
		return indices
	elseif index == length(word)
		if word[index] != '?'
			if haskey(node.children, word[index])
				append!(indices, node.children[word[index]].posi)
			end
		else
			for i in node.children
				append!(indices, i[2].posi)
			end
		end
		return indices
	end

	if word[index] == '?'
		for i in node.children
			append!(indices, positions(word, i[2], index + 1))
		end
	elseif haskey(node.children, word[index])
		append!(indices, positions(word, node.children[word[index]], index + 1))
	end

	return indices
end
