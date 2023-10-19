class SavingAccount:
    pass
class ChekingAccount:
    pass
class Stock:
    pass
class Bond:
    pass
class RealEstate:
    pass


class BankAccount(SavingAccount,ChekingAccount):
    pass
class Security(Stock,Bond):
    pass

class IntersetBearingltem(Security,BankAccount):
    pass
class Asset(Security,BankAccount):
    pass
class Insurabletem(BankAccount,RealEstate):
    pass
