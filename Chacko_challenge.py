Leg1 = input("Please Enter Side  A ") 
Leg2 = input("Please Enter Side  B ") 
Leg3= input("Please Enter Side  C ") 



legOneSq=int(Leg1) * int(Leg1)
legTwoSq=int(Leg2) * int(Leg2)
legThreeSq=int(Leg3) * int(Leg3)

Total_legOneandTwo = int(legOneSq)+int(legTwoSq)

if int(Leg1)+int(Leg2) < int(Leg3):
    print ('this is not a triangle')
elif Total_legOneandTwo == int(legThreeSq):
    print ('this is a right triangle')
elif Total_legOneandTwo < int(legThreeSq):
    print ('This is a Obtuse triangle')
elif Total_legOneandTwo > int(legThreeSq):
    print ("this is a acute triangle")
    