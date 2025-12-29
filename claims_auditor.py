import csv
import json
from datetime import datetime

class ClaimsAuditor:
    def __init__(self, input_csv):
        self.input_csv = input_csv
        self.report = {
            "total_claims_processed": 0,
            "passed_claims": 0,
            "failed_claims": 0,
            "errors": [],
            "summary_stats": {
                "total_charges": 0.0,
                "total_paid": 0.0,
                "unique_providers": set(),
                "top_diagnosis_codes": {}
            }
        }

    def _parse_date(self, date_str):
        if not date_str: return None
        try:
            return datetime.strptime(date_str, "%Y%m%d")
        except ValueError:
            return None

    def _parse_float(self, money_str):
        if not money_str: return 0.0
        try:
            return float(money_str)
        except ValueError:
            return 0.0

    def run_audit(self):
        print(f"Auditing {self.input_csv}...")
        
        with open(self.input_csv, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                self.report["total_claims_processed"] += 1
                errors = self._audit_claim(row)
                
                # Stats aggregation
                self.report["summary_stats"]["total_charges"] += self._parse_float(row.get("ChargesSubmitted"))
                self.report["summary_stats"]["total_paid"] += self._parse_float(row.get("TotalPaid"))
                self.report["summary_stats"]["unique_providers"].add(row.get("ProviderFullName"))
                
                diag1 = row.get("DiagnosisCode1")
                if diag1:
                    self.report["summary_stats"]["top_diagnosis_codes"][diag1] = \
                        self.report["summary_stats"]["top_diagnosis_codes"].get(diag1, 0) + 1
                
                if errors:
                    self.report["failed_claims"] += 1
                    self.report["errors"].append({
                        "ClaimNumber": row.get("ClaimNumber"),
                        "Issues": errors
                    })
                else:
                    self.report["passed_claims"] += 1
                    
        self._print_report()

    def _audit_claim(self, row):
        errors = []
        
        # Rule 1: Service Dates
        start = self._parse_date(row.get("ServiceStartDate"))
        end = self._parse_date(row.get("ServiceEndDate"))
        
        if not start:
            errors.append("Missing ServiceStartDate")
        if not end:
            errors.append("Missing ServiceEndDate")
        if start and end and end < start:
            errors.append(f"ServiceEndDate ({end.date()}) is before ServiceStartDate ({start.date()})")
            
        # Rule 2: Financial Integrity
        charges = self._parse_float(row.get("ChargesSubmitted"))
        allowed = self._parse_float(row.get("AllowedAmount"))
        paid = self._parse_float(row.get("TotalPaid"))
        
        if allowed > charges:
             errors.append(f"AllowedAmount ({allowed}) > ChargesSubmitted ({charges})")
        if paid > allowed:
             errors.append(f"TotalPaid ({paid}) > AllowedAmount ({allowed})")
             
        # Rule 3: Data Completeness
        if not row.get("DiagnosisCode1"):
            errors.append("Missing Primary Diagnosis Code")
            
        return errors

    def _print_report(self):
        print("\n" + "="*40)
        print("CLAIMS AUDIT REPORT")
        print("="*40)
        print(f"Total Processed: {self.report['total_claims_processed']}")
        print(f"Passed: {self.report['passed_claims']}")
        print(f"Failed: {self.report['failed_claims']}")
        print("-" * 20)
        print(f"Total Charges: ${self.report['summary_stats']['total_charges']:,.2f}")
        print(f"Total Paid:    ${self.report['summary_stats']['total_paid']:,.2f}")
        print(f"Unique Providers: {len(self.report['summary_stats']['unique_providers'])}")
        print("-" * 20)
        
        if self.report["errors"]:
            print("\nFAILED CLAIMS DETAILS (Top 5):")
            for err in self.report["errors"][:5]:
                print(f"Claim {err['ClaimNumber']}: {', '.join(err['Issues'])}")
                
        # Generate JSON artifact
        # Convert set to list for serializable format
        self.report["summary_stats"]["unique_providers"] = list(self.report["summary_stats"]["unique_providers"])
        with open("audit_report.json", "w") as f:
            json.dump(self.report, f, indent=4)
        print("\nFull report saved to 'audit_report.json'")

if __name__ == "__main__":
    auditor = ClaimsAuditor("mock_claims_data.csv")
    auditor.run_audit()
