# Write a Python program to find the number of notes (Samples of notes: 10, 20, 50, 100, 200, 500) against an amount.

def how_many_notes(amount):
    notes_available = [500, 200, 100, 50, 20, 10]
    number_of_notes = {}
    for note in notes_available:
        if amount >= note:
            number_of_notes[note] = amount // note
            amount %= note
    return number_of_notes

amt = int(input("Enter your amount: "))
count_of_notes = how_many_notes(amt)

print(f"Number of notes against {amt} : ")

for note, count in count_of_notes.items():
    print(f"{note} : {count}")