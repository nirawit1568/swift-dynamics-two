
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
def number_2_thai_text(number):
    thai_digits = ['ศูนย์', 'หนึ่ง', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า']
    thai_units = ['', 'สิบ', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน', 'สิบล้าน']
    result = ''
    if not(0 <= int(number) < 10000000):
        raise ValueError("Input number must be between 1 and 1000")

    if number == '0':
        return thai_digits[0]
    
    for i in range(0, len(number)):
        if number[i] != '0':
            if number[i] == '1' and len(number) >= 2 and i == len(number) - 1: # เช็คว่าเลขหนึ่งอยู๋หลักสุดท้าย และหลักทั้งหมดมีมากกว่า 2 หลัก
                result += 'เอ็ด'

            elif number[i] == '2' and len(number) >= 2 and i == len(number) - 2: # เช็คว่าเลขสองอยู๋หลักรองสุดท้าย และหลักทั้งหมดมีมากกว่า 2 หลัก
                result += 'ยี่'
                result += thai_units[len(number) - i - 1]

            elif number[i] == '1' and len(number) >= 2 and i == len(number) - 2: # เช็คว่าเป็นหลักสิบหรือไม่ ถ้าเป็นหลักสิบจะเรียกสิบแทนหนึ่ง
                result += thai_units[len(number) - i - 1]

            elif number[i] == '1' and len(number) >= 2 and i == len(number) - 8: # เช็คว่าเป็นหลักสิบล้านหรือไม่
                result += thai_units[len(number) - i - 1]

            else:
                result += thai_digits[int(number[i])]
                result += thai_units[len(number) - i - 1]
        
    return result

number = input('Please fill a arabic number.\n')
result = number_2_thai_text(number)
print(result)