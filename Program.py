import numpy as np
from tkinter import *


def removing_dominated_strategies(m, text):
    # matrix size
    size = m.shape

    # return the matrix if it's already 1x1
    if size == (1, 1):
        text.append("End of the computation. There's no more dominated columns/rows")
        return

    # check dominated rows
    for i in range(size[0]):
        for j in range(i + 1, size[0]):
            # compare these two rows
            result = (m[i, :] >= m[j, :])

            # if each elements in jth row >= to ith row
            # this implies that jth row dominate ith row
            if np.all(result == 0):
                # remove ith row
                # and continue looking for other dominated rows/columns
                m = np.delete(m, i, 0)
                text.append(
                    "Row {} is (strongly) dominated by Row {}; \nThe new matrix is \n{}\n\n".format(i + 1, j + 1, m))
                return removing_dominated_strategies(m, text)

            # if each elements in jth row <= to ith row
            # this implies that ith row dominate jth row
            if np.all(result == 1):
                m = np.delete(m, j, 0)
                text.append(
                    "Row {} is (strongly) dominated by Row {}; \nThe new matrix is \n{}\n\n".format(j + 1, i + 1, m))
                return removing_dominated_strategies(m, text)

    # check dominated columns
    for i in range(size[1]):
        for j in range(i + 1, size[1]):
            # compare these two columns
            result = (m[:, i] >= m[:, j])

            # if each elements in jth column >= to ith column
            # this implies that ith column dominate jth column
            if np.all(result == 0):
                # remove ith row
                # and continue looking for other dominated rows/columns
                m = np.delete(m, j, 1)
                text.append(
                    "Column {} is (strongly) dominated by Column {}; \nThe new matrix is \n{}\n\n".format(j + 1, i + 1,
                                                                                                          m))
                return removing_dominated_strategies(m, text)

            # if each elements in jth row <= to ith row
            # this implies that jth row dominate ith row
            if np.all(result == 1):
                m = np.delete(m, i, 1)
                text.append(
                    "Column {} is (strongly) dominated by Column {}; \nThe new matrix is \n{}\n\n".format(i + 1, j + 1,
                                                                                                          m))
                return removing_dominated_strategies(m, text)
    # if no dominated rows/column found

    text.append("End of the computation. There's no more dominated columns/rows")
    return


def list_to_string(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


if __name__ == "__main__":
    root = Tk()
    root.title('MAT406 Remove dominated strategies')
    root.geometry("500x900")


    def clear():
        text_box1.delete(1.0, END)
        text_box2.delete(1.0, END)


    def solve():
        text_box2.delete(1.0, END)
        m = []
        text = []
        ipt = text_box1.get(1.0, END)
        rows = list(filter("".__ne__, ipt.split("\n")))
        for i in rows:
            curr_row = list(filter("".__ne__, i.split(" ")))
            curr = []
            for j in curr_row:
                curr.append(int(j))
            m.append(curr)
        matrix = np.array(m)
        try:
            removing_dominated_strategies(matrix, text)
            text_box2.insert(END, list_to_string(text))
        except:
            text_box2.insert(END, "Invalid Input!")


    text_box1 = Text(root, width=40, height=15, font=("Helvetica", 16))
    text_box1.pack(pady=20)

    button_frame = Frame(root)
    button_frame.pack()

    clear_button = Button(button_frame, text="Clear", command=clear)
    clear_button.grid(row=0, column=0)

    get_text_button = Button(button_frame, text="Remove Dominated Strategies", command=solve)
    get_text_button.grid(row=0, column=1, padx=20)

    text_box2 = Text(root, width=40, height=15, font=("Helvetica", 16))
    text_box2.pack(pady=20)

    root.mainloop()
