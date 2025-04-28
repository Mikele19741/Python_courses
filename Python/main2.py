hello="hello"
world="world"

print(f"{hello} {world}")

def greeting(greet):
    return lambda name: f"{greet} {name}"

morning_greeting=greeting("Good Morning")
print(morning_greeting("Mike"))