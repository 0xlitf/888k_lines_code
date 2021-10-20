# -*- coding: utf-8 -*-

out_file_name = "main.cpp"

def test():
    with open(out_file_name, 'w+') as f:
        f.write("#include <iostream>\n")
        f.write("using namespace std;\n")
        f.write("\n")
        f.write("int main() {\n")

        f.write("\tcout << \"请给出一个不多于5位数的正整数：\";\n")
        f.write("\tint x;\n")
        f.write("\tcin >> x;\n")
        f.write("\tswitch (x) {\n")

        for i in range(1, 99999 + 1):
            s = str(i)
            length = len(s)
            f.write("\tcase " + s + ":\n")
            f.write("\t\tcout << \"是" + str(length) + "位数\"" + " << endl;\n")
            f.write("\t\tcout << \"个位数是：" + s[-1] + "\"" + " << endl;\n")

            if length > 1:
                f.write("\t\tcout << \"十位数是：" + s[-2] + "\"" + " << endl;\n")
            if length > 2:
                f.write("\t\tcout << \"百位数是：" + s[-3] + "\"" + " << endl;\n")
            if length > 3:
                f.write("\t\tcout << \"千位数是：" + s[-4] + "\"" + " << endl;\n")
            if length > 4:
                f.write("\t\tcout << \"万位数是：" + s[-5] + "\"" + " << endl;\n")

            f.write("\t\tcout << \"倒过来是：" + s[::-1] + "\"" + " << endl;\n")
            f.write("\t\tbreak;\n")

        f.write("\t}\n")
        f.write("}\n")
        f.write('\n')


if __name__ == "__main__":
    test()





