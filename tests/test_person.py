from beings.person import Person
import pytest


@pytest.fixture()
def person():
    return Person("Ian Hill", 48, jobs=["QA Engineer"])


def test_init(person: Person):
    assert person.name == "Ian Hill"
    assert person.age == 48
    assert person.jobs == ["QA Engineer"]


def test_forename(person: Person):
    assert person.forename == "Ian"


def test_surname(person: Person):
    assert person.surname == "Hill"


def test_celebrate_birthday(person: Person):
    person.celebrate_birthday()
    assert person.age == 49


def test_add_job(person: Person):
    person.add_job("Influencer")
    assert person.jobs == ["QA Engineer", "Influencer"]
