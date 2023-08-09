from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///properties.db"
db = SQLAlchemy(app)


class Operation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)


class Sublocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    location_id = db.Column(db.Integer, nullable=False)


class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)


class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    phone = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)


class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    operation_id = db.Column(db.Integer, nullable=False)
    type_id = db.Column(db.Integer, nullable=False)
    sublocation_id = db.Column(db.Integer, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    garages = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    currency_id = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    agent_id = db.Column(db.Integer, nullable=False)


# "All" option for filters
ALL = 0


@app.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    per_page = 4  # Number of properties per page

    operations = Operation.query.all()
    types = Type.query.all()
    locations = Location.query.all()
    sublocations = Sublocation.query.all()
    currencies = Currency.query.all()

    # Insert "All" option at the beginning of the filters
    operations.insert(ALL, Operation(id=ALL, name="All"))
    types.insert(ALL, Type(id=ALL, name="All"))
    currencies.insert(ALL, Currency(id=ALL, name="All"))

    # Handle form submission
    operation_id = request.args.get("operation_id", type=int)
    type_id = request.args.get("type_id", type=int)
    location = request.args.get("location")
    max_price = request.args.get("max-price", type=float)
    currency_id = request.args.get("currency_id", type=int)
    order = request.args.get("order")

    # Build the query based on form inputs
    query = Property.query

    if operation_id and operation_id != ALL:
        query = query.filter_by(operation_id=operation_id)
    if type_id and type_id != ALL:
        query = query.filter_by(type_id=type_id)
    if location:
        sublocation_ids = set()
        for word in location.split():
            # Search for matching locations and sublocations
            like_locations = Location.query.filter(
                Location.name.ilike(f"%{word}%")
            ).all()
            like_sublocations = Sublocation.query.filter(
                Sublocation.name.ilike(f"%{word}%")
            ).all()

            # Add like sublocations
            sublocation_ids.update(sublocation.id for sublocation in like_sublocations)

            # Add sublocations from like locations
            location_ids = {location.id for location in like_locations}
            derived_sublocations = Sublocation.query.filter(
                Sublocation.location_id.in_(location_ids)
            ).all()
            sublocation_ids.update(
                sublocation.id for sublocation in derived_sublocations
            )

        query = query.filter(Property.sublocation_id.in_(sublocation_ids))

    if max_price:
        query = query.filter(Property.price <= max_price)
    if currency_id and currency_id != ALL:
        query = query.filter_by(currency_id=currency_id)
    if order and order != "default":
        if order == "asc":
            query = query.order_by(Property.price.asc())
        elif order == "desc":
            query = query.order_by(Property.price.desc())

    properties = query.paginate(page=page, per_page=per_page)

    return render_template(
        "index.html",
        operations=operations,
        types=types,
        locations=locations,
        sublocations=sublocations,
        currencies=currencies,
        properties=properties,
    )


@app.route("/property/<int:property_id>")
def property(property_id):
    property = Property.query.get(property_id)
    type_name = Type.query.get(property.type_id).name
    sublocation = Sublocation.query.get(property.sublocation_id)
    location_name = Location.query.get(sublocation.location_id).name
    currency_name = Currency.query.get(property.currency_id).name
    agent = Agent.query.get(property.agent_id)
    return render_template(
        "property.html",
        property=property,
        type_name=type_name,
        sublocation=sublocation,
        location_name=location_name,
        currency_name=currency_name,
        agent=agent,
    )


@app.template_filter()
def currency(value):
    return "${:,.0f}".format(value)


if __name__ == "__main__":
    app.run(debug=True)
