import requests,json,random,string

class Register:
    def __init__(self):
        #密码
        self.password="qqq123456"
        #邀请码
        self.referralCode="lololinh0"

    def register(self,name,email):
        """
        注册器
        :param name:
        :param email:
        :return: 打印出注册好的账号
        """
        url='https://www.cambly.com/users'
        headers={'Content-Type': 'application/json; charset=UTF-8',
                'Content-Length': '281',
                'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; MI 5s MIUI/V8.0.22.0.MAGCNDI)',
                'Host': 'www.cambly.com',
                'Connection': 'Keep-Alive',
                'Accept-Encoding': 'gzip'
    }
        #构造请求参数
        data={"accountTypes":["student-en"],
              "androidDevice":"HUAWEI / HUAWEI NXT-AL10",
              "androidVersion":23,
              "device":100,
              #判别同一设备机制是设备id
              "deviceId":random.randint(188878575467865,999999999999999),
              "email":email,
              "language":"zh",
              "minutes":0,
              "password":self.password,
              "referralCode":self.referralCode,
              "username":name,
              "validCreditCard":'false'}
        requests.post(url=url,data=json.dumps(data),headers=headers)
        #打印出注册好的账号
        print(email)

    def random_string(self,num):
        """
        随机email、name的构造器
        :param num:
        :return: name_list,email_list
        """
        name_list = []
        email_list = []
        s = string.ascii_letters
        r = random.randint(1, 10)
        for i in range(0, num+1):
            l = random.choice(s)
            l2 = random.choice(s)
            l3 = random.choice(s)
            l4 = random.choice(s)
            name = l + str(r) + l2 + l3 + l4 + str('hhhh')
            name_list.append(name)
            email = name + str('@163.com')
            email_list.append(email)
        return name_list,email_list

    def scheduler(self):
        """
        调度器
        :return:
        """
        #num为需要的账号数量
        num=20
        name_list, email_list=self.random_string(num)
        count = 0
        for name in name_list:
            email = email_list[count]
            self.register(name, email)
            count = count + 1

if __name__ == '__main__':
    R=Register()
    R.scheduler()
