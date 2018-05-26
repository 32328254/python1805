#/usr/bin/env python
# -*- coding:utf-8 -*-
stack = []
def pop_it():
    if stack:
        stack.pop()
    else:
        print("null")
    #return stack
def push_it():
    item = input("item to push: ")
    stack.append(item)
    print(stack)
    #return stack
def view_it():
    print(stack)
def show_menu():
    cmds = {'0': pop_it, '1': push_it, '2': view_it}
    prompt = """(0) pop it
    (1) push it
    (2) view it
    (3) quit
please input you choice(0/1/2/3):"""
    while True:
        choice = input(prompt).strip()[0]
        if choice not in '0123':
            print("Invalid input . try again.")
            continue
        if choice == '3':
            break
        cmds[choice]()  ##这是重点
"""
        elif choice == '0':
            pop_it()
        elif choice == '1':
            push_it()
        elif choice == '2':
            view_it()
"""
if __name__ == '__main__':
    show_menu()