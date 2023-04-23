import os

count = 0

os.system('bcdedit /set {badmemory} badmemoryaccess no')

try:
    with open('RAM.txt') as f:
        for line in f:
            line = line.strip()
            sector = "0x" + line
            line = "bcdedit /set {badmemory} badmemorylist 0x" + line
            exit_code = os.system(line)

            if exit_code != 0:
                print(f'Hata oluştu: {exit_code}')
                input()
            else:
                print(f'RAM Sector: {sector} banned.')
                count += 1
except FileNotFoundError:
    print('RAM.txt file not found. Please create a RAM.txt file in the same folder as the script.')
    input()
        
print(f'Banned RAM Sector: {count}. Press any key to exit.')
input()


