height = input('請輸入身高(公分):')
height = float(height) / 100
weight = input('請輸入體重(公斤):')
weight = float(weight)
BMI = weight / height / height
if BMI < 18.5:
    print('你的BMI值為:', BMI, '體重過輕')
elif 18.5 <= BMI < 24:
    print('你的BMI值為:', BMI, '正常範圍')
elif 24 <= BMI < 27:
    print('你的BMI值為:', BMI, '過重')
elif 27 <= BMI < 30:
    print('你的BMI值為:', BMI,'輕度肥胖')
elif 30 <= BMI < 35:
    print('你的BMI值為:', BMI,'中度肥胖')
else:
    print('你的BMI值為:', BMI,'重度肥胖')

