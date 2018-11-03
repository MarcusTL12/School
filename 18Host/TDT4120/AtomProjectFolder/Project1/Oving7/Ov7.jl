

function can_use_greedy(coins::Array{Int, 1})::Bool
	divisible::Bool = true
	for i in 1 : length(coins) - 1
		divisible &= (coins[i] % coins[i + 1]) == 0
	end

	return divisible
end


function min_coins_greedy(coins::Array{Int, 1}, value::Int)::Int
	amt_coins::Int = 0

	for i in coins
		amt_coins += fld(value, i)
		value %= i
	end

	return amt_coins
end


function min_coins_dynamic(coins::Array{Int, 1}, value::Int)::Int
	amt_coins = fld(value, coins[length(coins)])

	for i in length(coins) : -1 : 1
		temp = min_coins_greedy(coins[i : length(coins)], value)
		if temp < amt_coins
			amt_coins = temp
		end
	end

	return amt_coins
end
