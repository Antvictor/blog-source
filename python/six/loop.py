import random;
runNumber = 0;
while runNumber < 10:
    runNumber+=1;
    print(f"这是第{runNumber}圈");


boxs = ["1",2,"3",4];

# for i in boxs:
#     print(i);
#     boxs.remove(i);

# print(boxs);

boxes = [];
for i in range(random.randint(0,10)):
    boxes.append(i);
print(boxes)

for i in boxes:
    print(i);


def test(s, ss, *sss):
    print(s)

test("s","ss")

for i in range(3,10,2):
    print(i);



boxes = [1,2,3,4,5,6];
for i in boxes:
    if (i == 3):
        break;
    print(i); 

boxes = [1,2,3,4,5,6];
for i in boxes:
    if (i == 3):
        continue;
    print(i);