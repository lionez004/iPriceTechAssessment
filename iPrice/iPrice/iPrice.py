import csv


def alternate(line):
    line = [element.upper() if not word % 2 else element.lower() for word, element in enumerate(line)] 
    line = "".join(line) 

    return line

def split(line):
    line = list(line)
    write_to_csv(line)
    return line

def write_to_csv(line):
    with open('splitword.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(line)
    return print("CSV created")



if __name__ == '__main__':
    line = input("input:")
    print(line.upper())
    print (alternate(line))
    split(line)
