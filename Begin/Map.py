feet= [128608.92408000001, 119750.65635, 122375.32826999998, 124015.74822]

feet = list(map(int, feet))

# Filter `feet` to only include uneven distances 
uneven = filter(lambda x: x%2, feet)
print(list(uneven))#[122375, 124015]