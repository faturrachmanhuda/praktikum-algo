def hex_to_dec(hex_str, index=0, result=0):
    if index == len(hex_str):
        return result
    char = hex_str[-(index + 1)].upper()
    value = int(char) if char.isdigit() else 10 + ord(char) - ord('A')
    result += value * (16 ** index)
    return hex_to_dec(hex_str, index + 1, result)

def dec_to_hex(decimal, result=""):
    if decimal == 0:
        return result[::-1] if result else "0"
    hex_chars = "0123456789ABCDEF"
    result += hex_chars[decimal % 16]
    return dec_to_hex(decimal // 16, result)

hex_value = input("Masukkan nilai hexadecimal: ")
print(f"Hasil konversi '{hex_value}' ke decimal: {hex_to_dec(hex_value)}")

decimal_value = int(input("Masukkan nilai decimal: "))
print(f"Hasil konversi '{decimal_value}' ke hexadecimal: {dec_to_hex(decimal_value)}")
