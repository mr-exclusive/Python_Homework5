# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.readline()


def save_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)


def encode(data):
    encoded = ''
    if data:
        prev_char = ''
        count = 1
        for char in data:
            if char == prev_char:
                count += 1
            else:
                if prev_char:
                    encoded += str(count) + prev_char
                count = 1
                prev_char = char
        encoded += str(count) + prev_char

    return encoded


def decode(data):
    decoded = ''

    if data:
        for i in range(1, len(data), 2):
            decoded += data[i] * int(data[i - 1])

    return decoded


file_name_in = 'dataRLE.txt'
file_name_out = 'encoded_data.txt'

data = read_file(file_name_in)
print(data)

encoded_data = encode(data)
print(encoded_data)
save_file(file_name_out, encoded_data)

decoded_data = decode(encoded_data)
print(decoded_data)
