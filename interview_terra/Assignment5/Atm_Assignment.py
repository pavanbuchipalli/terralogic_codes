# amount  = int(input("amount:----"))
# note1 = 0
# note2 = 0
# note3 = 0
# while True:
#     if amount >= 500 :
#         c = amount- 500
#         note1 += 1
#         amount= c
#     else:
#         break
# # print(amount)
# # print(note1)
# while True:
#         if amount >= 200:
#             r =amount -200
#
#             note2 +=1
#             amount =r
#         else:
#             break
# while True:
#     if amount >= 50:
#         f = amount - 50
#         note3 += 1
#         amount = f
#     else:
#         break
#
# print("500 notes:",note1)
# print("200 notes:",note2)
# print("50 notes:",note3)
# print("remaining amount",amount)

class Atm:
    def __init__(self):
        self.amount = 0
        self.note1 = 0
        self.note2 = 0
        self.note3 = 0

    def Atm_money(self):
        while self.amount >= 500:
            self.amount -= 500
            self.note1 += 1

        while self.amount >= 200:
            self.amount -= 200
            self.note2 += 1

        while self.amount >= 50:
            self.amount -= 50
            self.note3 += 1
            if self.amount == 0:
                 break

    def user_request(self):
        while True:
            user2 = input("you  want to continue the process :-- yes/no")
            if user2 == "yes":

                self.amount = int(input("Select Amount 500/200/50 notes only: "))
                if self.amount % 50 == 0:
                    self.Atm_money()
                    self.Money_recived()
                    user3 = input("do want to continue the process :-- yes/no")
                    if user3 =="yes":
                        continue
                    else:
                        break
                else:
                    print("you have entered the wrong input ")

            else:
                print("The process had ended")
                break



    def Money_recived(self):
        print("500 notes:", self.note1)
        print("200 notes:", self.note2)
        print("50 notes:", self.note3)
        print("Remaining amount:", self.amount)


counter = Atm()
counter.user_request()
# counter.Atm_money()
# counter.Money_recived()
