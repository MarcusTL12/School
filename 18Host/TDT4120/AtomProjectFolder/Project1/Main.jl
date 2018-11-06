
import ImageProcessing
imp = ImageProcessing


function main()
	println("Starting")
	# img = imp.loadImg("res/mazes/maze10.png")

	@time img = imp.loadFloatImg("res/img2.png")

	@time imp.simple_blur!(img)
	@time imp.sobell!(img)
	@time img = imp.loadFloatImg("res/PigBG.png")

	f(x, y) = sin(pi * x * y)^2

	# @time img[1, :, :] .= f.(img[1, :, :], 6 + 10)
	# @time img[2, :, :] .= f.(img[2, :, :], 100)
	# @time img[3, :, :] .= f.(img[3, :, :], 8 + 10)
	# img .= f.(img, 1)
	imp.sobell!(img)

	@time imp.writeImg("res/temp3.png", img)
end

main()

