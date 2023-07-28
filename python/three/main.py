from bird import Bird, Penguin
from mypackage import moudle1
b = Bird("big wings", "green feather");
b.fly()

del b.wings
# b.fly() 删除后不能再用
b.wings = "small wings"
b.fly() #重新赋值后才能使用

p = Penguin("small wings","villus");
p.fly()
p.run()
p.cry()
# p.__cry() 报错