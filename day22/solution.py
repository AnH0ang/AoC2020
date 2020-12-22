from copy import deepcopy


def play_game(deck0: list[int], deck1: list[int]) -> tuple[int, list[int], list[int]]:
    decks = [deck0, deck1]
    while all(decks):
        round_winner = (card0 := decks[0].pop(0)) < (card1 := decks[1].pop(0))
        decks[round_winner] += sorted([card0, card1], reverse=True)
    return not decks[0], deck0, deck1


def play_recgame(deck0: list[int], deck1: list[int]) -> tuple[int, list[int], list[int]]:
    history: list[list[int]] = []

    while deck0 and deck1:
        card0 = deck0.pop(0)
        card1 = deck1.pop(0)

        if card0 <= len(deck0) and card1 <= len(deck1):
            round_winner, *_ = play_recgame(deck0[:card0], deck1[:card1])
        else:
            round_winner = card0 < card1

        if round_winner:
            deck1 += [card1, card0]
        else:
            deck0 += [card0, card1]

        if deck0 in history:
            return 0, deck0, deck1
        history.append(deepcopy(deck0))

    return not deck0, deck0, deck1


def main() -> None:
    decks: list[list[int]]
    decks = [[int(card) for card in deck.split("\n")[1:]]
             for deck in open("input.txt", "r").read().split("\n\n")]

    # solution 1
    winner, *t_decks = play_game(*deepcopy(decks))
    silver = sum(pos * card for pos,
                 card in enumerate(reversed(t_decks[winner]), 1))
    print(silver)

    # solution 2
    winner, *t_decks = play_recgame(*deepcopy(decks))
    gold = sum(pos * card for pos,
               card in enumerate(reversed(t_decks[winner]), 1))
    print(gold)


if __name__ == "__main__":
    main()
