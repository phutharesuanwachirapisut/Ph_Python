#!/usr/bin/env python3
# ภูธเรศวร วชิรพิศุทย์
# 651610348
# HW04_3
# 229223 Sec 002

def main():
    test_substitute_once()

def substitute_once(text, old, new):
    if old in text:
        index = text.index(old)
        return text[:index] + new + text[index + len(old):]
    else:
        return text

def test_substitute_once():
    assert substitute_once('bubble','b','c') == 'cubble'
    assert substitute_once('Bidding','i','u') == 'Budding'
    assert substitute_once("doesn't","n't"," not") == 'does not'
    print("All Ok!")

if __name__ == '__main__':
    main()