#Batch gradient Descent Scratch implimentation using python

def read_file(fileName):
    import pandas as pd
    df = pd.read_csv(fileName)
    return df


def update_w_and_b(area, price, w, b, alpha):
    dc_dw = 0.0
    dc_db = 0.0
    N = len(area)
    for i in range(N):
        dc_dw += -2 * area[i] * (price[i] - (w * area[i] + b))
        dc_db += -2 * (price[i] - (w * area[i] + b))
    # update w and b
    w = w - (1 / float(N)) * dc_dw * alpha
    b = b - (1 / float(N)) * dc_db * alpha

    return w, b


def train(area, price, w, b, alpha, ephocs):
    N = len(area)
    y_pred = []
    for e in range(ephocs):
        # log of progress
        if e % 4 == 0:
            for i in range(N):
                y_pred.append(area[i] * w + b)

            print('epoch:{}, loss:{}, w:{}, b=:{}'.format(e, avg_loss(area, price, w, b), w, b))
            draw_data(area, price, y_pred)
            y_pred = []
        # updating value of w and b
        w, b = update_w_and_b(area, price, w, b, alpha)

    return w, b


def avg_loss(area, price, w, b):
    N = len(area)
    total_error = 0.0
    for i in range(N):
        total_error += ((w * area[i] + b) - price[i]) ** 2
    return total_error / float(N)


def draw_data(x, y, y_pred):
    import matplotlib.pyplot as plt
    plt.title('House Price Prediction')
    plt.xlabel('area in sequre feet')
    plt.ylabel('price in USD $')
    plt.scatter(x, y)
    plt.plot(x, y_pred)
    plt.show()


def predict(x, w, b):
    return w * x + b


df = read_file('data.csv')

# dummy data
# area=[1,1,2,2,3,3,4,4,5,5,6,6,7,7]
# price=[2,3,3,4,4,5,5,6,6,7,7,8,8,9]

area = df.area[0:21]
price = df.price[0:21]
w = 0.0
b = 1.0
alpha = 0.000001
ephocs = 9
w, b = train(area, price, w, b, alpha, ephocs)
x = int(input('Enter the area of the house:: '))
y = predict(x, w, b)
print('your house would be sell at: {} USD$'.format(y))

