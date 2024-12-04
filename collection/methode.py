arr=[100,200,300,400,500,600,700,800]

odd_position_number=[num for index,num in enumerate(arr) if index%2!=0]

odd_position_number.reverse()

print(odd_position_number)