from bird import Bird

b = Bird("big wings", "green feather");
b.fly()

del b.wings
# b.fly() 删除后不能再用
b.wings = "small wings"
b.fly() #重新赋值后才能使用