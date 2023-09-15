import typer


def change(amount):
    assert amount >= 10
    if amount == 10:
        return [5, 5]
    if amount == 12:
        return [5, 7]
    if amount == 14:
        return [7, 7]
    if amount == 15:
        return [5, 5, 5]
    if amount == 17:
        return [5, 7, 5]
    if amount == 19:
        return [5, 7, 7]
    if amount == 21:
        return [7, 7, 7]
    if amount == 28:
        return [7, 7, 7, 7]
    coins = change(amount - 5)
    coins.append(5)
    return coins


def main(amount: int):
    print(change(amount))


if __name__ == "__main__":
    typer.run(main)
