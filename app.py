from flask import Flask, jsonify,request
from models import Bank as BankModel, Branch as BranchModel
from database import SessionLocal

app = Flask(__name__)

def get_db():
    # Provides a database session.
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# route for access all banks 
@app.route("/banks/", methods=["GET"])
def read_banks():
    db = next(get_db())
    banks = db.query(BankModel).all()
    return jsonify([{"id": bank.id, "name": bank.name} for bank in banks])


# route for access branches 
@app.route("/branches/", methods=["GET"])
def read_branches():
    db = next(get_db())

    # pagination
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 500, type=int) # 500 limit for per page
    offset = (page - 1) * per_page
    branches_query = db.query(BranchModel).offset(offset).limit(per_page)
    branches = branches_query.all()
    return jsonify({
        "page": page,
        "per_page": per_page,
        "branches": [
            {
                "id": branch.id,
                "ifsc": branch.ifsc,
                "branch": branch.branch,
                "address": branch.address,
                "city": branch.city,
                "district": branch.district,
                "state": branch.state,
                "bank": branch.bank.name,
                "bank id": branch.bank.id
            }
            for branch in branches
        ]
    })



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
