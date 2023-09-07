import sys
args = sys.argv

def kuku(number):
    kuku = []
    for i in range(number):
        i = i + 1
        for j in range(number):
            calc = i * j
            if calc != 0 and i != number:
                context =+ calc
                kuku.append(context)
    return kuku

def sort(kuku_array):
    start = 0
    end = 9
    for _ in kuku_array:
        kukulist = kuku_array[start:start+end:1]
        kuku = ",".join(map(str,kukulist))
        print(f"情報 : {kuku}")
        start += end
        if start >= len(kuku_array):
            break

def main(args):
    number = int(args[1])
    result = kuku(number)
    sort(result)

if __name__ == "__main__":
    main(args)