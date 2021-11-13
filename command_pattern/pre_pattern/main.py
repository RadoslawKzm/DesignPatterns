from command_pattern.pre_pattern.banking.bank import Bank


def main() -> None:
    bank = Bank()

    account1 = bank.create_account("ArjanCodes")
    account2 = bank.create_account("Google")
    account3 = bank.create_account("Microsoft")

    account1.deposit(100_000_00)
    account2.deposit(100_000_00)
    account3.deposit(100_000_00)

    account2.withdraw(50_000_00)
    account1.deposit(50_000_00)

    account1.withdraw(150_000_00)

    print(bank)


if __name__ == '__main__':
    main()
