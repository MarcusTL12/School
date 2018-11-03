#include("ConsoleUtil.jl")
include("SortingAlgorithms.jl")

data = [1, 10, 4, 1, 10, 9, 9, 7, 7, 6]

println(data)

quicksort!(data)

println(data)
