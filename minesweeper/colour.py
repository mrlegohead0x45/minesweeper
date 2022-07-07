import attrs


@attrs.define
class Colour:
    red: int = attrs.field(
        default=0,
        validator=[
            attrs.validators.instance_of(int),
            attrs.validators.le(255),
            attrs.validators.ge(0),
        ],
    )
    green: int = attrs.field(
        default=0,
        validator=[
            attrs.validators.instance_of(int),
            attrs.validators.le(255),
            attrs.validators.ge(0),
        ],
    )
    blue: int = attrs.field(
        default=0,
        validator=[
            attrs.validators.instance_of(int),
            attrs.validators.le(255),
            attrs.validators.ge(0),
        ],
    )
