# 方法一
def ScoreLevel(score):
    if score>= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    else:
        return 'C'

if __name__ == "__main__":
    score = int(input("输入分数：\n"))
    level = ScoreLevel(score)
    print("%d 属于 %s" %(score, level))


#方法二
score = int(input("输入分数：\n"))
level = 'A' if score >= 90 else 'B' if score >= 80 else 'C'
print("%d 属于 %s" %(score, level))