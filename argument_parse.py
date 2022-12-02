# @author: Praveen Dominic

import argparse


def position_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("num1",help="number1")
    parser.add_argument("num2", help="number2")
    parser.add_argument("operation", help="operation", choices=['add','subtract'])

    args=parser.parse_args()
    return args

def optional_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--num1', help = 'number1')
    parser.add_argument('--num2', help = 'number2')
    parser.add_argument('--operation', help = 'operation', choices=['add', 'subtract'])
    
    args=parser.parse_args()
    return args


args = position_args()
print(args.num1)
print(args.num2)
print(args.operation)

args1=optional_args()
print(args1.num1)
print(args1.num2)
print(args1.operation)

