# Sets können keine compliezierten Elemente enthalten, die werden automatisch entfernt.

emails_der_anmeldungen = ["steffi@gmail.com", "sara@lean.de", "angelina@gmail.com", "steffi@gmail.com", "sara@lean.de"]
print("anzahl der Anmeldungen:", len(emails_der_anmeldungen))

set_emails = set(emails_der_anmeldungen)
print("Anzahl der User:", len(set_emails))