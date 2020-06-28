from Bank_class import Bank
def main():
    George_Amberson = Bank(1,1000)
    George_Amberson.Set_ID(12345)
    George_Amberson.Remove_Value(100)
    print(George_Amberson.Set_Password(12345))
    print(George_Amberson.Get_Value(12345,12345))
    print(George_Amberson.Upgrade_Membership(2))
    print(George_Amberson.Show_ID())
    print(George_Amberson.Get_Value(123,1233))


if __name__ == "__main__":
    main()