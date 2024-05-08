from django.db import models

# Create your models here.

class Portfolio(models.Model):
    # Personal Information
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    mailing_address = models.CharField(max_length=40)
    professional_title = models.CharField(max_length=255)

    # Professional Summary
    professional_summary = models.TextField()

    # Skills - Stored as a comma-separated string
    skills = models.TextField(help_text="Enter skills separated by commas")

    # Work Experience - Simplified for brevity; Consider a separate model for multiple entries
    job_titles = models.TextField(help_text="Enter job titles separated by commas")
    companies_worked_at = models.TextField(help_text="Enter companies separated by commas")
    employment_dates = models.CharField(max_length=255)
    job_descriptions = models.TextField()

    # Educational Background - Also consider a separate model for multiple entries
    institutions_attended = models.TextField(help_text="Enter institutions separated by commas")
    degrees_certifications = models.TextField(help_text="Enter degrees or certifications separated by commas")
    years_of_attendance = models.CharField(max_length=255)

    # Projects and Portfolio Pieces
    project_titles = models.TextField(help_text="Enter project titles separated by commas")
    project_descriptions = models.TextField()
    project_links = models.TextField(help_text="Enter project URLs separated by commas")
    project_images = models.ImageField(upload_to='images/', blank=True, null=True)

    # Achievements and Awards
    achievements = models.TextField(blank=True)

    # Professional References
    references_names = models.TextField()
    references_contact_info = models.TextField()

    # Professional Social Profiles
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    other_social_urls = models.TextField(blank=True)

    # Personalized Sections
    volunteer_work = models.TextField(blank=True)
    languages_spoken = models.TextField(blank=True)
    hobbies_interests = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.full_name} ({self.email})"