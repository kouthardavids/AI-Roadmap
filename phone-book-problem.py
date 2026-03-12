# 1. Open the phone book
# 2. Open to the middle of the phone book
# 3. Look at page
# 4. If person is on the page
# 5.     -> CALL THE PERSON
# 6. Else if person is earlier in the book
# 7.     -> GO TO THE MIDDLE OF THE LEFT SIDE OF THE PHONE BOOK
# 8. Back to line 3 (???while loop)
# 9. Else if person is later in the book
# 10.    -> GO TOT THE MIDDLE OF THE RIGHT SIDE OF THE PHONE BOOK
# 11. Go back to line 3
# 12. Else Quit

phone_book = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]
target = "Alice"

def call_person(book, target):
    right = len(book) - 1
    left = 0

    while right >= left:  # we use a while loop bc we want to repeat this function until we get a result based on a certain condition
        mid = (left + right) // 2
        person = book[mid]
        print(f"Looking at page {mid}: {person}")

        if person == target:
            print(f"Found {person} on page {mid}. Calling {person}!")
            return mid
        
        elif person > target:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return -1


call_person(phone_book, target)