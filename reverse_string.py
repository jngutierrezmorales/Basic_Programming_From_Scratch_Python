
def reverse_string(string_to_reverse):
    string_reversed = ""
    current_index = len(string_to_reverse) - 1
    while current_index >= 0:
        string_reversed += string_to_reverse[current_index]
        current_index -= 1
    return string_reversed


print(reverse_string("Hola"))
print(reverse_string("Caracola"))
print(reverse_string("Cocacola"))
print(reverse_string("Me llamo dave"))
print(reverse_string("Tengo 100 años"))
print(reverse_string("Me duele la cadera"))
print(reverse_string("Tengo 80 hijos"))
print(reverse_string("Me apetece un te"))
