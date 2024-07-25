import pytest
from main import BooksCollector

class TestBooksCollector:

    # тестируем добавление новых книг
    @pytest.mark.parametrize('name', ['Тёмная башня', 'Оно'])
    def test_add_new_book_add_books(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    # тестируем установку книге жанра
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Тёмная башня')
        collector.set_book_genre('Тёмная башня', 'Фантастика')
        assert collector.get_book_genre('Тёмная башня') == 'Фантастика'
        # исправлено

    # тестируем получение жанра книги по её имени
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Тёмная Башня")
        genre = "Фантастика"
        collector.set_book_genre("Тёмная Башня", genre)
        assert collector.get_book_genre("Тёмная Башня") == genre

    # тестируем добавление книги с определённым жанром в список книг с определённым жанром
    def test_get_books_with_specific_genre_includes_correct_book(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        books = collector.get_books_with_specific_genre('Ужасы')
        assert 'Оно' in books
        # исправлено

    # тестируем отсутствие книги без определённого жанра в списке книг с определённым жанром
    def test_get_books_with_specific_genre_excludes_other_books(self):
        collector = BooksCollector()
        collector.add_new_book('Тёмная башня')
        collector.set_book_genre('Тёмная башня', 'Фантастика')
        books = collector.get_books_with_specific_genre('Ужасы')
        assert 'Тёмная башня' not in books
        # исправлено

    # тестируем получение словаря books_genre
    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Тёмная башня')
        collector.add_new_book('Оно')
        assert 'Тёмная башня' in collector.get_books_genre()
        assert 'Оно' in collector.get_books_genre()

    # тестируем возвращение книг, подходящим детям
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Тёмная Башня')
        collector.add_new_book('Оно')
        collector.set_book_genre('Тёмная Башня', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert 'Тёмная Башня' in children_books
        assert 'Оно' not in children_books

    # тестируем добавление книги в Избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Тёмная Башня')
        collector.add_book_in_favorites('Тёмная Башня')
        assert 'Тёмная Башня' in collector.get_list_of_favorites_books()

    # тестируем удаление книги из Избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Тёмная Башня')
        collector.add_book_in_favorites('Тёмная Башня')
        collector.delete_book_from_favorites('Тёмная Башня')
        assert 'Тёмная Башня' not in collector.get_list_of_favorites_books()

    # тестируем получение списка Избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Тёмная Башня')
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Тёмная Башня')
        collector.add_book_in_favorites('Оно')
        favorites = collector.get_list_of_favorites_books()
        assert 'Тёмная Башня' in favorites
        assert 'Оно' in favorites
