#!/usr/bin/env -S python3 -B

import sys

if __name__ == "__main__" :
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    output1 = "1"
    output2 = "2"
    print("::set-output name=output-one::" + input1)
    print("::set-output name=output-two::" + input2)

