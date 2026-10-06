# DFA Simulator
# Language: Strings ending with "ab"

states = ["q0", "q1", "q2"]
alphabet = ["a", "b"]

# Transition table
transition = {
    "q0": {
        "a": "q1",
        "b": "q0"
    },
    "q1": {
        "a": "q1",
        "b": "q2"
    },
    "q2": {
        "a": "q1",
        "b": "q0"
    }
}

initial_state = "q0"
final_states = ["q2"]


def simulate_dfa(input_string):

    current_state = initial_state
    path = [current_state]

    for symbol in input_string:

        if symbol not in alphabet:
            return path, False

        current_state = transition[current_state][symbol]
        path.append(current_state)

    accepted = current_state in final_states

    return path, accepted


# Accept multiple strings
n = int(input("Enter number of strings: "))

for i in range(n):

    string = input("\nEnter input string: ")

    path, result = simulate_dfa(string)

    print("Transition Path:")
    print(" → ".join(path))

    if result:
        print("Accepted")
    else:
        print("Rejected")