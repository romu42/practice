#!/usr/bin/env python3

# https://codechalleng.es/bites/49/

from bites.bite49_packt import get_book

book = get_book()


def test_type():
    assert isinstance(book, tuple)


def test_book_title():
    assert book.title == 'Mastering TypeScript - Second Edition'


def test_book_description():
    assert book.description == ('Build enterprise-ready, industrial-strength '
                                'web applications using '
                                'TypeScript and leading JavaScript frameworks')


def test_book_image():
    assert book.image == '//d1ldz4te4covpm.cloudfront.net/sites/default/files/imagecache/dotd_main_image/B05588.png'  # noqa E501


def test_book_link():
    assert book.link == '/application-development/mastering-typescript-second-edition'  # noqa E501
