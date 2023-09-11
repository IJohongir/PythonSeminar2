def make_list(number):
    make_list.names = [input("name") for _ in range(number)]
    print(make_list.names)
    
number = int(input("How much"))
make_list(number)
for name in make_list.names:
    if name[0] =="А":
        print("f", name, "g")