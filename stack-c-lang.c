#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_SIZE 100

typedef struct {
    int data[MAX_SIZE];
    int top;
} Stack;

// Initialize the stack
void initStack(Stack *s) {
    s->top = -1;
}

// Check if the stack is empty
bool isEmpty(Stack *s) {
    return s->top == -1;
}

// Check if the stack is full
bool isFull(Stack *s) {
    return s->top == MAX_SIZE - 1;
}

// Push an element onto the stack with input validation
bool push(Stack *s, int value) {
    if (isFull(s)) {
        printf("Error: Stack overflow. Cannot push %d\n", value);
        return false;
    }
    s->data[++(s->top)] = value;
    return true;
}

// Pop an element from the stack with input validation
bool pop(Stack *s, int *value) {
    if (isEmpty(s)) {
        printf("Error: Stack underflow. Cannot pop.\n");
        return false;
    }
    *value = s->data[(s->top)--];
    return true;
}

// Peek at the top element with input validation
bool peek(Stack *s, int *value) {
    if (isEmpty(s)) {
        printf("Error: Stack is empty. Cannot peek.\n");
        return false;
    }
    *value = s->data[s->top];
    return true;
}

// Example usage
int main() {
    Stack s;
    initStack(&s);

    int n, val;
    printf("Enter number of elements to push (max %d): ", MAX_SIZE);
    if (scanf("%d", &n) != 1 || n < 0 || n > MAX_SIZE) {
        printf("Invalid input.\n");
        return 1;
    }

    for (int i = 0; i < n; ++i) {
        printf("Enter value to push: ");
        if (scanf("%d", &val) != 1) {
            printf("Invalid input.\n");
            return 1;
        }
        push(&s, val);
    }

    printf("Popping all elements:\n");
    while (pop(&s, &val)) {
        printf("%d\n", val);
    }

    return 0;
}