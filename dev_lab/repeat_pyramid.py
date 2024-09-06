import math
def main():
    # myinput = input()
    test_repeat_pyramid()

def repeat_pyramid(word):
    result = [word[0]]
    teter = word[0]
    limit_len = (2 * len(word) - 1)

    for i in range(1,len(word)):
        teter = word[i] + " " + teter + " " + word[i]
        result.append(teter)
    dedarer = ""
    for j in range(len(result)):
        dedarer = " " * (limit_len - math.ceil(len(result[j])/2)) + result[j]
        result[j] = dedarer
    last_re = ""
    for z in result:
        last_re = last_re + z + "\n"
    return last_re
def test_repeat_pyramid():
    assert repeat_pyramid('Python') == """          P
        y P y
      t y P y t
    h t y P y t h
  o h t y P y t h o
n o h t y P y t h o n
"""

    assert repeat_pyramid('BORNTODEV') == """                B
              O B O
            R O B O R
          N R O B O R N
        T N R O B O R N T
      O T N R O B O R N T O
    D O T N R O B O R N T O D
  E D O T N R O B O R N T O D E
V E D O T N R O B O R N T O D E V
"""    

    assert repeat_pyramid('RePeAtEr') == """              R
            e R e
          P e R e P
        e P e R e P e
      A e P e R e P e A
    t A e P e R e P e A t
  E t A e P e R e P e A t E
r E t A e P e R e P e A t E r
"""
    print("KK le")
if __name__ == "__main__":
    main()