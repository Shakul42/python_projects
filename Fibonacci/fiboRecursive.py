def fibo(n):
    n = int(n)
    if n == 0:
        return 0
    if n == 1:
      return 1
	# Recursive call
    return fibo(n-1) + fibo(n-2)



def run():
    print("How many numbers of Fibonacci sequence do you want to print?(must be a positive number)")
    line = input(">")
    try:
        line = int(line)
    except ValueError:
        print("Please enter a valid positive integer.")
        return
    if line < 1:
        print("Please enter a positive integer.")
        return
    print("Fibonacci sequence:")
    for i in range(line):
        print(fibo(i))


if __name__ == '__main__':
    run()