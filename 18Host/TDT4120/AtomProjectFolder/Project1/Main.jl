
import ImageProcessing
imp = ImageProcessing


function main()
	println("Starting")
	# img = imp.loadImg("res/mazes/maze10.png")
	@time img = imp.loadFloatImg("res/img2.png")
	kernel = reshape(Float32[
		1 0 0 0 0 0 0	0 0 0 0 0 0 1	0 0 0 0 0 0 1
		1 0 0 0 0 0 0	0 0 0 0 0 0 1	0 0 0 0 0 0 1
		1 0 0 0 0 0 0	0 0 0 0 0 0 1	0 0 0 0 0 0 1
		1 0 0 0 0 0 0	0 0 0 0 0 0 1	0 0 0 0 0 0 1
		1 0 0 0 0 0 0	0 0 0 0 0 0 1	0 0 0 0 0 0 1
		1 0 0 0 0 0 0	0 0 0 0 0 0 1	0 0 0 0 0 0 1
		1 0 0 0 0 0 0	0 0 0 0 0 0 1	0 0 0 0 0 0 1
	], (7, 7, 3))
	# kernel = Float32[
	# 	1 2 3 4 3 2 1;
	# 	2 3 4 5 4 3 2;
	# 	3 4 5 6 5 4 3;
	# 	4 5 6 7 6 5 4;
	# 	3 4 5 6 5 4 3;
	# 	2 3 4 5 4 3 2;
	# 	1 2 3 4 3 2 1
	# ]

	kernel[:, :, :] ./= sum(kernel[:, :, 2])
	# println(kernel[:, :, 1])
	# println(kernel[:])

	# @time imp.simple_gaussian!(img)
	# @time imp.grayscale!(img)
	@time imp.apply_kernel!(img, kernel)
	# @time img ./= sum(kernel[1, :, :])
	# @time img ./= sum(kernel)
	# img ./= sum(kernel[1, :, :])

	@time imp.writeImg("res/temp1.png", img)
end

main()

