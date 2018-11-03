function f()
    a::Float64 = 0
    s = 1

    println("start")
    for i in 1:10000000000
        a += 1 / (2 * i - 1) * s
        s *= -1
    end

    println(a * 4)
end

f()
