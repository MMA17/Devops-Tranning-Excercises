from typing import List

def house(list: List[str], name: str) -> None:
    print("ten " + name + " du dieu kien duoc phep vao nha") 

def require(func) -> bool:
    list = ["manh", "duc", "quang", "huyen"]
    print ("Nhap ten: ")
    name = input()
    for x in list:
        if x == name:
            func(list, name)
            return True
    return False
