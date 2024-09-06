#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# HW14_2
# 229223 Sec 002
def main():
    print('OK')

def append_ranking(infile_name='score_in.txt', outfile_name='score_out.txt'):
    with open(infile_name, 'r') as infile:
        lines = infile.readlines()

    student_scores = {}
    for line in lines:
        data = line.strip().split(',')
        student = data[0]
        scores = list(map(int, data[1:]))
        total_score = sum(sorted(scores, reverse=True)[:2]) * 0.1
        student_scores[student] = total_score

    sorted_students = sorted(student_scores.items(), key=lambda x: x[1], reverse=True)

    ranked_lines = []
    for rank, (student, _) in enumerate(sorted_students, start=1):
        line = f"{student},{','.join(map(str, sorted(student_scores[student], reverse=True)))},{rank}\n"
        ranked_lines.append(line)

    with open(outfile_name, 'w') as outfile:
        outfile.writelines(ranked_lines)

if __name__ == '__main__':
    main()