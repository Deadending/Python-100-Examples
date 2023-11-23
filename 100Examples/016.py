import datetime
import time


if __name__ == "__main__":
    print(time.time())
    print(time.localtime())
    print(time.asctime())
    print(time.strftime('%Y-%m-%d %H-%M-%S', time.localtime()))
    print(time.strftime('%H-%M-%S %d-%m-%Y', time.localtime()))

    print(datetime.date.today().strftime('%d-%m-%Y'))
