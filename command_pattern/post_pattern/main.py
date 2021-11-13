from command_pattern.post_pattern.banking.bank import Bank
from command_pattern.post_pattern.banking.commands import Deposit, Withdraw, Transfer
from command_pattern.post_pattern.banking.controller import BankController, Batch


def main() -> None:
    bank = Bank()

    controller = BankController()

    account1 = bank.create_account("ArjanCodes")
    account2 = bank.create_account("Google")
    account3 = bank.create_account("Microsoft")

    # # account1.deposit(100_000_00)

    controller.execute(Deposit(account1, 100_000_00))
    # # account2.deposit(100_000_00)
    # # account3.deposit(100_000_00)
    # controller.execute(Deposit(account2, 100_000_00))
    # controller.execute(Deposit(account3, 100_000_00))

    # # account2.withdraw(50_000_00)
    # # account1.deposit(50_000_00)
    #
    # controller.execute(Transfer(account2, account1, 50_000_00))

    controller.execute(Batch(commands=[Deposit(account2, 100_000_00),
                                       Deposit(account3, 100_000_00),
                                       Transfer(account2, account1, 50_000_00)]))

    # account1.withdraw(150_000_00)

    controller.execute(Withdraw(account1, 150_000_00))
    # controller.undo()
    print(bank)


if __name__ == '__main__':
    main()
