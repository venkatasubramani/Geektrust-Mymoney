import sys
from Mymoney import Mymoney


def main():
    input_file = sys.argv[1]
    # sys.argv[1] should give the absolute path to the input file
    # parse the file and process the command
    # print the output
    money_obj = None
    month_count = 0
    file1 = open(input_file, 'r')
    lines = file1.readlines()
    for line in lines:
        inp_line = line.split(' ')
        if inp_line[0] == 'ALLOCATE':
            money_obj = Mymoney(float(inp_line[1]), float(inp_line[2]), float(inp_line[3]))
        elif inp_line[0] == 'SIP':
            money_obj.sip(float(inp_line[1]), float(inp_line[2]), float(inp_line[3]))
        elif inp_line[0] == 'CHANGE':
            money_obj.change(float(inp_line[1].replace('%', '')), float(inp_line[2].replace('%', '')),
                             float(inp_line[3].replace('%', '')), inp_line[4], month_count)
            month_count += 1
        elif inp_line[0] == 'BALANCE':
            money_obj.balance(inp_line[1])
        elif inp_line[0] == 'REBALANCE':
            money_obj.rebalance()


if __name__ == "__main__":
    main()