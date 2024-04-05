from concurrent import futures
import random
import grpc
from recommendations.recommendations_pb2 import (
    BookCategory,
    BookRecommendation,
    RecommendationResponse
)

from recommendations import recommendations_pb2_grpc

books_by_category = {
    
    BookCategory.MYSTERY : [
        BookRecommendation(id=1, title="harry_potter"),
        BookRecommendation(id=2, title="d & g"),
        BookRecommendation(id=3, title="loard of the ring"),
        BookRecommendation(id=4, title="The Maltese Falcon"),
        BookRecommendation(id=5, title="Murder on the Orient Express"),
        BookRecommendation(id=6, title="The Hound of the Baskervilles")
    ],
    BookCategory.SELF_HELP : [
        BookRecommendation(id=7 , title="48 power"),
        BookRecommendation(id=8 , title="dan luck"),
        BookRecommendation(id=9, title="The 7 Habits of Highly Effective People"),
        BookRecommendation(id=10, title="How to Win Friends and Influence People"),
        BookRecommendation(id=11, title="Man's Search for Meaning"),
    ],
    BookCategory.SCIENCE_FICTION : [
        BookRecommendation(id=12, title="The Hitchhiker's Guide to the Galaxy"),
        BookRecommendation(id=13, title="Ender's Game"),
        BookRecommendation(id=14, title="The Dune Chronicles"),
        BookRecommendation(id=15 , title="python"),
        BookRecommendation(id=16 , title="fluent")
    ]
}
 
class RecommendationService(recommendations_pb2_grpc.RecommendationsServicer):
    
    def Recommend(self, request, context):
        if request.category not in books_by_category:
            context.abort(grpc.StatusCode.NOT_FOUND ,"category not founded !")
        
        books = books_by_category[request.category]
        count = min(request.max_results ,len(books))
        result_list = random.sample(books,count)
        
        return RecommendationResponse(recommendations=result_list)