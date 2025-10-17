# showcase_loops_conditionals.py
# Small demo of Python conditionals and loops with common variants

def demo_conditionals(x):
    print("demo_conditionals:", x)
    # simple if
    if x > 0:
        print("  x is positive")

    # if-else
    if x % 2 == 0:
        print("  x is even")
    else:
        print("  x is odd")

    # if-elif-else
    if x < 0:
        print("  x is negative")
    elif x == 0:
        print("  x is zero")
    else:
        print("  x is positive (checked with elif)")

    # nested if
    if x != 0:
        if abs(x) > 10:
            print("  large non-zero value")
        else:
            print("  small non-zero value")

    # ternary expression
    sign = "pos" if x > 0 else ("zero" if x == 0 else "neg")
    print("  sign (ternary):", sign)
    print()


def demo_for_loops(items):
    print("demo_for_loops:", items)
    # simple for
    for i in items:
        print("  item:", i)

    # for with range and enumerate
    for idx, val in enumerate(items):
        print(f"  index {idx} => {val}")

    # nested for
    pairs = []
    for a in items:
        for b in items:
            pairs.append((a, b))
    print("  pairs count:", len(pairs))

    # for-else: else runs if loop wasn't terminated by break
    for i in range(3):
        print("  for-else loop value:", i)
        if i == 10:
            break
    else:
        print("  for-else: completed without break")
    print()


def demo_while_loops(limit):
    print("demo_while_loops up to:", limit)
    i = 0
    # while loop with continue and break
    while i < limit:
        i += 1
        if i % 2 == 0:
            # skip even numbers
            continue
        if i > 7:
            print("  breaking at", i)
            break
        print("  odd i:", i)
    else:
        # runs only if loop finishes normally (no break)
        print("  while-else: finished without break")
    print()


def demo_misc():
    print("demo_misc:")
    # pass (does nothing but is syntactically valid in conditional/loop)
    for _ in range(1):
        pass

    # conditional expression inside list comprehension
    nums = list(range(-3, 4))
    classified = ["pos" if n > 0 else ("zero" if n == 0 else "neg") for n in nums]
    print("  nums:", nums)
    print("  classified:", classified)

    # using try/except in combination with control flow (common pattern)
    values = ["10", "a", "5"]
    parsed = []
    for v in values:
        try:
            parsed.append(int(v))
        except ValueError:
            # skip non-integers
            continue
    print("  parsed ints:", parsed)
    print()


if __name__ == "__main__":
    demo_conditionals(5)
    demo_conditionals(0)
    demo_conditionals(-12)

    demo_for_loops(["apple", "banana", "cherry"])
    demo_while_loops(12)
    demo_misc()