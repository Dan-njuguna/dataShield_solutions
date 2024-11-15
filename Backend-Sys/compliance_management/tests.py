from django.test import TestCase
from django.urls import reverse
from .models import DataProtectionRegulation, ComplianceStatus, ComplianceReport, ComplianceDocument, DataProcessingActivity, DPIA, Incident
from authentication.models import Organization, User

class DataProtectionRegulationModelTest(TestCase):
    """Test case for DataProtectionRegulation model."""

    def setUp(self):
        self.regulation = DataProtectionRegulation.objects.create(
            name="GDPR",
            jurisdiction="EU",
            description="General Data Protection Regulation"
        )

    def test_string_representation(self):
        """Test string representation of DataProtectionRegulation."""
        self.assertEqual(str(self.regulation), "GDPR")


class ComplianceStatusModelTest(TestCase):
    """Test case for ComplianceStatus model."""

    def setUp(self):
        self.organization = Organization.objects.create(name="Test Org")
        self.status = ComplianceStatus.objects.create(
            compliance_status="compliant",
            organization=self.organization,
            data_protection_regulations=None
        )

    def test_string_representation(self):
        """Test string representation of ComplianceStatus."""
        self.assertIn("compliant", str(self.status))


class ComplianceReportModelTest(TestCase):
    """Test case for ComplianceReport model."""

    def setUp(self):
        self.organization = Organization.objects.create(name="Test Org")
        self.report = ComplianceReport.objects.create(
            organization=self.organization,
            report_type="Annual Report",
            filters={"year": 2023},
            file="path/to/report.pdf"
        )

    def test_string_representation(self):
        """Test string representation of ComplianceReport."""
        self.assertIn("Annual Report", str(self.report))


class ComplianceDocumentModelTest(TestCase):
    """Test case for ComplianceDocument model."""

    def setUp(self):
        self.organization = Organization.objects.create(name="Test Org")
        self.document = ComplianceDocument.objects.create(
            organization=self.organization,
            title="Privacy Policy",
            document_type="Policy",
            file="path/to/document.pdf",
            uploaded_by=None
        )

    def test_string_representation(self):
        """Test string representation of ComplianceDocument."""
        self.assertEqual(str(self.document), "Privacy Policy")


class DataProcessingActivityModelTest(TestCase):
    """Test case for DataProcessingActivity model."""

    def setUp(self):
        self.organization = Organization.objects.create(name="Test Org")
        self.activity = DataProcessingActivity.objects.create(
            organization=self.organization,
            activity_name="Data Collection",
            purpose="Collecting user data",
            data_categories="Personal Data",
            data_subjects="Users",
            retention_period="1 year",
            security_measures="Encryption",
            is_high_risk=False
        )

    def test_string_representation(self):
        """Test string representation of DataProcessingActivity."""
        self.assertIn("Data Collection", str(self.activity))


class DPIAModelTest(TestCase):
    """Test case for DPIA model."""

    def setUp(self):
        self.organization = Organization.objects.create(name="Test Org")
        self.dpia = DPIA.objects.create(
            project_name="New Project",
            description="DPIA for new project",
            data_types={"personal_data": ["name", "email"]},
            risks={"risk": ["Data Breach"]},
            organization=self.organization
        )

    def test_string_representation(self):
        """Test string representation of DPIA."""
        self.assertEqual(str(self.dpia), "New Project")


class IncidentModelTest(TestCase):
    """Test case for Incident model."""

    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.incident = Incident.objects.create(
            description="Data breach incident",
            reported_by=self.user
        )

    def test_string_representation(self):
        """Test string representation of Incident."""
        self.assertEqual(str(self.incident), "Data breach incident")


class ComplianceStatusAPITest(TestCase):
    """Test case for ComplianceStatus API endpoint."""

    def setUp(self):
        self.organization = Organization.objects.create(name="Test Org")
        self.url = reverse('compliance_status-list')  # Corrected URL name

    def test_get_compliance_status_list(self):
        """Test GET method for compliance status list."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_post_compliance_status(self):
        """Test POST method for creating compliance status."""
        response = self.client.post(self.url, {
            'compliance_status': 'compliant',
            'organization': self.organization.id,
            'data_protection_regulations': None
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ComplianceStatus.objects.count(),  1)
        self.assertEqual(ComplianceStatus.objects.get().compliance_status, 'compliant')


class ComplianceReportAPITest(TestCase):
    """Test case for ComplianceReport API endpoint."""

    def setUp(self):
        self.organization = Organization.objects.create(name="Test Org")
        self.url = reverse('compliance_report-list')  # Corrected URL name

    def test_get_compliance_report_list(self):
        """Test GET method for compliance report list."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_post_compliance_report(self):
        """Test POST method for creating compliance report."""
        response = self.client.post(self.url, {
            'organization': self.organization.id,
            'report_type': 'Annual Report',
            'filters': {'year': 2023},
            'file': 'path/to/report.pdf'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ComplianceReport.objects.count(), 1)
        self.assertEqual(ComplianceReport.objects.get().report_type, 'Annual Report')


class ComplianceDocumentAPITest(TestCase):
    """Test case for ComplianceDocument API endpoint."""

    def setUp(self):
        self.organization = Organization.objects.create(name="Test Org")
        self.url = reverse('compliance_document-list')

    def test_get_compliance_document_list(self):
        """Test GET method for compliance document list."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_post_compliance_document(self):
        """Test POST method for creating compliance document."""
        response = self.client.post(self.url, {
            'organization': self.organization.id,
            'title': 'Privacy Policy',
            'document_type': 'Policy',
            'file': 'path/to/document.pdf',
            'uploaded_by': None
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ComplianceDocument.objects.count(), 1)
        self.assertEqual(ComplianceDocument.objects.get().title, 'Privacy Policy')


