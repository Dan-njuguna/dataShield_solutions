import os
from django.db import models
from authentication.models import User

from dotenv import load_dotenv
import os
load_dotenv()

DBUSER = os.getenv("DBUSER")
DBNAME = os.getenv("DBNAME")
DBPASS = os.getenv("DBPASS")
DBHOST = os.getenv("DBHOST")
DBPORT = os.getenv("DBPORT")


class Policy(models.Model):
    __doc__ = "Model representing a policy document."
    title = models.CharField(max_length=255, help_text="The title of the policy.")
    slug = models.SlugField(unique=True, max_length=255, help_text="URL-friendly version of the title.")
    description = models.TextField(help_text="Description of the policy.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the policy was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the policy was last updated.")
    created_by = models.ForeignKey(User, on_delete=(models.CASCADE), help_text="User  who created the policy.")
    is_active = models.BooleanField(default=False, help_text="Indicates if the policy is active.")

    def __str__(self):
        return self.title


class PolicyVersion(models.Model):
    __doc__ = "Model representing a version of a policy document."
    policy = models.ForeignKey(Policy, related_name="versions", on_delete=(models.CASCADE))
    version_number = models.IntegerField(help_text="Version number of the policy.")
    document = models.FileField(upload_to="policy_versions/", help_text="Uploaded policy document.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the version was created.")
    created_by = models.ForeignKey(User, on_delete=(models.CASCADE), help_text="User  who created the version.")

    def __str__(self):
        return f"{self.policy.title} - Version {self.version_number}"


class ApprovalWorkflow(models.Model):
    __doc__ = "Model representing an approval workflow for policies."
    policy = models.ForeignKey(Policy, on_delete=(models.CASCADE))
    approved_by = models.ForeignKey(User, on_delete=(models.CASCADE))
    approved_at = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.policy.title} approved by {self.approved_by.email}"
