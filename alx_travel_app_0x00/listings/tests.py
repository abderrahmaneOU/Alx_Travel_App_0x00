from django.test import TestCase
from .models import Listing, Booking, Review
from django.contrib.auth.models import User
from datetime import date

class ListingModelTest(TestCase):
    def setUp(self):
        self.listing = Listing.objects.create(
            title="Test Listing",
            description="Test Description",
            location="Test Location",
            price_per_night=100.00,
            is_available=True
        )

    def test_listing_creation(self):
        self.assertEqual(self.listing.title, "Test Listing")
        self.assertTrue(self.listing.is_available)

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.listing = Listing.objects.create(
            title="Test Listing",
            description="Test Description",
            location="Test Location",
            price_per_night=100.00,
            is_available=True
        )
        self.booking = Booking.objects.create(
            listing=self.listing,
            user=self.user,
            start_date=date.today(),
            end_date=date.today(),
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.user.username, 'testuser')
        self.assertEqual(self.booking.listing.title, "Test Listing")

class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.listing = Listing.objects.create(
            title="Test Listing",
            description="Test Description",
            location="Test Location",
            price_per_night=100.00,
            is_available=True
        )
        self.review = Review.objects.create(
            listing=self.listing,
            user=self.user,
            rating=5,
            comment="Great place!"
        )

    def test_review_creation(self):
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, "Great place!")
