def eval_loop():
    while True:
        a = input()
        if(a=="done"):
            break
        print(eval(a))

eval_loop()