"""
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.

Given an integer n, return its complement.

"""


def base_ten_complement(n: int) -> int:
    bin_num = bin(n).replace("0b", "")

    for i in range(len(bin_num)):
        if bin_num[i] == "0":
            bin_num = bin_num[:i] + "1" + bin_num[i + 1 :]
        else:
            bin_num = bin_num[:i] + "0" + bin_num[i + 1 :]

    base_ten_complement = int(bin_num, 2)

    return base_ten_complement


if __name__ == "__main__":
    print(base_ten_complement(5))
    print(base_ten_complement(12))
    print(base_ten_complement(10))
