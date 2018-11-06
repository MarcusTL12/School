
import ImageProcessing
imp = ImageProcessing


function main()
	println("Starting")
	# img = imp.loadImg("res/mazes/maze10.png")
	@time img = imp.loadFloatImg("res/img2.png")

	@time imp.simple_blur!(img)
	@time imp.sobell!(img)

	@time imp.writeImg("res/temp1.png", img)
end

main()

