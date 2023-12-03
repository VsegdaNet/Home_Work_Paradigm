# Я выбрал Императивный подход потому что я могу управлять так как мне надо
# состоянием программы

def sum(num):
    for i in range(1, num + 1):
        for j in range(1, 11):
            print(f"{i} * {j} = {i * j}", end=' || ')
        print('\n')


if __name__ == "__main__":
    sum(8)
