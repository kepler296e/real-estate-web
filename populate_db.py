from flask_app import (
    app,
    db,
    Operation,
    Type,
    Location,
    Sublocation,
    Currency,
    Agent,
    Property,
)

# Crea un contexto de aplicación
with app.app_context():
    # Crea todas las tablas definidas en los modelos
    db.create_all()

    # Add operations
    operations_data = [
        {"name": "Rent"},
        {"name": "Buy"},
    ]
    for operation_data in operations_data:
        db.session.add(Operation(**operation_data))

    # Add types
    types_data = [
        {"name": "Apartment"},
        {"name": "House"},
        {"name": "Land"},
    ]
    for type_data in types_data:
        type = Type(**type_data)
        db.session.add(type)

    # Add locations
    locations_data = [
        {"name": "Nordelta"},
        {"name": "San Isidro"},
        {"name": "Escobar"},
        {"name": "Benavídez"},
    ]
    for location_data in locations_data:
        location = Location(**location_data)
        db.session.add(location)

    # Add sublocations
    sublocations_data = [
        {
            "name": "El Cantón",
            "latitude": -34.3553,
            "longitude": -58.7417,
            "location_id": 3,
        },
        {
            "name": "Portezuelo",
            "latitude": -34.4026,
            "longitude": -58.6545,
            "location_id": 1,
        },
        {
            "name": "Castores",
            "latitude": -34.4075,
            "longitude": -58.6601,
            "location_id": 1,
        },
        {
            "name": "Las Lomas",
            "latitude": -34.4962,
            "longitude": -58.5452,
            "location_id": 2,
        },
        {
            "name": "San Isidro Labrador",
            "latitude": -34.3842,
            "longitude": -58.6800,
            "location_id": 4,
        },
        {
            "name": "La Colina",
            "latitude": -34.4787,
            "longitude": -58.6408,
            "location_id": 2,
        },
        {
            "name": "Castaños",
            "latitude": -34.4361,
            "longitude": -58.6460,
            "location_id": 1,
        },
    ]
    for sublocation_data in sublocations_data:
        db.session.add(Sublocation(**sublocation_data))

    # Add currencies
    currencies_data = [
        {"name": "USD"},
        {"name": "ARS"},
    ]
    for currency_data in currencies_data:
        db.session.add(Currency(**currency_data))

    # Add agents
    agents_data = [
        {
            "name": "Carl Friedrich Gauss",
            "phone": "12-3456-7890",
            "email": "primenumbers@integer.com",
        },
        {
            "name": "Pierre de Fermat",
            "phone": "12-1122-3344",
            "email": "xnyn@zn.com",
        },
    ]
    for agent_data in agents_data:
        db.session.add(Agent(**agent_data))

    # Add properties (just a few for testing purposes)
    properties_data = [
        {
            "operation_id": 1,
            "type_id": 2,
            "sublocation_id": 1,
            "size": 220,
            "bedrooms": 3,
            "bathrooms": 2,
            "garages": 3,
            "description": "",
            "currency_id": 1,
            "price": 1700,
            "agent_id": 1,
        },
        {
            "operation_id": 1,
            "type_id": 1,
            "sublocation_id": 2,
            "size": 50,
            "bedrooms": 1,
            "bathrooms": 1,
            "garages": 1,
            "description": "",
            "currency_id": 1,
            "price": 450,
            "agent_id": 2,
        },
        {
            "operation_id": 2,
            "type_id": 2,
            "sublocation_id": 3,
            "size": 300,
            "bedrooms": 3,
            "bathrooms": 3,
            "garages": 3,
            "description": "",
            "currency_id": 1,
            "price": 530000,
            "agent_id": 1,
        },
        {
            "operation_id": 2,
            "type_id": 1,
            "sublocation_id": 2,
            "size": 50,
            "bedrooms": 1,
            "bathrooms": 1,
            "garages": 1,
            "description": "",
            "currency_id": 1,
            "price": 130000,
            "agent_id": 2,
        },
        {
            "operation_id": 2,
            "type_id": 2,
            "sublocation_id": 3,
            "size": 280,
            "bedrooms": 4,
            "bathrooms": 3,
            "garages": 4,
            "description": "",
            "currency_id": 1,
            "price": 490000,
            "agent_id": 1,
        },
        {
            "operation_id": 2,
            "type_id": 1,
            "sublocation_id": 4,
            "size": 130,
            "bedrooms": 3,
            "bathrooms": 2,
            "garages": 3,
            "description": "",
            "currency_id": 1,
            "price": 230000,
            "agent_id": 2,
        },
        {
            "operation_id": 1,
            "type_id": 2,
            "sublocation_id": 5,
            "size": 280,
            "bedrooms": 4,
            "bathrooms": 3,
            "garages": 4,
            "description": "",
            "currency_id": 1,
            "price": 3000,
            "agent_id": 1,
        },
        {
            "operation_id": 2,
            "type_id": 2,
            "sublocation_id": 6,
            "size": 240,
            "bedrooms": 4,
            "bathrooms": 3,
            "garages": 4,
            "description": "",
            "currency_id": 1,
            "price": 330000,
            "agent_id": 1,
        },
        {
            "operation_id": 2,
            "type_id": 2,
            "sublocation_id": 3,
            "size": 320,
            "bedrooms": 4,
            "bathrooms": 3,
            "garages": 4,
            "description": "",
            "currency_id": 1,
            "price": 700000,
            "agent_id": 2,
        },
        {
            "operation_id": 2,
            "type_id": 3,
            "sublocation_id": 7,
            "size": 700,
            "bedrooms": 0,
            "bathrooms": 0,
            "garages": 0,
            "description": "",
            "currency_id": 1,
            "price": 375000,
            "agent_id": 2,
        },
    ]
    for property_data in properties_data:
        db.session.add(Property(**property_data))

    # Guarda los cambios en la base de datos
    db.session.commit()
