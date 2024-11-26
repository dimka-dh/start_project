def introspection_info(obj):
    info = {
        "type": type(obj).__name__,
        "attributes": [],
        "methods": [],
        "module": obj.__class__.__module__ if hasattr(obj, '__class__') else None,
    }

    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            info["methods"].append(attr)
        else:
            info["attributes"].append(attr)

    return info


number_info = introspection_info(55)
string_info = introspection_info("Просто строка текста")

print("Информация о числе:")
print(number_info)
print("\nИнформация о строке:")
print(string_info)


class CustomClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        return f"Переданное значение в класс: {self.value}"


custom_obj = CustomClass(10)
custom_obj_info = introspection_info(custom_obj)

print("\nИнформация о пользовательском классе:")
print(custom_obj_info)
