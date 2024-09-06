import copy

def main():
    test_chess_check_advantage()

def chess_check_advantage(remain_chess):
    remain_chess_copy = copy.deepcopy(remain_chess)
    remain_chess_copy = remain_chess_copy.split("\n")
    result = 0
    dict_a = {'P': 1, 'p': -1, 'N':3, 'n': -3, 'B': 3, 'b': -3, 'R': 5, "r": -5, "Q": 9, "q": -9, "K":0 , 'k':0, ".":0}
    for item in remain_chess_copy:
        for j in range(len(item)):
            result += dict_a[item[j]]
    if result == 0:
        result = "equal"
    return result
            

def test_chess_check_advantage():
    assert chess_check_advantage(""".R......
n.......
........
k.K.....
........
.......P
........
........""") == 3
    assert chess_check_advantage(""".r..k...
.....p.p
......p.
.r.....P
.....QP.
......K.
.....P..
........""") == -1
    assert chess_check_advantage("""q.....k.
......q.
.......q
........
........
........
......R.
......K.""") == -22
    assert chess_check_advantage("""rnbqkbnr
pppppppp
........
........
........
........
PPPPPPPP
RNBQKBNR""") == "equal"
    print("OK")
if __name__ == "__main__":
    main()