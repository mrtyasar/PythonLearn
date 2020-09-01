def lbsToKg(weight):
    return weight * 0.45

def kgToLbs(weight):
    return weight / 0.45

# büyük ve küçük sayıları bulmak

def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max




