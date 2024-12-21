from abc import ABC
from abc import abstractmethod

class Player(ABC):
    def __init__(self, nickname: str) -> None :
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass


class Elf(Player, ABC):
    def __init__(self, musical_instrument: str, nickname: str) -> None :
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the {self._musical_instrument}")


class Dwarf(Player, ABC):
    def __init__(self, favourite_dish: str, nickname: str) -> None:
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None :
        print(f"{self.nickname} is eating {self._favourite_dish}")


class ElfRanger(Elf):
    def __init__(
            self,
            bow_level: int,
            musical_instrument: str,
            nickname: str
    ) -> None:
        super().__init__(musical_instrument, nickname)
        self._bow_level = bow_level

    def get_rating(self) -> int:
        return 3 * self._bow_level

    def player_info(self) -> str:
        return (
            f"Elf ranger {self.nickname}. "
            f"{self.nickname} has bow of the {self._bow_level} level"
        )


class Druid(Elf):
    def __init__(
            self,
            musical_instrument: str,
            nickname: str,
            favourite_spell: str,
    ) -> None:
        super().__init__(musical_instrument, nickname)
        self._favourite_spell = favourite_spell

    def get_rating(self) -> int:
        return len(self._favourite_spell)

    def player_info(self) -> str:
        return (
            f"Druid {self.nickname}. "
            f"{self.nickname} has a favourite spell: {self._favourite_spell}"
        )


class DwarfWarrior(Dwarf):
    def __init__(
            self,
            favourite_dish: str,
            nickname: str,
            hummer_level: int
    ):
        super().__init__(favourite_dish, nickname)
        self._hummer_level = hummer_level

    def get_rating(self) -> int:
        return self._hummer_level + 4

    def player_info(self) -> str:
        return (
            f"Dwarf warrior {self.nickname}. "
            f"{self.nickname} has a hummer of the {self._hummer_level} level"
        )


class DwarfBlacksmith(Dwarf):
    def __init__(
            self,
            favourite_dish: str,
            nickname: str,
            skill_level: int
    ):
        super().__init__(favourite_dish, nickname)
        self._skill_level = skill_level

    def get_rating(self) -> int:
        return self._skill_level

    def player_info(self) -> str:
        return (
            f"Dwarf blacksmith {self.nickname}"
            f" with skill of the {self._skill_level} level"
        )


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum([player.get_rating() for player in players])

def elves_concert(elfs: list[Elf]) -> None:
    for elf in elfs:
        elf.play_elf_song()

def feast_of_the_dwarves(dwarfs: list[Dwarf]) -> None :
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()