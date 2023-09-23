workoutFee = int(input())

basketballSneakers = workoutFee - 0.40 * workoutFee
basketballSuit = basketballSneakers - 0.20 * basketballSneakers
basketballBall = 0.25 * basketballSuit
basketballAcc = 0.20 * basketballBall

finalPrice=workoutFee+basketballSneakers+basketballSuit+basketballBall+basketballAcc
print(finalPrice)
