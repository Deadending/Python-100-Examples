def find_min_peaches(remaining_peaches):
    while 1:
        total_peaches = remaining_peaches
        for i in range(5):
            if total_peaches % 5 != 1:
                break
            total_peaches = (total_peaches - 1) // 5 * 4
        else:
            return remaining_peaches
        remaining_peaches += 1

if __name__ == '__main__':
    remaining_peach_min = 1
    min_peaches = find_min_peaches(remaining_peach_min)
    print("海滩上原来最少有 %d 个桃子。" % min_peaches)