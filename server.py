

from concurrent import futures
from recommendations import recommendations_pb2_grpc
from recommendations.backed_recommendations import RecommendationService
import grpc

def serve():
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    recommendations_pb2_grpc.add_RecommendationsServicer_to_server(
        RecommendationService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()