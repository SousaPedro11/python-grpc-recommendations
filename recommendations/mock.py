from recommendations.recommendations_pb2 import BookCategory, BookRecommendation


books_by_category = {
    BookCategory.MYSTERY: [
        BookRecommendation(id=1, title="The Maltese Falcon"),
        BookRecommendation(id=2, title="Murder on the Orient Express"),
        BookRecommendation(id=3, title="The Hound of the Baskervilles"),
    ],
    BookCategory.SCIENCE_FICTION: [
        BookRecommendation(id=4, title="The Hitchhiker's Guide to the Galaxy"),
        BookRecommendation(id=5, title="Ender's Game"),
        BookRecommendation(id=6, title="The Dune Chronicles"),
    ],
    BookCategory.SELF_HELP: [
        BookRecommendation(id=7, title="The 7 Habits of Highly Effective People"),
        BookRecommendation(id=8, title="How to Win Friends and Influence People"),
        BookRecommendation(id=9, title="Man's Search for Meaning"),
    ],
}
