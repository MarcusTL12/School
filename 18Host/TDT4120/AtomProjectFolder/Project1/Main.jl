
using SpecialFunctions

function main()
	a::BigFloat = BigFloat(pi, Int(1073741824 / 2))
	s = string(a)
	io = open("C:/Dev/test.txt", "w")
	write(io, s)
	close(io)
end

main()

