#original dictionary 
data={'A':-10,'B':20,'C':-30,'D':40,'E':-50}
absolute_data={key:abs(value) for key,value in data.items()}
print("original dictionary:")
print(data)
print("\nAbsolute value dictionary:")
print(absolute_data)
    

