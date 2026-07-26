#!/usr/bin/python3
def magic_string(memory=[0]):
    memory[0] += 1
    return ", ".join(["BestSchool"] * memory[0])
