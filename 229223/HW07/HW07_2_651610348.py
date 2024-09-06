#!/usr/bin/env python3
# Phutharesuan_Wachirapisut
# 651610348
# HW07_2
# 229223 Sec 002

# 1. เรียง และ reverse แล้ว ตัด 0 ออกให้หมด ใส่ใน list_a
# 2. len(list_a) นำมาพิจารณา silver and bronze = []
# 3. หา max(list_a) เอามาเทียบเพื่อพิจารณา gold เป็นอันดับแรก 
# 4. เรียง และ reverse แล้ว ตัด 0 ออกให้หมด ใส่ใน gold
# 5. ตัดค่า gold ออกจากใน list_a
# 6. ถ้าจำนวน gold = 1 และ len(list_a) > 1 ให้หา silver โดยย้อนกลับไปที่ 3
#     6.1 ถ้าจำนวน silver = 1 และ len(list_a) > 1 ให้ที่หา bronze
# 7. ถ้าจำนวน gold = 2 และ len(list_a) > 2 ให้หา bronze
# 8. ถ้าจำนวน gold > 2 silver and bronze = []

def main():
    test_medal_allocation()
    # medal_allocation([0, 1, 1, 1])

def medal_allocation(list_a):
    gold = []
    silver = []
    bronze = []
    if list_a.count(0) == len(list_a):
        result = gold , silver , bronze
        return result

    if list_a.count(0) > 0:
        list_a = without_num(list_a,0)

    max_list_a_first = find_max(list_a)

    gold = list(map(lambda x : x if x == max_list_a_first else 0 , list_a))
    if gold.count(0) > 0: # ([1 , 1 , 1], [], [])
        gold = without_num(gold, 0)

    if len(gold) > 2:
        result = gold , silver , bronze
        return result

    list_a = without_max(list_a, max_list_a_first) # ตัดค่าสูงสุดที่เอาไปใส่ใน gold เพื่อหาค่าสูงสุดตัวใหม่

    max_list_a_second = find_max(list_a)
    
    if len(gold) == 2:
        bronze = list(map(lambda x : x if x == max_list_a_second else 0 , list_a))
        if bronze.count(0) > 0: # ([1 , 1 , 1], [], [])
            bronze = without_num(bronze, 0)
        
        if len(bronze) == 0:
            result = gold , silver , bronze
            return result

        result = gold , silver , bronze
        return result
    
    if len(gold) == 1:
        silver = list(map(lambda x : x if x == max_list_a_second else 0 , list_a))
        if silver.count(0) > 0:
            silver = without_num(silver, 0)

        if len(silver) == 1:
            list_a = without_max(list_a, max_list_a_second) # ตัดค่าสูงสุดที่เอาไปใส่ใน silver เพื่อหาค่าสูงสุดตัวใหม่
            max_list_a_third = find_max(list_a)

            bronze = list(map(lambda x : x if x == max_list_a_third else 0 , list_a))
            if bronze.count(0) > 0: # ([1 , 1 , 1], [], [])
                bronze = without_num(bronze, 0)
            
            if len(bronze) == 0:
                result = gold , silver , bronze
                return result

            result = gold , silver , bronze
            return result
        else:
            result = gold , silver , bronze
            return result
    

def without_num(n,num):
    n.sort(reverse=True)
    index_num = n.index(num)
    n = n[:index_num]
    return n

def without_max(n,num):
    n.sort()
    index_num = n.index(num)
    n = n[:index_num]
    return n

def find_max(list_a):
    if list_a == []:
        return list_a
    else:
        if len(list_a) == 1:
            return list_a[0]
        
        head = list_a[0]
        tail = list_a[1:]
        max_tail = find_max(tail)

        if max_tail > head:
            return max_tail
        else:
            return head

def test_medal_allocation():
    assert medal_allocation([0, 0, 0, 0, 0]) == ([], [], [])
    assert medal_allocation([9, 8, 7, 6, 5, 4, 3, 2]) == ([9], [8], [7])
    assert medal_allocation([9, 8, 7, 7, 6, 5, 4, 3, 2]) == ([9], [8], [7, 7])
    assert medal_allocation([9, 9, 8, 7, 6, 5, 4, 3, 2]) == ([9, 9], [], [8])
    assert medal_allocation([9, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2]) == ([9, 9, 9, 9], [], [])
    assert medal_allocation([1, 9, 6, 2, 2, 2, 2, 2]) == ([9], [6], [2, 2, 2, 2, 2])
    assert medal_allocation([1, 8, 8, 8, 5, 4, 9, 8]) == ([9], [8, 8, 8, 8], [])
    assert medal_allocation([0, 1, 2]) == ([2], [1], [])
    assert medal_allocation([0, 1, 2 , 2 , 1 , 1]) == ([2,2], [], [1,1,1])
    assert medal_allocation([0, 1, 1, 1]) == ([1, 1 ,1], [], [])
    assert medal_allocation([0, 1, 1]) == ([1 , 1], [], [])
    assert medal_allocation([0, 1, 2, 2]) == ([2 , 2], [], [1])
    assert medal_allocation([0, 1, 1, 2, 2]) == ([2, 2], [], [1 , 1])
    assert medal_allocation([0, 1, 2, 1, 1]) == ([2], [1, 1, 1], [])
    assert medal_allocation([0, 3, 2, 1, 1, 1]) == ([3], [2], [1,1,1])
    print("OK!")

if __name__ == '__main__':
    main()