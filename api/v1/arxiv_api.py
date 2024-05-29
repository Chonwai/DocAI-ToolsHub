# v1/arxiv_api.py
from flask import Blueprint, jsonify, request
from api.utils import create_response
import arxiv

arxiv_bp = Blueprint("arxiv_bp", __name__)


@arxiv_bp.route("/search", methods=["GET"])
def search_arxiv():
    query = request.args.get("query", default="")
    max_results = request.args.get("max_results", default=10, type=int)

    try:
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate,
        )

        results = []
        for result in search.results():
            results.append(
                {
                    "title": result.title,
                    "authors": [author.name for author in result.authors],
                    "summary": result.summary,
                    "published": result.published.strftime("%Y-%m-%d"),
                    "pdf_url": result.pdf_url,
                }
            )

        return create_response(success=True, data=results)

    except Exception as e:
        return create_response(success=False, errors=str(e), status_code=500)
