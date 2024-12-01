import re

def main():
    number_list_1 =[]
    number_list_2 = []

    file = open("input/input_day_01.txt", "r")
    content=file.readlines()
    print(content)
    file.close()

    for line in content:
        
     numbers = re.split(r'   ', line.rstrip('\n'))
     number_list_1.append(int(numbers[0]))
     number_list_2.append(int(numbers[1]))
    
    assert len(number_list_1) == len(number_list_2)

    number_list_1 = sorted(number_list_1)
    number_list_2 = sorted(number_list_2)

    print(number_list_1[:3])
    print(number_list_2[:3])

    # Part 1
    total_distance = 0
    for n1, n2 in zip(number_list_1, number_list_2):
       total_distance += abs(n1-n2)

    print(f"Day 01 - Answer Part 1: {total_distance}")

    # Part 2
    similarity_score = 0

    for n1, n2 in zip(number_list_1, number_list_2):
        occurrences_n2 = number_list_2.count(n1)
        similarity_score += n1*occurrences_n2

    print(f"Day 01 - Answer Part 2: {similarity_score}")
    


if __name__ == "__main__":
    main()
