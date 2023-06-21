while True:
    def is_multiple_of_11(number):
        # 將奇位數的數字加總為 A，偶位數的數字加總為 B
        A = 0
        B = 0
        for i in range(len(number)):
            digit = int(number[i])
            if i % 2 == 0:  # 奇數位
                A += digit
            else:  # 偶數位
                B += digit
    
        # 取 A-B 的絕對值
        diff = abs(A - B)
    
        # 判斷絕對值是否為 11 的倍數
        if diff % 11 == 0:
            return True
        else:
            return False
    
    input_number = input("請輸入一個純數字之字串：")
    result = is_multiple_of_11(input_number)
    
    if result:
        print("是 11 的倍數")
    else:
        print("不是 11 的倍數")
