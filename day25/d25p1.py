# open and read the input file
input_file = open("day25/input.txt", "r")
input = input_file.read().split("\n")

lookup = {"2":2, "1":1, "0":0, "-":-1, "=":-2}
reverse_lookup = "012=-"

def snafu_to_decimal(snafu:str) -> int:
    decimal_value = 0
    for position in range(len(snafu)):
        col_value = 5 ** position
        decimal_value += lookup[snafu[-1-position]] * col_value
    return decimal_value

def decimal_to_snafu(n:int) -> str:
    snafu_value = []
    while n:
        d = n % 5
        snafu_value.append(reverse_lookup[d])
        if d in [3, 4]:
            n += 2
        n = n // 5

    snafu_value.reverse()

    return ''.join(snafu_value)

decimal_total = 0
for line in input:
    decimal_value = snafu_to_decimal(line)
    decimal_total += decimal_value

print(f"Decimal sum of values: {decimal_total}")
print(f"Snafu sum of values: {decimal_to_snafu(decimal_total)} {snafu_to_decimal(decimal_to_snafu(decimal_total))}")