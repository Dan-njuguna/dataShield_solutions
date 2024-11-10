Search.setIndex({"alltitles": {"Analytics Documentation": [[0, null]], "Audit Log Documentation": [[1, null]], "Authentication Documentation": [[2, null]], "Compliance Management Documentation": [[3, null]], "Contents": [[5, "contents"]], "Contents:": [[5, null]], "Core\u2019s Documentation": [[4, null]], "Datashield Solutions Documentation": [[5, null]], "Getting Started": [[5, "getting-started"]], "Indices and Tables": [[5, "indices-and-tables"]], "Ingestion Documentation": [[6, null]], "Reporting Documentation": [[8, null]]}, "docnames": ["analytics/index", "audit_log/index", "authentication/index", "compliance_management/index", "core/index", "index", "ingestion/index", "policy_management/index", "reporting/index"], "envversion": {"sphinx": 64, "sphinx.domains.c": 3, "sphinx.domains.changeset": 1, "sphinx.domains.citation": 1, "sphinx.domains.cpp": 9, "sphinx.domains.index": 1, "sphinx.domains.javascript": 3, "sphinx.domains.math": 2, "sphinx.domains.python": 4, "sphinx.domains.rst": 2, "sphinx.domains.std": 2, "sphinx.ext.viewcode": 1}, "filenames": ["analytics\\index.rst", "audit_log\\index.rst", "authentication\\index.rst", "compliance_management\\index.rst", "core\\index.rst", "index.rst", "ingestion\\index.rst", "policy_management\\index.rst", "reporting\\index.rst"], "indexentries": {}, "objects": {"analytics": [[0, 0, 0, "-", "routing"], [0, 0, 0, "-", "tasks"], [0, 0, 0, "-", "views"]], "analytics.views": [[0, 1, 1, "", "metrics_view"]], "audit_log": [[1, 0, 0, "-", "forms"], [1, 0, 0, "-", "models"], [1, 0, 0, "-", "views"]], "audit_log.forms": [[1, 2, 1, "", "AuditLogForm"]], "audit_log.forms.AuditLogForm": [[1, 2, 1, "", "Meta"], [1, 3, 1, "", "base_fields"], [1, 3, 1, "", "declared_fields"], [1, 4, 1, "", "media"]], "audit_log.forms.AuditLogForm.Meta": [[1, 3, 1, "", "fields"], [1, 3, 1, "", "model"]], "audit_log.models": [[1, 2, 1, "", "AuditLog"]], "audit_log.models.AuditLog": [[1, 3, 1, "", "ACTION_CHOICES"], [1, 5, 1, "", "DoesNotExist"], [1, 5, 1, "", "MultipleObjectsReturned"], [1, 3, 1, "", "action"], [1, 3, 1, "", "action_description"], [1, 3, 1, "", "additional_data"], [1, 3, 1, "", "affected_resource"], [1, 3, 1, "", "compliance_notes"], [1, 3, 1, "", "created_at"], [1, 6, 1, "", "get_action_display"], [1, 6, 1, "", "get_next_by_created_at"], [1, 6, 1, "", "get_previous_by_created_at"], [1, 3, 1, "", "id"], [1, 3, 1, "", "ip_address"], [1, 3, 1, "", "is_compliant"], [1, 6, 1, "", "log_action"], [1, 3, 1, "", "objects"], [1, 3, 1, "", "organization"], [1, 3, 1, "", "organization_id"], [1, 3, 1, "", "user"], [1, 3, 1, "", "user_id"]], "audit_log.views": [[1, 1, 1, "", "audit_log_detail"], [1, 1, 1, "", "audit_log_list"], [1, 1, 1, "", "log_action_view"]], "authentication": [[2, 0, 0, "-", "forms"], [2, 0, 0, "-", "models"], [2, 0, 0, "-", "views"]], "authentication.forms": [[2, 2, 1, "", "OrganizationRegistrationForm"], [2, 2, 1, "", "UserRegistrationForm"]], "authentication.forms.OrganizationRegistrationForm": [[2, 2, 1, "", "Meta"], [2, 3, 1, "", "base_fields"], [2, 3, 1, "", "declared_fields"], [2, 4, 1, "", "media"]], "authentication.forms.OrganizationRegistrationForm.Meta": [[2, 3, 1, "", "fields"], [2, 3, 1, "", "model"]], "authentication.forms.UserRegistrationForm": [[2, 2, 1, "", "Meta"], [2, 3, 1, "", "base_fields"], [2, 3, 1, "", "declared_fields"], [2, 4, 1, "", "media"], [2, 6, 1, "", "save"]], "authentication.forms.UserRegistrationForm.Meta": [[2, 3, 1, "", "fields"], [2, 3, 1, "", "model"], [2, 3, 1, "", "widgets"]], "authentication.models": [[2, 2, 1, "", "Organization"], [2, 2, 1, "", "User"], [2, 2, 1, "", "UserManager"]], "authentication.models.Organization": [[2, 5, 1, "", "DoesNotExist"], [2, 5, 1, "", "MultipleObjectsReturned"], [2, 3, 1, "", "address"], [2, 3, 1, "", "auditlog_set"], [2, 3, 1, "", "company_size"], [2, 3, 1, "", "complianceaudit_set"], [2, 3, 1, "", "compliancedocument_set"], [2, 3, 1, "", "compliancereport_set"], [2, 3, 1, "", "compliancestatus_set"], [2, 3, 1, "", "contact_email"], [2, 3, 1, "", "contact_number"], [2, 3, 1, "", "contact_person"], [2, 3, 1, "", "created_at"], [2, 3, 1, "", "databreachreport_set"], [2, 3, 1, "", "dataprocessingactivity_set"], [2, 3, 1, "", "dpia_set"], [2, 6, 1, "", "get_next_by_created_at"], [2, 6, 1, "", "get_next_by_updated_at"], [2, 6, 1, "", "get_previous_by_created_at"], [2, 6, 1, "", "get_previous_by_updated_at"], [2, 3, 1, "", "id"], [2, 3, 1, "", "industry"], [2, 3, 1, "", "name"], [2, 3, 1, "", "objects"], [2, 6, 1, "", "save"], [2, 3, 1, "", "scheduledreport_set"], [2, 3, 1, "", "slug"], [2, 3, 1, "", "updated_at"], [2, 3, 1, "", "users"]], "authentication.models.User": [[2, 5, 1, "", "DoesNotExist"], [2, 5, 1, "", "MultipleObjectsReturned"], [2, 3, 1, "", "REQUIRED_FIELDS"], [2, 3, 1, "", "USERNAME_FIELD"], [2, 3, 1, "", "approvalworkflow_set"], [2, 3, 1, "", "auditlog_set"], [2, 3, 1, "", "complianceaudit_set"], [2, 3, 1, "", "compliancedocument_set"], [2, 3, 1, "", "created_at"], [2, 3, 1, "", "email"], [2, 3, 1, "", "first_name"], [2, 6, 1, "", "get_full_name"], [2, 6, 1, "", "get_next_by_created_at"], [2, 6, 1, "", "get_next_by_updated_at"], [2, 6, 1, "", "get_previous_by_created_at"], [2, 6, 1, "", "get_previous_by_updated_at"], [2, 6, 1, "", "get_short_name"], [2, 3, 1, "", "groups"], [2, 3, 1, "", "id"], [2, 3, 1, "", "incident_set"], [2, 3, 1, "", "is_active"], [2, 3, 1, "", "is_staff"], [2, 3, 1, "", "is_superuser"], [2, 3, 1, "", "last_login"], [2, 3, 1, "", "last_name"], [2, 3, 1, "", "objects"], [2, 3, 1, "", "organization"], [2, 3, 1, "", "organization_id"], [2, 3, 1, "", "password"], [2, 3, 1, "", "policy_set"], [2, 3, 1, "", "policyversion_set"], [2, 6, 1, "", "save"], [2, 3, 1, "", "slug"], [2, 3, 1, "", "updated_at"], [2, 3, 1, "", "user_permissions"]], "authentication.models.UserManager": [[2, 6, 1, "", "create_superuser"], [2, 6, 1, "", "create_user"]], "authentication.views": [[2, 1, 1, "", "organization_detail"], [2, 1, 1, "", "organization_list"], [2, 1, 1, "", "organization_register"], [2, 1, 1, "", "user_detail"], [2, 1, 1, "", "user_list"], [2, 1, 1, "", "user_login"], [2, 1, 1, "", "user_register"]], "compliance_management": [[3, 0, 0, "-", "models"], [3, 0, 0, "-", "views"]], "compliance_management.models": [[3, 2, 1, "", "ComplianceDocument"], [3, 2, 1, "", "ComplianceReport"], [3, 2, 1, "", "ComplianceStatus"], [3, 2, 1, "", "DPIA"], [3, 2, 1, "", "DataProcessingActivity"], [3, 2, 1, "", "DataProtectionRegulation"], [3, 2, 1, "", "Incident"], [3, 2, 1, "", "KenyaDPA"]], "compliance_management.models.ComplianceDocument": [[3, 5, 1, "", "DoesNotExist"], [3, 5, 1, "", "MultipleObjectsReturned"], [3, 3, 1, "", "document_type"], [3, 3, 1, "", "expiry_date"], [3, 3, 1, "", "file"], [3, 6, 1, "", "get_next_by_upload_date"], [3, 6, 1, "", "get_previous_by_upload_date"], [3, 3, 1, "", "id"], [3, 3, 1, "", "objects"], [3, 3, 1, "", "organization"], [3, 3, 1, "", "organization_id"], [3, 3, 1, "", "title"], [3, 3, 1, "", "upload_date"], [3, 3, 1, "", "uploaded_by"], [3, 3, 1, "", "uploaded_by_id"]], "compliance_management.models.ComplianceReport": [[3, 5, 1, "", "DoesNotExist"], [3, 5, 1, "", "MultipleObjectsReturned"], [3, 3, 1, "", "file"], [3, 3, 1, "", "filters"], [3, 3, 1, "", "generated_at"], [3, 6, 1, "", "get_next_by_generated_at"], [3, 6, 1, "", "get_previous_by_generated_at"], [3, 3, 1, "", "id"], [3, 3, 1, "", "objects"], [3, 3, 1, "", "organization"], [3, 3, 1, "", "organization_id"], [3, 3, 1, "", "report_type"]], "compliance_management.models.ComplianceStatus": [[3, 3, 1, "", "COMPLIANCE_STATUS_CHOICES"], [3, 5, 1, "", "DoesNotExist"], [3, 5, 1, "", "MultipleObjectsReturned"], [3, 3, 1, "", "compliance_status"], [3, 3, 1, "", "data_protection_regulations"], [3, 3, 1, "", "data_protection_regulations_id"], [3, 6, 1, "", "get_compliance_status_display"], [3, 6, 1, "", "get_next_by_last_checked_at"], [3, 6, 1, "", "get_previous_by_last_checked_at"], [3, 3, 1, "", "id"], [3, 3, 1, "", "last_checked_at"], [3, 3, 1, "", "objects"], [3, 3, 1, "", "organization"], [3, 3, 1, "", "organization_id"]], "compliance_management.models.DPIA": [[3, 5, 1, "", "DoesNotExist"], [3, 5, 1, "", "MultipleObjectsReturned"], [3, 3, 1, "", "created_at"], [3, 3, 1, "", "data_types"], [3, 3, 1, "", "description"], [3, 6, 1, "", "get_next_by_created_at"], [3, 6, 1, "", "get_previous_by_created_at"], [3, 3, 1, "", "id"], [3, 3, 1, "", "objects"], [3, 3, 1, "", "organization"], [3, 3, 1, "", "organization_id"], [3, 3, 1, "", "project_name"], [3, 3, 1, "", "risks"]], "compliance_management.models.DataProcessingActivity": [[3, 5, 1, "", "DoesNotExist"], [3, 5, 1, "", "MultipleObjectsReturned"], [3, 3, 1, "", "activity_name"], [3, 3, 1, "", "data_categories"], [3, 3, 1, "", "data_subjects"], [3, 6, 1, "", "get_next_by_last_reviewed"], [3, 6, 1, "", "get_previous_by_last_reviewed"], [3, 3, 1, "", "id"], [3, 3, 1, "", "is_high_risk"], [3, 3, 1, "", "last_reviewed"], [3, 3, 1, "", "objects"], [3, 3, 1, "", "organization"], [3, 3, 1, "", "organization_id"], [3, 3, 1, "", "purpose"], [3, 3, 1, "", "retention_period"], [3, 3, 1, "", "security_measures"]], "compliance_management.models.DataProtectionRegulation": [[3, 5, 1, "", "DoesNotExist"], [3, 5, 1, "", "MultipleObjectsReturned"], [3, 3, 1, "", "compliancestatus_set"], [3, 3, 1, "", "description"], [3, 3, 1, "", "id"], [3, 3, 1, "", "jurisdiction"], [3, 3, 1, "", "kenyadpa_set"], [3, 3, 1, "", "name"], [3, 3, 1, "", "objects"]], "compliance_management.models.Incident": [[3, 5, 1, "", "DoesNotExist"], [3, 5, 1, "", "MultipleObjectsReturned"], [3, 3, 1, "", "date"], [3, 3, 1, "", "description"], [3, 6, 1, "", "get_next_by_date"], [3, 6, 1, "", "get_previous_by_date"], [3, 3, 1, "", "id"], [3, 3, 1, "", "objects"], [3, 3, 1, "", "reported_by"], [3, 3, 1, "", "reported_by_id"]], "compliance_management.models.KenyaDPA": [[3, 5, 1, "", "DoesNotExist"], [3, 5, 1, "", "MultipleObjectsReturned"], [3, 3, 1, "", "category"], [3, 3, 1, "", "data_protection_regulation_id"], [3, 3, 1, "", "data_protection_regulation_id_id"], [3, 3, 1, "", "description"], [3, 3, 1, "", "id"], [3, 3, 1, "", "key_points"], [3, 3, 1, "", "objects"], [3, 3, 1, "", "section_in_act"]], "compliance_management.views": [[3, 1, 1, "", "compliance_document_detail"], [3, 1, 1, "", "compliance_document_list"], [3, 1, 1, "", "compliance_report_detail"], [3, 1, 1, "", "compliance_report_list"], [3, 1, 1, "", "compliance_status_detail"], [3, 1, 1, "", "compliance_status_list"], [3, 1, 1, "", "create_compliance_document"], [3, 1, 1, "", "create_compliance_report"], [3, 1, 1, "", "create_compliance_status"], [3, 1, 1, "", "create_data_processing_activity"], [3, 1, 1, "", "create_data_protection_regulation"], [3, 1, 1, "", "create_dpi_a"], [3, 1, 1, "", "create_incident"], [3, 1, 1, "", "data_processing_activity_detail"], [3, 1, 1, "", "data_processing_activity_list"], [3, 1, 1, "", "data_protection_regulation_detail"], [3, 1, 1, "", "data_protection_regulation_list"], [3, 1, 1, "", "dpi_a_detail"], [3, 1, 1, "", "dpi_a_list"], [3, 1, 1, "", "incident_detail"], [3, 1, 1, "", "incident_list"]], "core": [[4, 0, 0, "-", "urls"]], "ingestion": [[6, 0, 0, "-", "models"]], "ingestion.models": [[6, 2, 1, "", "DataEntry"]], "ingestion.models.DataEntry": [[6, 5, 1, "", "DoesNotExist"], [6, 5, 1, "", "MultipleObjectsReturned"], [6, 3, 1, "", "STATUS_CHOICES"], [6, 3, 1, "", "created_at"], [6, 3, 1, "", "data"], [6, 6, 1, "", "get_next_by_created_at"], [6, 6, 1, "", "get_next_by_updated_at"], [6, 6, 1, "", "get_previous_by_created_at"], [6, 6, 1, "", "get_previous_by_updated_at"], [6, 6, 1, "", "get_status_display"], [6, 3, 1, "", "id"], [6, 3, 1, "", "metadata"], [6, 3, 1, "", "objects"], [6, 3, 1, "", "processed_data"], [6, 3, 1, "", "status"], [6, 3, 1, "", "updated_at"]], "policy_management": [[7, 0, 0, "-", "forms"], [7, 0, 0, "-", "models"], [7, 0, 0, "-", "views"]], "policy_management.forms": [[7, 2, 1, "", "ApprovalWorkflowForm"], [7, 2, 1, "", "PolicyForm"], [7, 2, 1, "", "PolicyVersionForm"]], "policy_management.forms.ApprovalWorkflowForm": [[7, 2, 1, "", "Meta"], [7, 3, 1, "", "base_fields"], [7, 3, 1, "", "declared_fields"], [7, 4, 1, "", "media"]], "policy_management.forms.ApprovalWorkflowForm.Meta": [[7, 3, 1, "", "fields"], [7, 3, 1, "", "model"]], "policy_management.forms.PolicyForm": [[7, 2, 1, "", "Meta"], [7, 3, 1, "", "base_fields"], [7, 3, 1, "", "declared_fields"], [7, 4, 1, "", "media"]], "policy_management.forms.PolicyForm.Meta": [[7, 3, 1, "", "fields"], [7, 3, 1, "", "model"]], "policy_management.forms.PolicyVersionForm": [[7, 2, 1, "", "Meta"], [7, 3, 1, "", "base_fields"], [7, 3, 1, "", "declared_fields"], [7, 4, 1, "", "media"]], "policy_management.forms.PolicyVersionForm.Meta": [[7, 3, 1, "", "fields"], [7, 3, 1, "", "model"]], "policy_management.models": [[7, 2, 1, "", "ApprovalWorkflow"], [7, 2, 1, "", "Policy"], [7, 2, 1, "", "PolicyVersion"]], "policy_management.models.ApprovalWorkflow": [[7, 5, 1, "", "DoesNotExist"], [7, 5, 1, "", "MultipleObjectsReturned"], [7, 3, 1, "", "approved_at"], [7, 3, 1, "", "approved_by"], [7, 3, 1, "", "approved_by_id"], [7, 6, 1, "", "get_next_by_approved_at"], [7, 6, 1, "", "get_previous_by_approved_at"], [7, 3, 1, "", "id"], [7, 3, 1, "", "objects"], [7, 3, 1, "", "policy"], [7, 3, 1, "", "policy_id"], [7, 3, 1, "", "status"]], "policy_management.models.Policy": [[7, 5, 1, "", "DoesNotExist"], [7, 5, 1, "", "MultipleObjectsReturned"], [7, 3, 1, "", "approvalworkflow_set"], [7, 3, 1, "", "created_at"], [7, 3, 1, "", "created_by"], [7, 3, 1, "", "created_by_id"], [7, 3, 1, "", "description"], [7, 6, 1, "", "get_next_by_created_at"], [7, 6, 1, "", "get_next_by_updated_at"], [7, 6, 1, "", "get_previous_by_created_at"], [7, 6, 1, "", "get_previous_by_updated_at"], [7, 3, 1, "", "id"], [7, 3, 1, "", "is_active"], [7, 3, 1, "", "objects"], [7, 3, 1, "", "slug"], [7, 3, 1, "", "title"], [7, 3, 1, "", "updated_at"], [7, 3, 1, "", "versions"]], "policy_management.models.PolicyVersion": [[7, 5, 1, "", "DoesNotExist"], [7, 5, 1, "", "MultipleObjectsReturned"], [7, 3, 1, "", "created_at"], [7, 3, 1, "", "created_by"], [7, 3, 1, "", "created_by_id"], [7, 3, 1, "", "document"], [7, 6, 1, "", "get_next_by_created_at"], [7, 6, 1, "", "get_previous_by_created_at"], [7, 3, 1, "", "id"], [7, 3, 1, "", "objects"], [7, 3, 1, "", "policy"], [7, 3, 1, "", "policy_id"], [7, 3, 1, "", "version_number"]], "policy_management.views": [[7, 1, 1, "", "approval_workflow_detail"], [7, 1, 1, "", "approval_workflow_list"], [7, 1, 1, "", "create_approval_workflow"], [7, 1, 1, "", "create_policy"], [7, 1, 1, "", "create_policy_version"], [7, 1, 1, "", "policy_detail"], [7, 1, 1, "", "policy_list"], [7, 1, 1, "", "policy_version_detail"], [7, 1, 1, "", "policy_version_list"]], "reporting": [[8, 0, 0, "-", "models"], [8, 0, 0, "-", "views"]], "reporting.models": [[8, 2, 1, "", "ComplianceAudit"], [8, 2, 1, "", "DataBreachReport"], [8, 2, 1, "", "ScheduledReport"]], "reporting.models.ComplianceAudit": [[8, 5, 1, "", "DoesNotExist"], [8, 5, 1, "", "MultipleObjectsReturned"], [8, 3, 1, "", "audit_date"], [8, 3, 1, "", "audit_findings"], [8, 3, 1, "", "auditor"], [8, 3, 1, "", "auditor_id"], [8, 6, 1, "", "get_next_by_audit_date"], [8, 6, 1, "", "get_previous_by_audit_date"], [8, 3, 1, "", "id"], [8, 3, 1, "", "is_resolved"], [8, 3, 1, "", "objects"], [8, 3, 1, "", "organization"], [8, 3, 1, "", "organization_id"], [8, 3, 1, "", "recommendations"], [8, 3, 1, "", "resolution_date"]], "reporting.models.DataBreachReport": [[8, 5, 1, "", "DoesNotExist"], [8, 5, 1, "", "MultipleObjectsReturned"], [8, 3, 1, "", "SEVERITY_CHOICES"], [8, 3, 1, "", "affected_data_subjects"], [8, 6, 1, "", "clean"], [8, 3, 1, "", "data_types_affected"], [8, 3, 1, "", "date_reported_to_authorities"], [8, 3, 1, "", "date_reported_to_data_subjects"], [8, 3, 1, "", "description"], [8, 3, 1, "", "discovery_date"], [8, 6, 1, "", "get_next_by_discovery_date"], [8, 6, 1, "", "get_next_by_incident_date"], [8, 6, 1, "", "get_next_by_report_generated_date"], [8, 6, 1, "", "get_previous_by_discovery_date"], [8, 6, 1, "", "get_previous_by_incident_date"], [8, 6, 1, "", "get_previous_by_report_generated_date"], [8, 6, 1, "", "get_severity_display"], [8, 3, 1, "", "id"], [8, 3, 1, "", "incident_date"], [8, 3, 1, "", "is_within_72_hours"], [8, 3, 1, "", "objects"], [8, 3, 1, "", "organization"], [8, 3, 1, "", "organization_id"], [8, 3, 1, "", "potential_impact"], [8, 3, 1, "", "remediation_steps"], [8, 3, 1, "", "report_generated_date"], [8, 3, 1, "", "reported_to_authorities"], [8, 3, 1, "", "reported_to_data_subjects"], [8, 6, 1, "", "save"], [8, 3, 1, "", "severity"]], "reporting.models.ScheduledReport": [[8, 5, 1, "", "DoesNotExist"], [8, 5, 1, "", "MultipleObjectsReturned"], [8, 3, 1, "", "email_recipients"], [8, 6, 1, "", "get_next_by_schedule_time"], [8, 6, 1, "", "get_previous_by_schedule_time"], [8, 3, 1, "", "id"], [8, 3, 1, "", "interval"], [8, 3, 1, "", "objects"], [8, 3, 1, "", "organization"], [8, 3, 1, "", "organization_id"], [8, 3, 1, "", "report_type"], [8, 3, 1, "", "schedule_time"]], "reporting.views": [[8, 1, 1, "", "compliance_audit_detail"], [8, 1, 1, "", "compliance_audit_list"], [8, 1, 1, "", "create_compliance_audit"], [8, 1, 1, "", "create_data_breach_report"], [8, 1, 1, "", "create_scheduled_report"], [8, 1, 1, "", "data_breach_report_detail"], [8, 1, 1, "", "data_breach_report_list"], [8, 1, 1, "", "scheduled_report_detail"], [8, 1, 1, "", "scheduled_report_list"]]}, "objnames": {"0": ["py", "module", "Python module"], "1": ["py", "function", "Python function"], "2": ["py", "class", "Python class"], "3": ["py", "attribute", "Python attribute"], "4": ["py", "property", "Python property"], "5": ["py", "exception", "Python exception"], "6": ["py", "method", "Python method"]}, "objtypes": {"0": "py:module", "1": "py:function", "2": "py:class", "3": "py:attribute", "4": "py:property", "5": "py:exception", "6": "py:method"}, "terms": {"": [1, 2, 5, 7], "1": [3, 7], "A": [1, 2, 3, 6, 7, 8], "In": [1, 2, 3, 7, 8], "The": [1, 3, 7], "To": 5, "about": 5, "abov": 5, "abstractbaseus": 2, "access": [3, 7], "accessor": [1, 2, 3, 7, 8], "action": 1, "action_choic": 1, "action_descript": 1, "activ": 3, "activity_nam": 3, "add": 2, "additional_data": 1, "address": [1, 2], "affect": 1, "affected_data_subject": 8, "affected_resourc": 1, "after": 2, "alia": [1, 2, 6, 7], "all": [1, 2, 7], "an": [1, 2, 3, 7, 8], "analysi": 0, "analyt": 5, "api": 6, "apiview": 6, "applic": [1, 4, 6, 8], "approv": 7, "approval_workflow_detail": [5, 7], "approval_workflow_list": [5, 7], "approvalworkflow": [5, 7], "approvalworkflow_set": [2, 5, 7], "approvalworkflowform": [5, 7], "approved_at": [5, 7], "approved_at_displai": 7, "approved_bi": [5, 7], "approved_by_id": [5, 7], "ar": 2, "arg": [1, 2, 3, 6, 7, 8], "assess": 3, "assign": [3, 7], "attribut": [3, 7], "audit": [5, 8], "audit_d": 8, "audit_find": 8, "audit_log": 1, "audit_log_detail": [1, 5], "audit_log_list": [1, 5], "auditlog": [1, 5], "auditlog_set": 2, "auditlogform": [1, 5], "auditor": 8, "auditor_id": 8, "authent": 5, "auto_id": [1, 2, 7], "backend": 5, "base": [1, 2, 3, 6, 7, 8], "base_field": [1, 2, 5, 7], "baseusermanag": 2, "befor": 8, "below": [2, 3, 7], "bool": 1, "booleanfield": [1, 7], "breach": 8, "built": [2, 3, 7], "call": 2, "can": [2, 3, 7], "categori": 3, "charfield": [1, 2, 3, 6, 7, 8], "check": 1, "child": [1, 2, 3, 7, 8], "children": [1, 2, 3, 7, 8], "class": [1, 2, 3, 6, 7, 8], "classmethod": 1, "clean": 8, "code": [3, 7], "commit": 2, "company_s": 2, "complianc": [1, 5, 8], "compliance_audit_detail": [5, 8], "compliance_audit_list": [5, 8], "compliance_check": 1, "compliance_document_detail": [3, 5], "compliance_document_list": [3, 5], "compliance_manag": 3, "compliance_not": 1, "compliance_report_detail": [3, 5], "compliance_report_list": [3, 5], "compliance_statu": 3, "compliance_status_choic": 3, "compliance_status_detail": [3, 5], "compliance_status_list": [3, 5], "complianceaudit": [5, 8], "complianceaudit_set": 2, "compliancedocu": [3, 5], "compliancedocument_set": 2, "compliancereport": [3, 5], "compliancereport_set": 2, "compliancestatu": [3, 5], "compliancestatus_set": [2, 3], "compliant": [1, 3], "compon": 5, "comprehens": 5, "conduct": [3, 8], "contact_email": 2, "contact_numb": 2, "contact_person": 2, "content": [], "core": 5, "creat": [1, 2, 6], "create_approval_workflow": [5, 7], "create_compliance_audit": [5, 8], "create_compliance_docu": [3, 5], "create_compliance_report": [3, 5], "create_compliance_statu": [3, 5], "create_data_breach_report": [5, 8], "create_data_processing_act": [3, 5], "create_data_protection_regul": [3, 5], "create_dpi_a": [3, 5], "create_forward_many_to_many_manag": [2, 3, 7], "create_incid": [3, 5], "create_polici": [5, 7], "create_policy_vers": [5, 7], "create_scheduled_report": [5, 8], "create_superus": 2, "create_us": 2, "createapiview": 6, "created_at": [1, 2, 3, 5, 6, 7], "created_bi": [5, 7], "created_by_id": [5, 7], "creation": 7, "critic": 8, "custom": 2, "data": [0, 1, 2, 3, 6, 7, 8], "data_breach_report_detail": [5, 8], "data_breach_report_list": [5, 8], "data_categori": 3, "data_id": 6, "data_processing_activity_detail": [3, 5], "data_processing_activity_list": [3, 5], "data_protection_regul": 3, "data_protection_regulation_detail": [3, 5], "data_protection_regulation_id": 3, "data_protection_regulation_id_id": 3, "data_protection_regulation_list": [3, 5], "data_protection_regulations_id": 3, "data_subject": 3, "data_typ": 3, "data_types_affect": 8, "databreachreport": [5, 8], "databreachreport_set": 2, "dataentri": [5, 6], "dataentryseri": 6, "dataprocessingact": [3, 5], "dataprocessingactivity_set": 2, "dataprocessview": [5, 6], "dataprotectionregul": [3, 5], "dataresultview": [5, 6], "datastatusview": [5, 6], "datauploadview": [5, 6], "date": 3, "date_reported_to_author": 8, "date_reported_to_data_subject": 8, "datefield": 3, "datetimefield": [1, 2, 3, 6, 7, 8], "db": [1, 2, 3, 6, 7, 8], "declared_field": [1, 2, 5, 7], "default": 1, "defer": [1, 2, 3, 6, 7, 8], "defin": [2, 3, 7], "deleg": [2, 3, 7], "delet": 1, "descript": [1, 3, 5, 7, 8], "descriptor": [3, 7], "detail": 4, "discovery_d": 8, "django": [1, 2, 3, 6, 7, 8], "do": [3, 7], "document": 7, "document_typ": 3, "doesnotexist": [1, 2, 3, 5, 6, 7, 8], "dpi_a_detail": [3, 5], "dpi_a_list": [3, 5], "dpia": [3, 5], "dpia_set": 2, "dynam": [2, 3, 7], "effect": 5, "email": 2, "email_recipi": 8, "emailfield": 2, "empti": 1, "empty_permit": [1, 2, 7], "entri": 1, "error_class": [1, 2, 7], "errorlist": [1, 2, 7], "event": 1, "exampl": [1, 2, 3, 7, 8], "except": [1, 2, 3, 6, 7, 8], "execut": [1, 2, 3, 6, 7, 8], "expiry_d": 3, "export": 1, "f": [3, 7], "fail": 6, "fals": [1, 2, 3, 6, 7, 8], "featur": 0, "field": [1, 2, 3, 6, 7, 8], "fieldfil": [3, 7], "file": [1, 2, 3, 7], "filefield": 7, "filter": 3, "first": [1, 2, 3, 6, 7, 8], "first_nam": 2, "foreignkei": [1, 2, 3, 7, 8], "form": [1, 2, 7], "format": 6, "forward": [1, 2, 3, 7, 8], "forwardmanytoonedescriptor": [1, 2, 3, 7, 8], "forwardonetoonedescriptor": [1, 2, 3, 7, 8], "from": [1, 2, 3, 6, 7, 8], "full": 2, "function": [3, 8], "gener": [2, 3], "generated_at": 3, "genericipaddressfield": 1, "get": [3, 6, 7], "get_action_displai": 1, "get_compliance_status_displai": 3, "get_full_nam": 2, "get_next_by_approved_at": [5, 7], "get_next_by_audit_d": 8, "get_next_by_created_at": [1, 2, 3, 5, 6, 7], "get_next_by_d": 3, "get_next_by_discovery_d": 8, "get_next_by_generated_at": 3, "get_next_by_incident_d": 8, "get_next_by_last_checked_at": 3, "get_next_by_last_review": 3, "get_next_by_report_generated_d": 8, "get_next_by_schedule_tim": 8, "get_next_by_updated_at": [2, 5, 6, 7], "get_next_by_upload_d": 3, "get_previous_by_approved_at": [5, 7], "get_previous_by_audit_d": 8, "get_previous_by_created_at": [1, 2, 3, 5, 6, 7], "get_previous_by_d": 3, "get_previous_by_discovery_d": 8, "get_previous_by_generated_at": 3, "get_previous_by_incident_d": 8, "get_previous_by_last_checked_at": 3, "get_previous_by_last_review": 3, "get_previous_by_report_generated_d": 8, "get_previous_by_schedule_tim": 8, "get_previous_by_updated_at": [2, 5, 6, 7], "get_previous_by_upload_d": 3, "get_severity_displai": 8, "get_short_nam": 2, "get_status_displai": 6, "group": 2, "guid": 5, "handl": [0, 1, 4, 6, 7], "hello": [3, 7], "high": 8, "homepag": [5, 6], "how": 5, "i": [1, 2, 3, 6, 7, 8], "id": [1, 2, 3, 5, 6, 7, 8], "id_": [1, 2, 7], "impact": 3, "implement": [2, 3, 7], "import": [1, 3, 7], "incid": [3, 5, 8], "incident_d": 8, "incident_detail": [3, 5], "incident_list": [3, 5], "incident_set": 2, "index": 5, "indic": 1, "individu": 5, "industri": 2, "inform": 5, "ingest": 5, "initi": [1, 2, 7], "instanc": [1, 2, 3, 7, 8], "integerfield": 7, "interv": 8, "ip": 1, "ip_address": 1, "is_act": [2, 5, 7], "is_compli": 1, "is_high_risk": 3, "is_next": [1, 2, 3, 6, 7, 8], "is_resolv": 8, "is_staff": 2, "is_superus": 2, "is_within_72_hour": 8, "its": 5, "jsonfield": 1, "jurisdict": 3, "kenya": 3, "kenyadpa": [3, 5], "kenyadpa_set": 3, "key_point": 3, "kwarg": [1, 2, 3, 6, 7, 8], "label_suffix": [1, 2, 7], "last": 2, "last_checked_at": 3, "last_login": 2, "last_nam": 2, "last_review": 3, "later": 2, "like": [3, 7], "list": [1, 5], "load": [1, 2, 3, 6, 7, 8], "log": 5, "log_act": 1, "log_action_view": [1, 5], "login": 1, "logout": 1, "low": 8, "manag": [1, 2, 5, 6, 7, 8], "mani": [1, 2, 3, 7, 8], "manual": 2, "manytomanydescriptor": 2, "manytomanyfield": 2, "mechan": 2, "media": [1, 2, 5, 7], "medium": 8, "meta": [1, 2, 5, 7], "metadata": 6, "method": [2, 8], "metrics_view": [0, 5], "model": [1, 2, 3, 6, 7, 8], "modelchoicefield": [1, 2, 7], "modelform": [1, 2, 7], "modul": [0, 1, 2, 3, 4, 5, 6, 7, 8], "most": [2, 3, 7], "multipleobjectsreturn": [1, 2, 3, 5, 6, 7, 8], "myapp": [3, 7], "mymodel": [3, 7], "name": [2, 3], "new": 1, "non": 3, "none": [1, 2, 6, 7], "note": 1, "object": [1, 2, 3, 5, 6, 7, 8], "objectdoesnotexist": [1, 2, 3, 6, 7, 8], "one": [1, 2, 3, 7, 8], "open": [3, 7], "option": 1, "organ": [1, 2, 3, 5, 8], "organization_detail": [2, 5], "organization_id": [1, 2, 3, 8], "organization_list": [2, 5], "organization_regist": [2, 5], "organizationregistrationform": [2, 5], "otherwis": 2, "our": 5, "overrid": [2, 8], "page": 5, "paramet": 1, "parent": [1, 2, 3, 7, 8], "password": 2, "passwordinput": 2, "path": [3, 7], "perform": [1, 8], "permissionsmixin": 2, "pizza": 2, "pk": [3, 7], "pleas": 5, "polici": [5, 7], "policy_detail": [5, 7], "policy_id": [5, 7], "policy_list": [5, 7], "policy_manag": 7, "policy_set": 2, "policy_version_detail": [5, 7], "policy_version_list": [5, 7], "policyform": [5, 7], "policyvers": [5, 7], "policyversion_set": 2, "policyversionform": [5, 7], "post": 6, "potential_impact": 8, "prefix": [1, 2, 7], "process": [3, 6], "processed_data": 6, "project_nam": 3, "properti": [1, 2, 7], "protect": 3, "provid": [2, 5, 8], "purpos": 3, "queri": [1, 2, 3, 6, 7, 8], "read": [1, 2, 3, 6, 7, 8], "recommend": 8, "refer": 5, "regard": 1, "regul": 3, "relat": [1, 2, 3, 7, 8], "related_nam": [1, 2, 3, 7, 8], "remediation_step": 8, "render": [1, 2, 7], "report": [3, 5], "report_generated_d": 8, "report_typ": [3, 8], "reported_bi": 3, "reported_by_id": 3, "reported_to_author": 8, "reported_to_data_subject": 8, "repres": [1, 2, 3, 7, 8], "request": [0, 1, 2, 3, 6, 7, 8], "requir": [1, 2, 7], "required_field": 2, "resolution_d": 8, "resourc": 1, "restructuredtext": [], "retention_period": 3, "retriev": 1, "return": [1, 2, 3, 7], "revers": [2, 3, 7], "reversemanytoonedescriptor": [2, 3, 7], "risk": 3, "root": 4, "save": [2, 8], "save_m2m": 2, "schedul": 8, "schedule_tim": 8, "scheduled_report_detail": [5, 8], "scheduled_report_list": [5, 8], "scheduledreport": [5, 8], "scheduledreport_set": 2, "search": 5, "section": 5, "section_in_act": 3, "security_measur": 3, "see": [], "self": 2, "serializer_class": 6, "set": 8, "sever": 8, "severity_choic": 8, "short": 2, "side": [1, 2, 3, 7, 8], "size": [3, 7], "slug": [1, 2, 3, 5, 7], "so": [3, 7], "sourc": [0, 1, 2, 3, 6, 7, 8], "specif": [1, 3], "statu": [3, 5, 6, 7], "status_choic": 6, "str": 1, "string": 1, "subclass": [1, 2, 3, 7, 8], "superus": 2, "syntax": [], "system": [1, 5], "them": 5, "thi": [0, 1, 2, 3, 4, 5, 6, 7, 8], "time": [1, 2, 3, 6, 7, 8], "titl": [3, 5, 7], "top": 2, "true": [1, 2, 3, 6, 7, 8], "type": 1, "typedchoicefield": 1, "updat": 1, "updated_at": [2, 5, 6, 7], "upload": [3, 6], "upload_d": 3, "uploaded_bi": 3, "uploaded_by_id": 3, "us": 5, "use_required_attribut": [1, 2, 7], "user": [1, 2, 5], "user_detail": [2, 5], "user_id": 1, "user_list": [2, 5], "user_login": [2, 5], "user_permiss": 2, "user_regist": [2, 5], "usermanag": [2, 5], "username_field": 2, "userregistrationform": [2, 5], "util": [1, 2, 7], "valid": 8, "valu": [1, 2, 3, 6, 7, 8], "version": [5, 7], "version_numb": [5, 7], "via": [1, 2, 3, 7, 8], "view": [0, 1, 2, 3, 6, 7, 8], "wa": 1, "welcom": 5, "when": [1, 2, 3, 6, 7, 8], "which": [1, 2], "who": 1, "widget": [1, 2, 7], "within": [1, 4, 6], "workflow": 7, "world": [3, 7], "wrapper": [1, 2, 3, 6, 7, 8], "write": [3, 7], "you": [3, 7], "your": []}, "titles": ["Analytics Documentation", "Audit Log Documentation", "Authentication Documentation", "Compliance Management Documentation", "Core\u2019s Documentation", "Datashield Solutions Documentation", "Ingestion Documentation", "&lt;no title&gt;", "Reporting Documentation"], "titleterms": {"": 4, "analyt": 0, "audit": 1, "authent": 2, "complianc": 3, "content": 5, "core": 4, "datashield": 5, "document": [0, 1, 2, 3, 4, 5, 6, 8], "get": 5, "indic": 5, "ingest": 6, "log": 1, "manag": 3, "report": 8, "solut": 5, "start": 5, "tabl": 5}})