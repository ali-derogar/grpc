from recommendations.recommendations_pb2 import BookCategory , RecommendationRequest
from recommendations.recommendations_pb2_grpc import RecommendationsStub
from grpc import insecure_channel

server_channel = insecure_channel("localhost:50051")
client = RecommendationsStub(server_channel)
request = RecommendationRequest(
    user_id = 12 , category = BookCategory.MYSTERY , max_results = 12
)
client.Recommend(request)


