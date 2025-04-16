import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)
fake = Faker()
Faker.seed(42)

# Set parameters
num_contacts = 500
num_companies = 100
duplicate_rate = 0.15  # 15% of contacts will be duplicates
missing_data_rate = 0.2  # 20% chance of missing email or phone

# Generate today's date and a date 2 years ago
today = datetime.now()
two_years_ago = today - timedelta(days=730)

# Generate company data
company_ids = list(range(1, num_companies + 1))
companies = []

for company_id in company_ids:
    company_name = fake.company()
    industry = random.choice(['Technology', 'Healthcare', 'Finance', 'Retail', 'Manufacturing', 'Education', 'Consulting'])
    size = random.choice(['Small', 'Medium', 'Large', 'Enterprise'])
    
    # Determine if company is active (80% chance)
    is_active = random.random() < 0.8
    
    # Generate last activity date
    if is_active:
        # Active companies have activity in the last 90 days
        days_since_activity = random.randint(0, 90)
    else:
        # Inactive companies have activity between 91 and 730 days ago
        days_since_activity = random.randint(91, 730)
    
    last_activity_date = today - timedelta(days=days_since_activity)
    
    # Generate creation date (between 2 years ago and 3 months ago)
    created_date = two_years_ago + timedelta(days=random.randint(0, 640))
    
    companies.append({
        'company_id': company_id,
        'company_name': company_name,
        'industry': industry,
        'size': size,
        'is_active': is_active,
        'last_activity_date': last_activity_date,
        'created_date': created_date,
        'annual_revenue': random.randint(100000, 10000000)
    })

companies_df = pd.DataFrame(companies)

# Generate contact data
contacts = []
contact_id = 1

# Regular contacts (non-duplicates)
for i in range(int(num_contacts * (1 - duplicate_rate))):
    company_id = random.choice(company_ids)
    first_name = fake.first_name()
    last_name = fake.last_name()
    job_title = fake.job()
    
    # Apply missing data logic
    has_missing_email = random.random() < missing_data_rate
    has_missing_phone = random.random() < missing_data_rate
    
    email = '' if has_missing_email else f"{first_name.lower()}.{last_name.lower()}@{fake.domain_name()}"
    phone = '' if has_missing_phone else fake.phone_number()
    
    # Get company info
    company_info = next(c for c in companies if c['company_id'] == company_id)
    
    # Contact creation date should be after company creation date
    days_since_company_created = (today - company_info['created_date']).days
    contact_created_days_ago = random.randint(0, days_since_company_created)
    created_date = today - timedelta(days=contact_created_days_ago)
    
    # Last activity should be after creation but not after company's last activity
    company_last_activity_days_ago = (today - company_info['last_activity_date']).days
    max_activity_days = min(contact_created_days_ago, company_last_activity_days_ago)
    activity_days_ago = random.randint(0, max_activity_days) if max_activity_days > 0 else 0
    last_activity_date = today - timedelta(days=activity_days_ago)
    
    # Determine if contact is active
    is_active = activity_days_ago <= 90
    
    contacts.append({
        'contact_id': contact_id,
        'company_id': company_id,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'job_title': job_title,
        'created_date': created_date,
        'last_activity_date': last_activity_date,
        'is_active': is_active
    })
    
    contact_id += 1

# Generate duplicate contacts
original_contacts = contacts.copy()
for i in range(int(num_contacts * duplicate_rate)):
    # Pick a random contact to duplicate
    original = random.choice(original_contacts)
    
    # Create a duplicate with slight changes
    duplicate = original.copy()
    duplicate['contact_id'] = contact_id
    
    # Apply one or more of these changes
    change_type = random.randint(1, 5)
    
    if change_type == 1:
        # Typo in name
        duplicate['first_name'] = duplicate['first_name'] + random.choice(['', 'n', 'e'])
    elif change_type == 2:
        # Different email format
        if duplicate['email']:
            name_part = duplicate['email'].split('@')[0]
            domain = duplicate['email'].split('@')[1]
            duplicate['email'] = f"{name_part.replace('.', '_')}@{domain}"
    elif change_type == 3:
        # Different phone format
        if duplicate['phone']:
            duplicate['phone'] = duplicate['phone'].replace('-', '.')
    elif change_type == 4:
        # Slight name variation
        duplicate['last_name'] = duplicate['last_name'] + random.choice(['', 'n', 's'])
    elif change_type == 5:
        # Different job title
        duplicate['job_title'] = fake.job()
    
    contacts.append(duplicate)
    contact_id += 1

contacts_df = pd.DataFrame(contacts)

# Generate interactions data
interactions = []
interaction_id = 1

for contact in contacts:
    # Number of interactions per contact (0 to 10)
    num_interactions = random.randint(0, 10)
    
    for _ in range(num_interactions):
        # Interaction date should be between contact creation and their last activity
        contact_created = contact['created_date']
        contact_last_activity = contact['last_activity_date']
        
        if contact_created == contact_last_activity:
            interaction_date = contact_created
        else:
            days_range = (contact_last_activity - contact_created).days
            if days_range > 0:
                random_days = random.randint(0, days_range)
                interaction_date = contact_created + timedelta(days=random_days)
            else:
                interaction_date = contact_created
        
        interaction_type = random.choice(['Email', 'Call', 'Meeting', 'Demo', 'Support'])
        outcome = random.choice(['Positive', 'Neutral', 'Negative', 'No Response'])
        
        interactions.append({
            'interaction_id': interaction_id,
            'contact_id': contact['contact_id'],
            'company_id': contact['company_id'],
            'interaction_date': interaction_date,
            'interaction_type': interaction_type,
            'outcome': outcome,
            'notes': fake.sentence()
        })
        
        interaction_id += 1

interactions_df = pd.DataFrame(interactions)

# Save to CSV files
companies_df.to_csv('crm_companies.csv', index=False)
contacts_df.to_csv('crm_contacts.csv', index=False)
interactions_df.to_csv('crm_interactions.csv', index=False)

print(f"Generated {len(companies_df)} companies")
print(f"Generated {len(contacts_df)} contacts")
print(f"Generated {len(interactions_df)} interactions")

# Preview the data
print("\nCompanies Preview:")
print(companies_df.head())

print("\nContacts Preview:")
print(contacts_df.head())

print("\nInteractions Preview:")
print(interactions_df.head())