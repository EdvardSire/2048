###
def game():
    init(iterGRID)

    while not(gameFinished):
        show(iterGRID)
        try:
            key = str(input())
            if key == 'w':
                up(iterGRID)
            if key == 'a':
                left(iterGRID)
            if key == 's':
                down(iterGRID)
            if key == 'd':
                right(iterGRID)
            if key == 'f':
                evaluate(TEMPLATE, iterGRID)

        except IllegalMove:
            print("Illegal Move")

        else:
            try:
                insertNumber(iterGRID)
            except:
                end()


    print("Done")
    print(evaluate(TEMPLATE, GRID))
