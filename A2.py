Amount =int(input("Please Enter Amount for Withdraw"))

note_500 = Amount//500

note_100= (Amount%500)//100

note_50= ((Amount%500)%100)//50

print( "Notes of 500 rupee=", note_500)
print( "Notes of 100 ruppee=", note_100)
print( "notes of 50 rupee=", note_50)