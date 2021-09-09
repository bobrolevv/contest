# id 52786854

def handman(data: str, finger: str) -> int:
    time_moments: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    fingers: int = int(finger)*2
    score: int = 0
    #
    for time in time_moments:
        res: int = 0
        for height in range(0, 4):
            for width in data[height]:
                if width.isdigit() and int(width) == int(time): res += 1
        if 0 < res <= fingers: score += 1
    return score

def main():
    finger: str = input()
    data: str = [input() for _ in range(4)]
    print(handman(data, finger))

if __name__ == '__main__':
    main()
