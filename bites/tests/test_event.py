#!/usr/bin/env python3
# by rog
# https://codechalleng.es/bites/64/

from bites.event import get_attendees


def test_get_attendees(capfd):
    get_attendees()
    output = capfd.readouterr()[0].strip().split("\n")

    assert len(output) == 8
    assert "('Kim', '-', '-')" in output
    assert "('Andre', '-', '-')" in output