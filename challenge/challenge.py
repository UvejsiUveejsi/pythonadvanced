# {
#     "book1": {
#         "title": "Lord of the rings",
#         "Author": "Miloti",
#         "Year": "2012",
#         "genre": "Science Fiction"
#     },
#     "book2": {
#         "title": "God delusion",
#         "Author": "Uvejsi",
#         "Year": "2006",
#         "genre": "Science"
#     },
#     "book3": {
#         "title": "Harry Potter",
#         "Author": "Dreni",
#         "Year": "2023",
#         "genre": "Science Fiction"
#     },
# }


from fastapi import FastAPI
app = FastAPI()
@app.get("/")

def root():
    return {

            "book1": {
                "title": "Lord of the rings",
                "Author": "Miloti",
                "Year": "2012",
                "genre": "Science Fiction"
            },
            "book2": {
                "title": "God delusion",
                "Author": "Uvejsi",
                "Year": "2006",
                "genre": "Science"
            },
            "book3": {
                "title": "Harry Potter",
                "Author": "Dreni",
                "Year": "2023",
                "genre": "Science Fiction"
            },
        }
    