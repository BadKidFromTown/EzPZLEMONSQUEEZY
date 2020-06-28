def final_exam(stack_1,stack_2,stack_3):
    if stack_1 == [] and stack_2 == [] and stack_3 == [4,3,2,1]:
        return stack_3
    elif stack_1[-1] > stack_2[-1]:
        if stack_1[-1] < stack_3[-1]:
            stack_3.append()
            del stack_1[-1]
        