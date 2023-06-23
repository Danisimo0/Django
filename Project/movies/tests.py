from django.test import TestCase
from django.urls import reverse

from .models import Category, Actor, Genre, Movie, Rating, Reviews, LikeDislike


class MovieTestCase(TestCase):
    def setUp(self):
        # Создаем несколько объектов для тестирования
        self.category = Category.objects.create(name="Action", slug="action")
        self.actor1 = Actor.objects.create(name="Actor 1", age=30, slug="actor1")
        self.actor2 = Actor.objects.create(name="Actor 2", age=35, slug="actor2")
        self.genre = Genre.objects.create(name="Sci-Fi", slug="sci-fi")
        self.movie = Movie.objects.create(title="Movie 1", description="Description 1", year=2021,
                                          country="USA", category=self.category)

        self.movie.directors.add(self.actor1)
        self.movie.actors.add(self.actor1, self.actor2)
        self.movie.genres.add(self.genre)

        self.rating = Rating.objects.create(count_reviews=3, sum_rating=14, avg_rating=4.67, movie=self.movie)

        self.review = Reviews.objects.create(name="John", text="Great movie!", movie=self.movie)

    def test_movie_detail_view(self):
        # Проверяем, что страница деталей фильма возвращает корректный статус ответа и использует правильный шаблон
        url = reverse("movie_detail", kwargs={"slug": self.movie.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movie_detail.html")

    def test_actor_detail_view(self):
        # Проверяем, что страница деталей актера возвращает корректный статус ответа и использует правильный шаблон
        url = reverse("actor_detail", kwargs={"slug": self.actor1.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "actor_detail.html")

    def test_genre_catalog_view(self):
        # Проверяем, что страница каталога жанра возвращает корректный статус ответа и использует правильный шаблон
        url = reverse("genre_catalog", kwargs={"slug": self.genre.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "genre_catalog.html")

    def test_movie_rating(self):
        # Проверяем функцию рейтинга фильма
        # У фильма должен быть объект рейтинга
        self.assertIsNotNone(self.movie.rating)

        # Проверяем, что изначально рейтинг фильма равен 4.67
        self.assertEqual(self.movie.rating.avg_rating, 4.67)

    def test_movie_errors(self):
        # Проверяем возникновение ошибок при некорректных данных
        # Попытка создания фильма с неправильным годом
        with self.assertRaises(ValueError):
            Movie.objects.create(title="Film 3", description="Description 3", year=-2023, category=self.category)

        # Попытка создания рейтинга с отрицательным средним рейтингом
        with self.assertRaises(ValueError):
            Rating.objects.create(count_reviews=2, sum_rating=-10, avg_rating=-5, movie=self.movie)

        # Попытка создания отзыва без указания имени
        with self.assertRaises(ValueError):
            Reviews.objects.create(text="Good movie!", movie=self.movie)

    def test_like_dislike(self):
        # Проверяем функцию лайков и дизлайков для отзыва
        # У отзыва должны быть связанные объекты лайков и дизлайков
        self.assertIsNotNone(self.review.votes)

        # Проверяем, что изначально количество лайков и дизлайков равно 0
        self.assertEqual(self.review.votes.likes().count(), 0)
        self.assertEqual(self.review.votes.dislikes().count(), 0)

        # Добавляем несколько лайков и дизлайков
        LikeDislike.objects.create(vote=LikeDislike.LIKE, content_object=self.review)
        LikeDislike.objects.create(vote=LikeDislike.LIKE, content_object=self.review)
        LikeDislike.objects.create(vote=LikeDislike.DISLIKE, content_object=self.review)

        # Проверяем, что количество лайков и дизлайков правильно подсчитывается
        self.assertEqual(self.review.votes.likes().count(), 2)
        self.assertEqual(self.review.votes.dislikes().count(), 1)


class CategoryTestCase(TestCase):
    def test_category_str(self):
        # Проверяем строковое представление категории
        category = Category.objects.create(name="Action", slug="action")
        self.assertEqual(str(category), "Action")


class ActorTestCase(TestCase):
    def test_actor_str(self):
        # Проверяем строковое представление актера
        actor = Actor.objects.create(name="Actor 1", age=30, slug="actor1")
        self.assertEqual(str(actor), "Actor 1")


class GenreTestCase(TestCase):
    def test_genre_str(self):
        # Проверяем строковое представление жанра
        genre = Genre.objects.create(name="Sci-Fi", slug="sci-fi")
        self.assertEqual(str(genre), "Sci-Fi")


class RatingTestCase(TestCase):
    def test_rating_str(self):
        # Проверяем строковое представление рейтинга
        movie = Movie.objects.create(title="Movie 1", description="Description 1", year=2021)
        rating = Rating.objects.create(count_reviews=3, sum_rating=14, avg_rating=4.67, movie=movie)
        self.assertEqual(str(rating), "4.67 - Movie 1")


class ReviewsTestCase(TestCase):
    def test_reviews_str(self):
        # Проверяем строковое представление отзыва
        movie = Movie.objects.create(title="Movie 1", description="Description 1", year=2021)
        review = Reviews.objects.create(name="John", text="Great movie!", movie=movie)
        self.assertEqual(str(review), "Movie 1 - John")
