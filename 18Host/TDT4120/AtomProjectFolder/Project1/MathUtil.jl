function log_taylor(x::Number)
    if x <= 0
        return undef
    end

    e = float(Base.MathConstants.e)
    lb = 0.546
    ub = lb * e

    res = 0

    while x < lb
        x *= e
        res -= 1
    end

    while x > ub
        x /= e
        res += 1
    end

    s = 1

    for i in 1 : 40
        res += s * (x - 1)^i / i
        s *= -1
    end

    return res
end
