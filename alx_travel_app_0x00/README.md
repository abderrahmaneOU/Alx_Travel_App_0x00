# alx_travel_app_0x00

This is a duplicated and extended version of the original `alx_travel_app` project.

## Overview

This Django project includes a `listings` app with models for travel listings, bookings, and reviews. It also includes serializers for API data representation and a management command to seed the database with sample data.

## Listings App

### Models

- **Listing**: Represents a travel listing with fields such as title, description, location, price per night, and availability.
- **Booking**: Represents a booking for a listing, linked to a user, with start and end dates.
- **Review**: Represents a user review for a listing, including rating and comments.

### Serializers

- `ListingSerializer`: Serializes all fields of the Listing model.
- `BookingSerializer`: Serializes all fields of the Booking model.

### Management Command

- `seed`: Seeds the database with sample listings data.

## Setup and Usage

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Apply migrations:
   ```
   python manage.py migrate
   ```

3. Seed the database with sample data:
   ```
   python manage.py seed
   ```

4. Run the development server:
   ```
   python manage.py runserver
   ```

## Testing

Please specify if you want critical-path testing or thorough testing of the new features.

## Notes

- The `user` field in Booking and Review models currently references Django's built-in User model.
- Adjustments may be needed to integrate with authentication and other project-specific requirements.
