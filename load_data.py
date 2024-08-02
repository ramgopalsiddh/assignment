import csv
from models import Bank, Branch
from database import SessionLocal

def load_data():
    db = SessionLocal()
    
    with open('banks.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        banks = {}
        
        for row in reader:
            bank = Bank(id=row['id'], name=row['name'])
            db.add(bank)
            banks[row['id']] = bank
    
    with open('bank_branches.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            branch = Branch(
                ifsc=row['ifsc'],
                branch=row['branch'],
                address=row['address'],
                city=row['city'],
                district=row['district'],
                state=row['state'],
                bank_id=row['bank_id']
            )
            db.add(branch)
    
    db.commit()
    db.close()

if __name__ == "__main__":
    load_data()
