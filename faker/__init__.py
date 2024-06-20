"""
The goal of this package is to generate fake user information
from repositories of avaiable data.

This information includes, name, age, sex, race, email, matriculation number.


Matriculation number is a unique identifier for students in a university.
Format: 210591019 | xxxxxxyyy

Where x is the year of admission based on the department namespace
Where y is the unique identifier for the student
"""

import secrets
from typing import Dict, Optional, List, TypeVar, TypedDict, Union
from enum import Enum
from dataclasses import dataclass

from faker.data import NAMES, Sex, Race


S = TypeVar('S', bound=Enum)


def random_from_enum(
    choices: List[S],
    weight: Optional[Dict[S, int]] = None
) -> S:

    if weight is None:
        return secrets.choice(choices)

    for item in weight:
        choices.extend([item] * weight[item])

    return secrets.choice(choices)


T = TypeVar('T')


def random_from_list(
    data:  List[T],
    weight: Optional[Dict[T, int]] = None
) -> T:

    if weight is None:
        return secrets.choice(data)

    choices = data

    for item in weight:
        choices.extend([item] * weight[item])

    return secrets.choice(choices)


class PersonConfiguration(TypedDict):
    name_source: List[str]
    name_weight: Optional[Dict[str, int]]

    age_range_min: int
    age_range_max: int

    age_range_weight: Optional[Dict[int, int]]

    sex_source: List[Sex]
    sex_weight: Optional[Dict[Sex, int]]

    race_source: List[Race]
    race_weight: Optional[Dict[Race, int]]


@dataclass
class Person:
    name: str
    age: int
    sex: Sex
    race: Race
    email: str
    matriculation_number: str

    config: PersonConfiguration

    def __init__(
        self,
        config: PersonConfiguration,
        matriculation_number: str
    ) -> None:
        self.config = config
        self.matriculation_number = matriculation_number

        self.populate_person()

    def __str__(self) -> str:
        return f"""
        _______________________________________

        Profile
        Name: {self.name}
        Email: {self.email}
        Matriculation Number: {self.matriculation_number}

        Stats
        Age: {self.age}
        Sex: {self.sex.value}
        Race: {self.race.value}
        """.replace("        ", "")

    def populate_person(self) -> None:

        first_name: str = self.get_name()
        last_name: str = self.get_name()

        self.name = f"{first_name} {last_name}"
        self.email = f"{first_name}.{last_name}@example.com".lower()

        self.age = self.get_age()
        self.sex = self.get_sex()
        self.race = self.get_race()

    def get_sex(self) -> Sex:
        return random_from_enum(
            self.config["sex_source"],
            self.config["sex_weight"])

    def get_race(self) -> Race:
        return random_from_enum(
            self.config["race_source"],
            self.config["race_weight"]
        )

    def get_name(self) -> str:
        return random_from_list(
            self.config["name_source"],
            self.config["name_weight"]
        )

    def get_age(self) -> int:
        age_range = range(
            self.config["age_range_min"],
            self.config["age_range_max"]
        )

        valid_ages = [age for age in age_range]

        return random_from_list(
            valid_ages,
            self.config["age_range_weight"]
        )


def main() -> None:
    student_configuration: PersonConfiguration = {
        "name_source": NAMES,
        "name_weight": None,
        "age_range_min": 16,
        "age_range_max": 50,
        "age_range_weight": None,
        "sex_source": [item for item in Sex],
        "sex_weight": {
            Sex.F: 7,
        },
        "race_source": [item for item in Race],
        "race_weight": {
            Race.Human: 2,
        }
    }

    # Lets make 30 students

    department_code: str = "CS-210591"

    for i in range(30):
        student_id: str = str(i).rjust(3, "0")

        matriculation_number = f"{department_code}{student_id}"

        student = Person(student_configuration, matriculation_number)

        print(student)


if __name__ == '__main__':
    main()
