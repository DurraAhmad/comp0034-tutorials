from typing import List

from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from student.flask_paralympics import db


class Event(db.Model):
    __tablename__ = 'event'
    event_id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[int] = mapped_column(nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    date_start: Mapped[str] = mapped_column(Text)
    date_start_text: Mapped[str] = mapped_column(Text)
    duration: Mapped[int]
    countries: Mapped[int]
    events: Mapped[int]
    sports: Mapped[int]
    highlights: Mapped[String] = mapped_column(Text)
    url: Mapped[String] = mapped_column(Text)

    # Relationship to the DisabilityEvent table. back_populates takes the name of the relationship that is defined in the DisabilityClass
    disability_events: Mapped[List["DisabilityEvent"]] = relationship(back_populates="event")


class Disability(db.Model):
    __tablename__ = 'disability'

    disability_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    category: Mapped[str] = mapped_column(Text, nullable=False)

    # Relationship to the DisabilityEvent table. back_populates takes the name of the relationship that is defined in the DisabilityClass
    disability_events: Mapped[List["DisabilityEvent"]] = relationship(back_populates="disability")


class DisabilityEvent(db.Model):
    __tablename__ = 'disability_event'

    event_id: Mapped[int] = mapped_column(ForeignKey('event.event_id'), primary_key=True)
    disability_id: Mapped[int] = mapped_column(ForeignKey('disability.disability_id'), primary_key=True)

    # Relationships to the parent tables, Disability and Event
    # back_populates takes the name of the relationships that is defined in the parent classes (same name was used in both)
    event: Mapped["Event"] = relationship("Event", back_populates="disability_events")
    disability: Mapped["Disability"] = relationship("Disability", back_populates="disability_events")