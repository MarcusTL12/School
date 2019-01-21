using Plots
R = 0.0821
T = 243.6
isoterm(x) = R * T / x
v = 1 : 0.1 : 10
p = isoterm.(v)
plot(xlabel = "V[L]", ylabel = "P[atm]", xlims = (0, 15), ylims = (0, 25),
		xticks = 0 : 1 : 15, yticks = 0 : 2 : 25)
plot!(reverse(v), reverse(p);
		color = :red, label = "Trinn 1", arrow = :arrow, linewidth = 2)
plot!([1, 10], [20, 20];
		color = :blue, label = "Trinn 2", arrow = :arrow, linewidth = 2)
plot!([10, 10], [20, 2];
		color = "#007f00", label = "Trinn 3", arrow = :arrow, linewidth = 2)
#
