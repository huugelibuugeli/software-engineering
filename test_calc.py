from calc import add, sub

def test_add():
    print("\ntesting add...")
    assert add(2,3) == 5

def test_sub():
    print("\ntesting sub...")
    assert sub(4,3) == 1

if __name__ == "__main__":
    test_add()
    test_sub()
    print("done.")