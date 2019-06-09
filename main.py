# endpoint to create new user
from flask import jsonify
from webargs.flaskparser import use_args

from app.config import app
from app.models import db, Clothing
from app.schemas import ClothingSchema, ClothingRawSchema


@app.route("/clothing", methods=["POST"])
@use_args(ClothingSchema(exclude=("id",)))
def add_clothing(clothing):
    if not isinstance(clothing, Clothing):
        return jsonify(error="Error validating object")

    db.session.add(clothing)
    db.session.commit()
    return ClothingSchema().dumps(clothing).data


# endpoint to show all users
@app.route("/clothing", methods=["GET"])
def get_clothing():
    obj_list = Clothing.query.all()
    return ClothingSchema(many=True).dumps(obj_list).data


# endpoint to get user detail by id
@app.route("/clothing/<int:obj_id>", methods=["GET"])
def clothing_detail(obj_id):
    obj = Clothing.query.get(obj_id)
    return ClothingSchema().dumps(obj)


# endpoint to update user
@app.route("/clothing/<int:obj_id>", methods=["PUT"])
@use_args(ClothingRawSchema(exclude=("id",)))
def clothing_update(data, obj_id):
    clothing = Clothing.query.get(obj_id)

    if clothing is None:
        return jsonify(error="Object doesn't exist")

    for x in ClothingSchema.UPDATE_FIELDS:
        setattr(clothing, x, data[x])

    db.session.add(clothing)
    db.session.commit()

    return ClothingSchema().dumps(clothing).data


# endpoint to delete user
@app.route("/clothing/<int:obj_id>", methods=["DELETE"])
def clothign_delete(obj_id):
    obj = Clothing.query.get(obj_id)

    if obj is None:
        return jsonify(error="Clothing object Does Not Exist")

    db.session.delete(obj)
    db.session.commit()

    return ClothingSchema().dumps(obj).data


if __name__ == "__main__":
    app.run(port=8080)
