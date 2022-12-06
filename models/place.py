#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False, default=0)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False, default=0)
    longitude = Column(Float, nullable=False, default=0)
    amenity_ids = []

    # Establishes a relationship between Reviews and Places
    reviews = relationship("Review", cascade="all, delete", backref="place")

    @property
    def reviews(self):
        """ Returns a dictionary of all reviews with a place_id
            matching this instance's id
        """
        from models.__init__ import storage
        from models.review import Review
        # Create empty dictionary
        r_dict = {}

        # Fill with all reviews whose place_id match this instance's id
        for key, value in storage.all(Review).items():
            if value.to_dict()['place_id'] == self.id:
                r_dict[key] = value
