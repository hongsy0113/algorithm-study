import random
if __name__ == '__main__':

    print(50)
    for _ in range(50):
        print(20)

        for i in range(20):
            for j in range(20):
                value = random.randint(1, 100)
                print(value, end=' ')
            print()

