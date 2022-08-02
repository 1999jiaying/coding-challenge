"""
challenge: https://leetcode.com/problems/implement-stack-using-queues/
question: Implement a last-in-first-out (LIFO) stack using only two queues.
The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
"""
# solution

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
class MyStack:

    def __init__(self):

        self.stack = list()

    def push(self, x):

        self.stack.insert(0, x)

    def pop(self):

        item = self.stack.pop(0)

        return item

    def top(self):

        return self.stack[0]

    def empty(self):

        if not self.stack:
            return True
        else:
            return False



# test
def op(order, value):
    out = []
    index = 0
    for i in order:
        if i == 'MyStack':
            mstack = MyStack()
            out.append(None)
        if i == 'push':
            out.append(mstack.push(value[index][0]))
        if i == 'top':
            out.append(mstack.top())
        if i == 'pop':
            out.append(mstack.pop())
        if i == 'empty':
            out.append(mstack.empty())
        index += 1
    return out


def test_answer():
    assert op(["MyStack", "push", "push", "top", "pop", "empty"],
              [[], [1], [2], [], [], []]) == [None, None, None, 2, 2, False]
    assert op(["MyStack", "push", "push", "push", "pop", "empty"],
              [[], [1], [2], [3], [], []]) == [None, None, None, None, 3, False]
