def compute_factorial():
    # ここにコードを書いてください
    # number変数を編集し、ユーザー入力として正の整数を受け取ります。整数に変換することを忘れないでください
    number = int(input('Please input an integer: '))
    if number < 0:
        print('pleases input a positive value')
    else:
        result = 1
        if number >= 2:
            for i in range(1, number+1):
                result *= i

    return result


compute_factorial()
