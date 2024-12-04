#original dictionary data
data={'A':30,'B':75,'C':20,'D':60,'E':90,'E':90,'F':40}

filtered_data={key:value for key,value in data.items() if value>50}
print("original dictionary:")
print(data)
print("\nfiltered dictionary:")
print(filtered_data)                          
