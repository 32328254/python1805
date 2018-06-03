#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pickle
import os
import time


def save_money(record, wallet):
    try:
        amount = int(input('amount number:'))
        comment = input('comment: ')
    except:
        print("input Invlid")
        return
    dates = time.strftime('%Y-%m-%d')
    with open(wallet, 'rb') as fobj:
        balance = pickle.load(fobj) + amount
    lines = '%-12s%-10s%-10s%-10s%-10s\n' % (dates, '', amount, balance, comment)
    with open(record, 'a') as fobj:
        fobj.write(lines)
    with open(wallet, 'wb') as fobj:
        pickle.dump(balance, fobj)


def cost_money(record, wallet):
    try:
        amount = int(input('amount number:'))
        comment = input('comment: ')
    except:
        print("input Invild")
        return
    dates = time.strftime('%Y-%m-%d')
    with open(wallet, 'rb') as fobj:
        balance = pickle.load(fobj)
        # balance = pickle.load(fobj) - amount
    if balance >= amount:
        balance -= amount
        lines = '%-12s%-10s%-10s%-10s%-10s\n' % (dates, amount, '', balance, comment)
        with open(record, 'a') as fobj:
            fobj.write(lines)
        with open(wallet, 'wb') as fobj:
            pickle.dump(balance, fobj)
    else:
        print('not sufficient funds')


def view_money(record, wallet):
    print("\033[32;1mtime, cost,amount, balance, comment\033[0m")
    with open(record, 'r') as fobj:
        for line in fobj:
            print(line, end='')
    with open(wallet, 'rb') as fobj:
        balance = pickle.load(fobj)
    print("\033[31;1mLatest Balance: %d\033[0m" % balance)


def view_menu():
    record = 'record.txt'
    wallet = 'wallet.date'
    if not os.path.exists(record):
        os.mknod(record)
    if not os.path.exists(wallet):
        with open(wallet, 'wb') as fobj:
            pickle.dump(10000, fobj)
    prompt = """(0) save money
(1) cost money
(2) view money
(3) quit
pleast input you choice(0/1/2/3): """
    cmds = {"0": save_money, "1": cost_money, "2": view_money}
    while True:
        try:
            choice = input(prompt).strip()[0]
        except IndexError as index:
            print("choice Invlid")
            continue
        except (KeyboardInterrupt, EOFError):
            print()
            choice == '3'
        if choice not in '0123':
            print("Invlid input,Try again!")
            continue
        elif choice == '3':
            print("bye bye")
            break
        cmds[choice](record, wallet)


if __name__ == '__main__':
    view_menu()
