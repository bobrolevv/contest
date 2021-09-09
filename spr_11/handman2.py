# id 52787623

def handman(data: str, finger: str) -> int:
    time_moments: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    fingers: int = int(finger)*2
    score: int = 0
    for time in time_moments:
        res = find_t(data, str(time))
        if 0 < res <= fingers: score += 1
    return score

def find_t(data: list, symb: str) -> int:
    start: int = -1
    count: int = 0
    for string in data:
        while True:
            start = string.find(symb, start + 1)
            if start == -1:
                break
            count += 1
    return count

def main():
    finger: str = input()
    data: str = [input() for _ in range(4)]
    print(handman(data, finger))
    print(find_t(data, "1"))

if __name__ == '__main__':
    main()
