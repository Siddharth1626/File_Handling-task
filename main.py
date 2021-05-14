
def task1():
    i=0
    print("Task1")
    for x in range(10):
        print(f"Current no. {x}\t Previous no. {i}\t Sum {x+i}")
        i=x

def task2():
    list=[10,20,30,40,10]
    print("\nTask 2 ")
    if list[0]==list[-1]:
        print("True\n")

def task3():
    list = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    list[2][2].insert(2,7000)
    print("Task 3")
    print(list)

def task4():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    newdict = {}
    print("\nTask 4")
    for x in range(len(keys)):
        newdict = dict(zip(keys,values))
    #newdict.update({keys:values})
    print(newdict)

def task5():
    sampleDict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }
    print("\nTask 5")
    print(sampleDict['class']['student']['marks']['history'])


def file_handling():
    with open("C:\\Users\\Dell\\Downloads\\file1.txt", "r") as f1:
        d = f1.readlines()
    l = list()
    for x in d:
        key, value = x.split(":")
        a = {
            key: value.strip()
        }
        l.append(a)
    print(l)

    #print(list)

def file_handlingtask():
    try:
        f = open('C:\\Users\\Dell\\Downloads\\file1.txt','r')
        file = f.readlines()
        l=list()
        for x in file:
            (key, value) = x.split(':')
            a = {
                key : value.strip()
            }
            l.append(a)
        print(l)
    except NameError:
        print("Exception occurs")


task1()
task2()
task3()
task4()
task5()
file_handling()
file_handlingtask()