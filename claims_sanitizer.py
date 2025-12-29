import csv
import random
import datetime

class ClaimsSanitizer:
    """
    Generates mock claims data matching the 'Standard Claims Export.csv' schema.
    Specifically designed to provide realistic but fake financial and clinical data.
    """

    def __init__(self):
        self.first_names = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda"]
        self.last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"]
        self.cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"]
        self.states = ["NY", "CA", "IL", "TX", "AZ", "PA"]
        
        self.providers = [
            "General Hospital", "City Medical Center", "Valley Clinic", "Dr. Smith Practice", "Imaging Center North"
        ]
        
        self.diag_codes = ["J0190", "E119", "I10", "Z0000", "M545", "R05"]
        self.proc_codes = ["99213", "99214", "71045", "85025", "99203"]

    def _random_date(self, start_year=2024, end_year=2025):
        start = datetime.date(start_year, 1, 1)
        end = datetime.date(end_year, 12, 31)
        return start + datetime.timedelta(days=random.randint(0, (end - start).days))

    def generate_row(self, index):
        """Generates a single dictionary representing a Claims CSV row."""
        
        charges = round(random.uniform(100.00, 5000.00), 2)
        allowed = round(charges * random.uniform(0.6, 0.9), 2)
        deductible = round(random.uniform(0, 100), 2)
        copay = random.choice([0, 20, 25, 50])
        coinsurance = round((allowed - deductible - copay) * 0.2, 2)
        paid = round(allowed - deductible - copay - coinsurance, 2)
        
        if paid < 0: paid = 0
        
        svc_start = self._random_date()
        svc_end = svc_start + datetime.timedelta(days=random.randint(0, 5))
        
        row = {
            "RecordType": "C",
            "GroupNumber": "8030",
            "GroupName": "Fort Wayne Medical Oncology",
            "DivisionName": "Active",
            "SubscriberID": f"SUB{random.randint(10000,99999)}",
            "SubscriberTIN": f"9{random.randint(10000000,99999999)}",
            "SubscriberLastName": random.choice(self.last_names),
            "SubscriberFirstName": random.choice(self.first_names),
            "SubscriberMiddleName": "",
            "SubscriberNameSuffix": "",
            "SubscriberBirthDate": "19800101",
            "PatientID": f"PAT{random.randint(10000,99999)}",
            "PatientTIN": f"9{random.randint(10000000,99999999)}",
            "PatientLastName": random.choice(self.last_names),
            "PatientFirstName": random.choice(self.first_names),
            "PatientMiddleName": "",
            "PatientNameSuffix": "",
            "PatientBirthDate": "20100505",
            "PatientGender": random.choice(["M", "F"]),
            "PatientRelationship": "18",
            "ProviderTIN": f"1{random.randint(10000000,99999999)}",
            "ProviderNPI": f"1{random.randint(100000000,999999999)}",
            "ProviderFullName": random.choice(self.providers),
            "ProviderAddress": "123 Med Way",
            "ProviderAddress2": "",
            "ProviderCity": random.choice(self.cities),
            "ProviderState": random.choice(self.states),
            "ProviderPostalCode": "10001",
            "ClaimType": "P", # Professional
            "ClaimNumber": f"CLM{random.randint(100000,999999)}",
            "ClaimLineNumber": "1",
            "BenefitTypeDescription": "Medical",
            "NetworkStatus": "IN",
            "NetworkName": "PPO",
            "ServiceStartDate": svc_start.strftime("%Y%m%d"),
            "ServiceEndDate": svc_end.strftime("%Y%m%d"),
            "PlaceOfService": "11", # Office
            "TypeOfBill": "",
            "NumberOfServices": "1",
            "DaysSupply": "",
            "DiagnosisCode1": random.choice(self.diag_codes),
            "DiagnosisCode2": "",
            "DiagnosisCode3": "",
            "DiagnosisCode4": "",
            "ProcedureCode1Qualifier": "HC",
            "ProcedureCode1": random.choice(self.proc_codes),
            "ProcedureCode2Qualifier": "",
            "ProcedureCode2": "",
            "ServiceModifier1": "",
            "ServiceModifier2": "",
            "DRGCode": "",
            "ChargesSubmitted": f"{charges:.2f}",
            "AllowedAmount": f"{allowed:.2f}",
            "NotCoveredTotal": f"{charges - allowed:.2f}",
            "CoPay": f"{copay:.2f}",
            "Deductible": f"{deductible:.2f}",
            "Coinsurance": f"{coinsurance:.2f}",
            "COBSavings": "0.00",
            "OtherInsuranceBenefit": "0.00",
            "BenefitCode": "",
            "BenefitCodeDescription": "",
            "TotalPaid": f"{paid:.2f}",
            "PayeeType": "P",
            "ReceivedDate": (svc_end + datetime.timedelta(days=2)).strftime("%Y%m%d"),
            "ProcessedDate": (svc_end + datetime.timedelta(days=5)).strftime("%Y%m%d"),
            "PaidDate": (svc_end + datetime.timedelta(days=7)).strftime("%Y%m%d"),
            "PatientAccount": "",
            "DrugCode": "",
            "DrugQuantity": "",
            "FormularyIndicator": "",
            "MailOrderIndicator": "",
            "BrandIndicator": "",
            "PayeeTIN": "",
            "PayeeName": "",
            "PayeeAddress": "",
            "PayeeAddress2": "",
            "PayeeCity": "",
            "PayeeState": "",
            "PayeePostalCode": "",
            "ProcedureCPT": "",
            "ClaimExCode1": "",
            "ClaimExCode1Description": "",
            "ClaimExCode1CARC": "",
            "ClaimExCode1RARC": "",
            # ... skipping many empty ex codes for brevity ...
            "Voided": "N",
            "SpecialtyCode": "",
            "SpecialtyDescription": "",
            "SubscriberAddress": "123 Main St",
            "SubscriberAddress2": "",
            "SubscriberCity": "City",
            "SubscriberState": "ST",
            "SubscriberPostalCode": "00000",
            "RevenueCode": "",
            "PlanID": "HLT",
            "PlanDescription": "Medical Plan"
        }
        return row

    def generate_file(self, filename, count=50):
        # Full header list based on analysis
        fieldnames = [
            "RecordType","GroupNumber","GroupName","DivisionName","SubscriberID","SubscriberTIN","SubscriberLastName","SubscriberFirstName","SubscriberMiddleName","SubscriberNameSuffix","SubscriberBirthDate","PatientID","PatientTIN","PatientLastName","PatientFirstName","PatientMiddleName","PatientNameSuffix","PatientBirthDate","PatientGender","PatientRelationship","ProviderTIN","ProviderNPI","ProviderFullName","ProviderAddress","ProviderAddress2","ProviderCity","ProviderState","ProviderPostalCode","ClaimType","ClaimNumber","ClaimLineNumber","BenefitTypeDescription","NetworkStatus","NetworkName","ServiceStartDate","ServiceEndDate","PlaceOfService","TypeOfBill","NumberOfServices","DaysSupply","DiagnosisCode1","DiagnosisCode2","DiagnosisCode3","DiagnosisCode4","ProcedureCode1Qualifier","ProcedureCode1","ProcedureCode2Qualifier","ProcedureCode2","ServiceModifier1","ServiceModifier2","DRGCode","ChargesSubmitted","AllowedAmount","NotCoveredTotal","CoPay","Deductible","Coinsurance","COBSavings","OtherInsuranceBenefit","BenefitCode","BenefitCodeDescription","TotalPaid","PayeeType","ReceivedDate","ProcessedDate","PaidDate","PatientAccount","DrugCode","DrugQuantity","FormularyIndicator","MailOrderIndicator","BrandIndicator","PayeeTIN","PayeeName","PayeeAddress","PayeeAddress2","PayeeCity","PayeeState","PayeePostalCode","ProcedureCPT","ClaimExCode1","ClaimExCode1Description","ClaimExCode1CARC","ClaimExCode1RARC","ClaimExCode2","ClaimExCode2Description","ClaimExCode2CARC","ClaimExCode2RARC","ClaimExCode3","ClaimExCode3Description","ClaimExCode3CARC","ClaimExCode3RARC","ClaimExCode4","ClaimExCode4Description","ClaimExCode4CARC","ClaimExCode4RARC","ClaimDetailExCode1","ClaimDetailExCode1Description","ClaimDetailExCode1CARC","ClaimDetailExCode1RARC","ClaimDetailExCode2","ClaimDetailExCode2Description","ClaimDetailExCode2CARC","ClaimDetailExCode2RARC","ClaimDetailExCode3","ClaimDetailExCode3Description","ClaimDetailExCode3CARC","ClaimDetailExCode3RARC","Voided","SpecialtyCode","SpecialtyDescription","SubscriberAddress","SubscriberAddress2","SubscriberCity","SubscriberState","SubscriberPostalCode","RevenueCode","PlanID","PlanDescription"
        ]
        
        print(f"Generating {count} mock claims to {filename}...")
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            for i in range(count):
                writer.writerow(self.generate_row(i))
        print("Done.")

if __name__ == "__main__":
    generator = ClaimsSanitizer()
    generator.generate_file("mock_claims_data.csv", 30)
