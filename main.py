"""
Exercise 1
"""


class Stack:
    def __init__(self, data_type, maximum_stack_size):
        self.data_type = data_type
        self.maximum_stack_size = maximum_stack_size
        self.stack = [None] * maximum_stack_size
        self.top_index = -1

    def push(self, number):
        if type(number) == self.data_type and self.top_index < self.maximum_stack_size - 1:
            self.top_index += 1
            self.stack[self.top_index] = number
        elif self.top_index == self.maximum_stack_size - 1:
            print("Stack is full")
        else:
            print("Data type is invalid")

    def pop(self):
        if self.top_index >= 0:
            number = self.stack[self.top_index]
            self.stack[self.top_index] = None
            self.top_index -= 1
            return number
        else:
            print("Stack is empty")
            return None

    def is_empty(self):
        return self.top_index == -1

    def top(self):
        if not self.is_empty():
            number = self.stack[self.top_index]
            return number
        else:
            return None

    def convert_from_infix_to_postfix(self, infix_expression):
        infix_expression_length = 0
        for element in infix_expression:
            infix_expression_length += 1

        end_expression = ""
        infix_stack = Stack(str, infix_expression_length)

        order = {'+': 2, '-': 2, '*': 1, '/': 1}

        current_element = 0
        while current_element < infix_expression_length:
            if infix_expression[current_element].isdigit() or infix_expression[current_element] == '.':
                number = ""
                while current_element < infix_expression_length and (
                        infix_expression[current_element].isdigit() or infix_expression[current_element] == '.'):
                    number += infix_expression[current_element]
                    current_element += 1
                end_expression += number + " "
                continue

            elif infix_expression[current_element] == '-':
                if current_element == 0 or not (infix_expression[current_element - 1].isdigit()
                                                or infix_expression[current_element - 1] == '.'):
                    number = ""
                    current_element += 1
                    while current_element < infix_expression_length and (
                            infix_expression[current_element].isdigit() or infix_expression[current_element] == '.'):
                        number += infix_expression[current_element]
                        current_element += 1
                    end_expression += number + " "
                    continue

            elif infix_expression[current_element] == '(':
                infix_stack.push(infix_expression[current_element])

            elif infix_expression[current_element] == ')':
                while not infix_stack.is_empty() and infix_stack.top() != '(':
                    end_expression += str(infix_stack.pop()) + " "
                if not infix_stack.is_empty() and infix_stack.top() == '(':
                    infix_stack.pop()

            elif infix_expression[current_element] in ['+', '-', '*', '/']:
                while not infix_stack.is_empty() and infix_stack.top() in ['+', '-', '*', '/'] \
                        and order[infix_stack.top()] >= order[infix_expression[current_element]]:
                    end_expression += str(infix_stack.pop()) + " "
                infix_stack.push(infix_expression[current_element])

            current_element += 1

        while not infix_stack.is_empty():
            end_expression += str(infix_stack.pop()) + " "

        return end_expression.strip()

    def evaluate_postfix_expression(self, postfix_expression):
        final_result = 0
        postfix_expression_length = 0

        for element in postfix_expression:
            postfix_expression_length += 1
            postfix_stack = Stack(str, postfix_expression_length)

        for char in postfix_expression.split():
            if char.isdigit():
                postfix_stack.push(char)
            elif char.startswith('-') and char[1:].isdigit():
                postfix_stack.push(-int(char[1:]))
            else:
                operand2 = float(postfix_stack.pop())
                operand1 = float(postfix_stack.pop())
                if char == "+":
                    final_result = operand1 + operand2
                elif char == "-":
                    final_result = operand1 - operand2
                elif char == "*":
                    final_result = operand1 * operand2
                elif char == "/":
                    final_result = operand1 / operand2
                postfix_stack.push(str(final_result))
        return postfix_stack.pop()


"""
Exercise 2 (Palindromes)
"""


class Word:
    def __init__(self, word):
        self.word = word
        self.next = None


class LinkedList:
    def __init__(self):
        self.main_word = None

    def insert(self, word):
        new_word = Word(word)
        if self.main_word is None:
            self.main_word = new_word
        else:
            current_word = self.main_word
            while current_word.next:
                current_word = current_word.next
            current_word.next = new_word

    def reverse(self):
        previous = None
        current_word = self.main_word

        while current_word:
            next_word = current_word.next
            current_word.next = previous
            previous = current_word
            current_word = next_word

        self.main_word = previous

    def is_palindrome(self):
        slow_iteration = self.main_word
        fast_iteration = self.main_word
        prev = None

        while fast_iteration and fast_iteration.next:
            fast_iteration = fast_iteration.next.next

            # Reverse the first half of all the words
            next_slow = slow_iteration.next
            slow_iteration.next = prev
            prev = slow_iteration
            slow_iteration = next_slow

        # Skip middle word when number of words is odd
        if fast_iteration:
            slow_iteration = slow_iteration.next

        # Compare the reversed first half with the second half
        while slow_iteration:
            if slow_iteration.word != prev.word:
                return False
            slow_iteration = slow_iteration.next
            prev = prev.next

        return True


def main_function():
    # Exercise 1
    stack = Stack(float, 20)
    infix_expression = input("Enter infix expression:\n")
    postfix_expression = stack.convert_from_infix_to_postfix(infix_expression)
    print(postfix_expression)

    result = stack.evaluate_postfix_expression(postfix_expression)
    print(result)

    # Exercise 2
    expression = input("Enter string which you want to check if is a palindrome\n")

    expression = expression.replace(" ", "")
    expression = expression.replace(",", "")

    linked_list = LinkedList()
    for char in expression:
        linked_list.insert(char)

    linked_list.reverse()

    is_palindrome = linked_list.is_palindrome()

    if is_palindrome:
        print("The expression is a palindrome.")
    else:
        print("The expression is not a palindrome.")


if __name__ == "__main__":
    main_function()
