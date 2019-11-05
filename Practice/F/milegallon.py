#miles per gallon
numGall =input(" how many gallons of gas can your car hold?")
NumDriv = input(" how many miles do you get on a full tank?")
#process
MilesperGallon = float(numGall) / float(NumDriv)

print("Your car gets " + str(MilesperGallon) + " miles per gallon.")