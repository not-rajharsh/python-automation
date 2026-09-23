import logging
#Log Levels (Lowest to Highest Severity)**:
#`DEBUG` (10) → `INFO` (20) → `WARNING` (30) → `ERROR` (40) → `CRITICAL` (50)

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

logging.basicConfig(filename='Local-Automation\\test.log',level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

num1=132178
num2=721369

ar=add(num1,num2)
logging.debug('{}+{}={}'.format(num1, num2, ar))

sr=sub(num1,num2)
logging.debug('{}-{}={}'.format(num1, num2, sr))

mr=mul(num1,num2)
logging.debug('{}x{}={}'.format(num1, num2, mr))

dr=div(num1,num2)
logging.debug('{}/{}={}'.format(num1, num2, dr))