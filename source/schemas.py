from marshmallow import Schema, fields


class WeightSchema(Schema):
    mass_kg = fields.Int()
    last_measured = fields.DateTime()


class FeedingSchema(Schema):
    amount_kg = fields.Int()
    cron_schedule = fields.Str()
    last_measured = fields.DateTime()


class MilkProductionSchema(Schema):
    last_milk = fields.DateTime()
    cron_schedule = fields.Str()
    amount_l = fields.Int()


class CowSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    sex = fields.Str()
    birthdate = fields.DateTime()
    condition = fields.Str()
    weight = fields.Nested(WeightSchema)
    feeding = fields.Nested(FeedingSchema)
    milk_production = fields.Nested(MilkProductionSchema)
    has_calves = fields.Bool()


cow_schema = CowSchema()
cows_schema = CowSchema(many=True)
