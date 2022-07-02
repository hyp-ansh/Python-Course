import datetime
class order():
    def __init__(self, order_id):
        self.order_id = order_id
        self.date = str(datetime.datetime.now())[0:-7]
order01 = order('A01')
print(order01.date)