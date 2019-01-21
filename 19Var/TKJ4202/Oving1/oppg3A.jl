using Plots
R = 0.0821
T = 298
isoterm(x) = R * T / x
v = 5 : -0.1 : 2.5
p = isoterm.(v)
plot(xlabel = "V[L]", ylabel = "P[atm]", xlims = xlims = (0, 7),
		ylims = ylims = (0, 14),
		xticks = 0 : 0.5 : xlims[2], yticks = 0 : 1 : ylims[2])
plot!(v, p;
		color = :red, label = "A: Trinn 1", arrow = :arrow, linewidth = 2)
plot!([v[end], v[end]], [p[end], p[1]];
		color = :blue, label = "A: Trinn 2", arrow = :arrow, linewidth = 2)
plot!([v[1], v[end]], [p[1], p[1]];
		color = :green, label = "B: Trinn 1", arrow = :arrow, linewidth = 2)
#
