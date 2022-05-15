from config import config
import os
from flask import Flask, render_template
import grpc
from recommendations.recommendations_pb2 import BookCategory, RecommendationRequest

from recommendations.recommendations_pb2_grpc import RecommendationsStub


def create_app(config_name: str = "dev") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config.get(config_name))

    recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
    recommendations_channel = grpc.insecure_channel(f"{recommendations_host}:50051")
    recommendations_client = RecommendationsStub(recommendations_channel)

    @app.route("/")
    def render_homepage():
        recommendations_request = RecommendationRequest(
            user_id=1, category=BookCategory.MYSTERY, max_results=3
        )
        recommendations_response = recommendations_client.Recommend(
            recommendations_request
        )
        return render_template(
            "homepage.html",
            recommendations=recommendations_response.recommendations,
        )

    return app
