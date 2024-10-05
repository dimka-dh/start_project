def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if "@" not in recipient or not (
            recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}, неверно указан адрес получателя.")
        return
    if "@" not in sender or not (sender.endswith(".com") or sender.endswith(".ru") or sender.endswith(".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', input('Введите адрес для отправки: '))
send_email('Вы видите это сообщение как лучший студент курса!', 'dimm15@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'dimm15@mail.ru', sender='dimm15@mail.ru')
