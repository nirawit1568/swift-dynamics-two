
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
def arabic_to_roman(num):
    if not 0 < num < 1000:
        raise ValueError("Input number must be between 1 and 1000")
    
    roman_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'
    }

    roman = ""
    for value in sorted(roman_numerals.keys(), reverse=True):
        while num >= value:
            roman += roman_numerals[value]
            num -= value

    return roman

arabic_number = int(input('Please fill a arabic number.\n'))
roman_number = arabic_to_roman(arabic_number)
print(f"{arabic_number} in Roman numerals is {roman_number}")