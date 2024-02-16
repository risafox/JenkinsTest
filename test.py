import main

def test_add():
    assert(main.add(3, 5), 8)
    assert(main.add(0, 0), 0)

if __name__ == "__main__":
    print("hello from test")
    test_add()
