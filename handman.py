# id 52688587

def handman(data):
    time_moments = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    fingers = int(data[0])*2
    score = 0
    for time in time_moments:
        res = 0
        for height in range(1, 5):
            for width in data[height]:
                if width.isdigit() and int(width) == int(time): res += 1
        if 0 < res <= fingers: score += 1

    return score

def main():
    data = [input() for i in range(5)]
    print(handman(data))

if __name__ == '__main__':
    main()
