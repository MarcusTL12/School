function CinI(prompt::String="")::Int
	print(prompt)
	while true
		try
			return parse(Int, readline())
		catch
			println("Input not an integer; Try again:")
		end
	end
end

function CinF(prompt::String="")::Float64
	print(prompt)
	while true
		try
			return parse(Float64, readline())
		catch
			println("Input not a float; Try again:")
		end
	end
end