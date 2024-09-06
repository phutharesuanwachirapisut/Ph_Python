def main():
    list_a = ['喝 (hē)','今年 (jīnnián)','岁 (suì)', '下午 (xiàwǔ)', '东西 (dōngxī)', '生日 (shēngrì)', '快乐 (kuàilè)','月 (yuè)','号 (hào)']
    unity(list_a)
def unity(list_a):
    for item in list_a:
        chinese_char = item[:item.index("(")].lstrip("")

        chinese_piyin = item[item.index("(")+1:item.index(")")]
        tup = (chinese_piyin,chinese_char)
        print(tup,end="")
if __name__ == "__main__":
    main()