from flask import Flask, Blueprint, jsonify, request

# from v1.api import api_bp
import arxiv

# from v1.utils import create_response

app = Flask(__name__)

# app.register_blueprint(api_bp, url_prefix="/api/v1")


@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/v1/arxiv/search")
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

        # return create_response(success=True, data=results)
        response = {"success": True, "data": results, "errors": None}
        return jsonify(response), 200

    except Exception as e:
        # return create_response(success=False, errors=str(e), status_code=500)
        response = {"success": False, "data": None, "errors": str(e)}
        return jsonify(response), 500
