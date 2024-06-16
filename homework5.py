immutable_var = (8,9,"x","y",["z"])
print(type(immutable_var))
print(immutable_var)
immutable_var [4][0] = "c"
print(immutable_var)
mutable_list = [10,11,"j","k"]
print(type(mutable_list))
print(mutable_list)
mutable_list [0] = 9999
print(mutable_list)