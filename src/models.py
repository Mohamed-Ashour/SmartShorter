from mongoframes import Frame


class Link(Frame):

    _collection = "links"

    _fields = {
        "slug",
        "ios",
        "android",
        "web"
    }
    _private_fields = {
        "_id"
    }
