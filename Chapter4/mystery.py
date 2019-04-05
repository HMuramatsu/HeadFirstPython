# Pythonの関数引数は、状況によって値渡しと参照渡しの両方を行う。
def double(arg):
    print('実行前: ', arg)
    arg = arg * 2
    print('実行後: ', arg)


def change(arg: list):
    print('実行前: ', arg)
    arg.append('さらなるデータ')
    print('実行後: ', arg)    