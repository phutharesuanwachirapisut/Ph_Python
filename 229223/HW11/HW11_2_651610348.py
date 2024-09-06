#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# HW11_2
# 229223 Sec 002
def main():
    runner_up()

def runner_up():
    total_students = input("Total students: ")
    if not total_students.isdigit() or int(total_students) <= 0:
        return
    total_students = int(total_students)

    sum_ = 0
    max_score = float('-inf')
    runner_up_score = None

    print("Enter scores: ")
    for i in range(total_students):
        enter_score = input()
        enter_score = float(enter_score)

        sum_ += enter_score

        if enter_score > max_score:
            runner_up_score = max_score
            max_score = enter_score
        elif enter_score < max_score and (runner_up_score is None or enter_score > runner_up_score):
            runner_up_score = enter_score
    if  runner_up_score == float('-inf'):
        runner_up_score = None
    print("---")
    print(f"Max score is: {(max_score):.2f}")
    if runner_up_score != None:
        print(f"Runner up is: {(runner_up_score):.2f}")
    else:
        print(f"Runner up is: {runner_up_score}")
    print(f"Average is: {(sum_ / total_students):.2f}")

if __name__ == '__main__':
    main()
