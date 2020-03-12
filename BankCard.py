#Create Credit card number
bankcard = (4,3,1,9,7,3,9,8,7,1,4,2,3,4,5,6)

#Multiply every second digit by 2
second = (bankcard[1] * 2)
fourth = (bankcard[3] * 2)
sixth = (bankcard[5] * 2)
eight = (bankcard[7] * 2)
ten = (bankcard[9] * 2)
twelve = (bankcard[11] * 2)
fourteen = (bankcard[13] * 2)
sixteen = (bankcard[15] * 2)


#prints bankcard
print(bankcard)
print(eight)

#Mods every second digit by 10 if its above 10
if second > 10:
 second = second % 10

if fourth > 10:
 fourth = fourth % 10

if sixth > 10:
 sixth = sixth % 10

if eight > 10:
 eight = eight % 10

if ten > 10:
 ten = ten % 10

 if twelve > 10:
  twelve = twelve % 10

 if fourteen > 10:
  fourteen = fourteen % 10

 if sixteen > 10:
  sixteen = sixteen % 10

#Sums up all digits
sum = (bankcard[0] + second + bankcard[2] + fourth + bankcard[4] + sixth + bankcard[6] + eight + bankcard[8] + ten + bankcard[10] + twelve + bankcard[12]) + fourteen + bankcard[14] + sixteen

#prints sum of all digits
print(sum)
sum = sum + 8


print('**************MODE:1******************')
#checks if card is legit or not
if  (sum) % 10 == 0:
 print('Card is legit')
else:
 print('Card is not legit')

print('**************MODE:2******************')
 #Checks vendor of the card
if bankcard[0] == 4 and bankcard[1] == 3 and bankcard[2] == 1 and bankcard[3] == 9:
 print('This card is a visa')
if bankcard[0] == 6 and bankcard[1] == 3 and bankcard[2] == 0 and bankcard[3] == 4:
 print('This card is Laser')
if bankcard[0] == 5 and bankcard[1] == 0:
 print('This card is a Maestro')
if bankcard[0] == 6 and bankcard[1] == 3 and bankcard[2] == 3 and bankcard[3] == 4:
 print('This card is Solo')

#sum = sum + 8
#print(sum)


#while (sum % 10) != 0:
# new9 = bankcard[10] + 1
# new9 = bankcard[10]
#1 print(bankcard[10])

 #sum = sum + (bankcard[9])



#if sum % 10 == 0:
# print fullcard






