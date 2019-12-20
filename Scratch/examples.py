# program that runs programs
# model for generally what we will be doing

# memory just holds numbers bcs even letters are numbers
# arrays are perfect for how ram/memory works
# because memory has addresses exaclty like index into an array/list
# so if you have a list of 10 things there are 10 index.
# Values for each of those 10 things

print_chris = 1
halt = 2
print_num = 3
save = 4 # save value into register
print_register = 5
add = 6

memory = [
    print_chris,
    print_chris,
    print_num,
    save,
    33,
    print_chris,
    add,
    print_register,
    15,
    halt,
    print_chris,
    print_chris
]

# write code that goes thru the list, looks at instruction
# does what it says, one by one

# for loop, if/else
# for i in memory:
#     if i == halt:
#         break
#     else:
#         print(i)

# while loop
running = True
pc = 0  # program counter,
# index into memory of the current instruction

# create 8 registers
register = [0] * 8

# while running:
#     TODO

while running:
    current_instruction = memory[pc]

    if current_instruction == print_chris:
        print("Chris!")
        pc += 1

    elif current_instruction == print_num:
        pc +=1
        num = memory[pc]
        print(num)

    elif current_instruction == halt:
        running = False

    elif current_instruction == save:
        num = memory[pc+1]  # get num from first arg
        reg = memory[pc+2]  # get register index from 2nd arg
        register[reg] = num # store the num in the correct register
        pc += 3

    elif current_instruction == print_register:
        reg = memory[pc+1]
        print(register[reg])
        pc += 1

    elif current_instruction == add:
        reg_a = memory[pc+1]
        reg_b = memory[pc+2]
        register[reg_a] += register[reg_b]  # should be 85
        pc += 3

    else:
        print(f'unknown instruction at address {pc}')
        sys.exit(1)
