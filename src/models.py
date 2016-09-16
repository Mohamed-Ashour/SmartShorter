from mongoframes import Frame, SubFrame


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


# class IOS(SubFrame):
#
#     _fields = {
#         "primary",
#         "fallback"
#     }
#
#
# class Android(SubFrame):
#
#     _fields = {
#         "primary",
#         "fallback"
#     }


########## Testing ##############

# from mongoframes import Frame
# from pymongo import MongoClient
#
# Frame._client = MongoClient("mongodb://127.0.0.1:27017/SmartShorter")
#
# Link({
#       "slug": "s5G1f3",
#       "ios": {
#         "primary": "http://...",
#         "fallback": "http://..."
#       },
#       "android": {
#         "primary": "http://...",
#         "fallback": "http://..."
#       },
#       "web": "http://..."
#     }).insert()