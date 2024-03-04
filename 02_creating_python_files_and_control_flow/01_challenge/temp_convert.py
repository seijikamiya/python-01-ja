def convert():
    # ここにコードを書いてください
    # temp変数を編集し、ユーザー入力として温度を受け取ります。整数に変換することを忘れないでください
    temp = int(input('温度を入力して下さい'))
    unit = input('温度の単位をfかcで入力して下さい')

    if unit == "f":
        temp = (temp - 32) * 5/9
    elif unit == "c":
        temp = temp * 9/5 + 32

    return temp

convert()
