

include("Oving12/Ov12.jl")


function main()
	# c::Matrix{Float64} = [
	# 	0	13	13	0	0	0	;
	# 	0	0	0	14	0	0	;
	# 	0	4	0	9	5	0	;
	# 	0	0	0	0	0	4	;
	# 	0	0	0	7	0	20	;
	# 	0	0	0	0	0	0
	# ]
	
	c::Matrix{Float64} = [
		0	13	13	0	0	0	;
		-13	0	-4	14	0	0	;
		-13	4	0	9	12	0	;
		0	-14	-9	0	-7	4	;
		0	0	-12	7	0	20	;
		0	0	0	-4	-20	0
	]

	println(max_flow(1, 6, 6, c))
end

main()

