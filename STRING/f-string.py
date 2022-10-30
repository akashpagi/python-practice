# f-string :
# ex. 1
print('***** integer ******')
a=10
b=20
value=f'{a}'
print(f"{a}")
print(f"{a}    {b}")
print(f"{b} {a}")
print(value)
print()

print('***** float ******')
c=10.87
d=20.93
print(f"{c}")
print(f"{c} {d}")
print(f"{d} {c}")
print()

print('***** string ******')
f_name='akash'
l_name='pagi'
print(f"{f_name}")
print(f"{f_name} {l_name}")
print(f"{l_name} {f_name}")
print()


print('***** integer and string ******')
name='akash'
age=18
print(f"my name is {name}")
print(f"{name} {age}")
print(f"{age}    {name}")
print()

print('>>>>>>>> integer <<<<<<<<<')
num=20
print(f'{num:5d}') # [width]type
print(f'{num:05d}') # [0](padding)[width]type
print(f'{num:+5d}') # [sign](+,-,'space')[width]type
# if (+)(+)=(+),  (-)(-)=(-),  (-)(+)=(-),   (+)(-)=(+)
print(f'{num:<5d}') # [left align][width]type
print(f'{num:*>5d}') # [fill][right align][width]type
print(f'{num:*^5d}') # [fill][center align][width]type
print()

print('>>>>>>>> float <<<<<<<<<')
f=15.45
print(f'{f}')
print(f'{f:8f}') # [width]type
print(f'{f:010.2f}') # [0](padding)[width][.precision]type
print(f'{f:+8.3f}') # [sign](+,-,'space')[width][.precision]type
# if (+)(+)=(+),  (-)(-)=(-),  (-)(+)=(-),   (+)(-)=(+)
print(f'{f:<8.2f}') # [left align][width][.precision]type
print(f'{f:*>8.2f}') # [fill][right align][width][.precision]type
print(f'{f:*^8.2f}') # [fill][center align][width][.precision]type
print()


