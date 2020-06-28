Sequence_A = [34,55,78]
Sequence_B = [66,13,96]
Avg_Sequence_A = (Sequence_A[0] + Sequence_A[2] + Sequence_A[1])/3
Avg_Sequence_B = (Sequence_B[0] + Sequence_B[2] + Sequence_B[1])/3
if( Avg_Sequence_A == Avg_Sequence_B):
    print("they are of the same amount")
else:
    if(Avg_Sequence_A > Avg_Sequence_B):
        print("Avg Sequence A is greater than Avg Sequence B, which is: " + str(Avg_Sequence_A))
    else:
         print("Avg Sequence A is smaller than Avg Sequence B, which is: " + str(Avg_Sequence_B))