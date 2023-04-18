from django.test import TestCase
from .models import Book
from datetime import date


class BookModelTestCase(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="Война и мир",
            author="Лев Толстой",
            description="Роман о войне и мире.",
            published_date=date(1869, 1, 1),
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Война и мир")
        self.assertEqual(self.book.author, "Лев Толстой")
        self.assertEqual(self.book.description, "Роман о войне и мире.")
        self.assertEqual(self.book.published_date, date(1869, 1, 1))

    def test_book_update(self):
        self.book.title = "Преступление и наказание"
        self.book.save()
        self.assertEqual(self.book.title, "Преступление и наказание")

    def test_book_deletion(self):
        self.book.delete()

    def test_book_list_view(self):
        response = self.client.get('/books/')
        self.assertContains(response, "Война и мир")

    def test_book_detail_view(self):
        response = self.client.get('/books/{}/'.format(self.book.id))
        self.assertContains(response, "Лев Толстой")
