from . import db, app

print(f"Database URI {app.config['SQLALCHEMY_DATABASE_URI']}")

class ContactMe(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'ContactMe'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=False
    )
    email = db.Column(
        db.String(80),
        index=False,
        unique=False,
        nullable=False
    )
    created = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=False
    )
    contact = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=False
    )
    message = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=False
    )

    def __repr__(self):
        return '<User {}>'.format(self.name)