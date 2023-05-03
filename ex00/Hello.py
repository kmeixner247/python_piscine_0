ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"

tmp_list = list(ft_tuple)
tmp_list[1] = "Germany!"
ft_tuple = tuple(tmp_list)
# ft_tuple = (ft_list[0], "Germany!")

ft_set.discard("tutu!")
ft_set.add("Wolfsburg!")

ft_dict["Hello"] = "42Wolfsburg!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
