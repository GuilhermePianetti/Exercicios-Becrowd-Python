A,B,C = map(int,input().split())

if B < A and C >= B:
    print(":)")
elif B > A and C <= B:
    print(":(")
elif B > A and C > B and B-A > C-B:
    print(":(")
elif B > A and C > B and B-A <= C-B:
    print(":)")
elif A > B and B > C and B - C < A - B:
    print(":)")
elif A > B and B > C and B - C <= A - B:
    print(":(")
elif A == B and B < C:
    print(":)")
elif A == B and B > C:
    print(":(")