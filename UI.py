import tkinter as tk
from tkinter.constants import NONE
import BranchAndBoundJob8

window = tk.Tk()

window.geometry("600x500")

textArea = tk.Text(window, height=15, width=35)
textArea.pack()

textResult = tk.Text(window, height=10, width=30)
# textResult.config(state=tk.DISABLED)
textResult.pack()

button = tk.Button(window, height=1, width=10, text="Commit",
                   command=lambda: retrieve_input())

button.pack()


def retrieve_input():
    inputValue = textArea.get("1.0", "end-1c")
    matrix = []
    array = []
    num = ""
    for x in range(len(inputValue)):
        if(inputValue[x] == "\n"):
            array.append(int(num))
            num = ""

            matrix.append(array)
            array = []
        elif(inputValue[x] == " "):
            array.append(int(num))
            num = ""
        elif(x + 1 == len(inputValue)):
            num += inputValue[x]
            array.append(int(num))
        else:
            num += inputValue[x]

    matrix.append(array)
    print(matrix)
    copyM = []
    for x in range(len(matrix)):
        copyM.append(matrix[x].copy())

    result = BranchAndBoundJob8.JobAssigment(copyM)

    temp = result[0]
    totalCost = 0
    while(temp.getParent() != None):
        totalCost += matrix[temp.getWorker()][temp.getJob()]
        temp = temp.getParent()

    if(len(result) == 1):
        textResult.delete(1.0, "end")
        Re(result[0], matrix)

    textResult.insert(1.0, "Total Cost: " + str(totalCost) + "\n")


def Re(node, matrix):
    if(node.getParent().getParent() != None):
        Re(node.getParent(), matrix)

    textResult.insert(1.0, "Worker: " + str(node.getWorker()) + ", " + "Job: " + str(
        node.getJob()) + ", " + "Cost: " + str(matrix[node.getWorker()][node.getJob()]) + "\n")


window.mainloop()
