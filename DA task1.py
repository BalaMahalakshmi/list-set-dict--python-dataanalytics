my_list= [1,2,3,4,5]
my_list.append(6)
my_list.remove(3)
my_list[0]=8
print("updated list",my_list)

my_dict={'name':'bala','age':20,'city':'theni'}
my_dict['gender']='female'
del my_dict['age']
my_dict["city"]='coimbatore'
print("updated dictionary is",my_dict)


my_set={1,2,3,4,5}
my_set.add(8)
my_set.remove(3)
my_set.discard(1)
my_set.add(12)
print("updated set is",my_set)