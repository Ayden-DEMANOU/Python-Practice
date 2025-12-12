"""
Email Template Filler (Automation Tool)
Teaches: String Formatting, File I/O, String Replacement, Automation
"""

import os
from datetime import datetime


# ========== TEMPLATE CREATION ==========
def create_sample_templates():
    """Create sample email templates if they don't exist"""
    
    # Template 1: Job Application
    job_template = """Subject: Application for {position} Position

Dear {recipient_name},

I am writing to express my interest in the {position} position at {company_name}. 
With {years_experience} years of experience in {field}, I believe I would be an 
excellent fit for your team.

I am particularly excited about {company_name} because {reason}.

My skills include:
- {skill_1}
- {skill_2}
- {skill_3}

I would welcome the opportunity to discuss how my experience aligns with your needs.
Thank you for your consideration.

Best regards,
{sender_name}
{email}
{phone}
"""
    
    # Template 2: Meeting Invitation
    meeting_template = """Subject: Meeting Invitation - {meeting_topic}

Dear {recipient_name},

I hope this email finds you well. I would like to schedule a meeting to discuss {meeting_topic}.

Meeting Details:
- Date: {date}
- Time: {time}
- Duration: {duration}
- Location: {location}
- Agenda: {agenda}

Please confirm your availability at your earliest convenience.

Looking forward to our discussion.

Best regards,
{sender_name}
{email}
"""
    
    # Template 3: Follow-up Email
    followup_template = """Subject: Following Up - {subject}

Hi {recipient_name},

I wanted to follow up on {subject} that we discussed on {previous_date}.

{main_message}

Next Steps:
1. {step_1}
2. {step_2}
3. {step_3}

Please let me know if you have any questions or need additional information.

Best regards,
{sender_name}
"""
    
    # Template 4: Thank You Email
    thankyou_template = """Subject: Thank You - {occasion}

Dear {recipient_name},

Thank you so much for {reason}. Your {quality} truly made a difference.

{personal_message}

I look forward to {future_action}.

Warm regards,
{sender_name}
"""
    
    # Create templates directory if it doesn't exist
    if not os.path.exists("templates"):
        os.makedirs("templates")
        print("✓ Created 'templates' folder")
    
    # Save templates to files
    templates = {
        "templates/job_application.txt": job_template,
        "templates/meeting_invitation.txt": meeting_template,
        "templates/followup_email.txt": followup_template,
        "templates/thankyou_email.txt": thankyou_template
    }
    
    for filename, content in templates.items():
        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                file.write(content)
            print(f"✓ Created template: {filename}")


# ========== FILE OPERATIONS ==========
def read_template(filename):
    """Read template file and return its content"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"❌ Error: Template file '{filename}' not found!")
        return None
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None


def save_filled_email(content, recipient_name):
    """Save filled email to output folder"""
    # Create output directory if it doesn't exist
    if not os.path.exists("output"):
        os.makedirs("output")
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output/email_{recipient_name}_{timestamp}.txt"
    
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"✓ Email saved to: {filename}")
        return filename
    except Exception as e:
        print(f"❌ Error saving file: {e}")
        return None


# ========== PLACEHOLDER DETECTION ==========
def find_placeholders(template):
    """Find all placeholders in template (words between {})"""
    placeholders = []
    
    # Simple method: look for {word}
    import re
    matches = re.findall(r'\{(\w+)\}', template)
    
    # Remove duplicates and return
    return list(set(matches))


def display_placeholders(placeholders):
    """Display all required placeholders"""
    print("\n" + "="*50)
    print("REQUIRED INFORMATION:")
    print("="*50)
    for i, placeholder in enumerate(sorted(placeholders), start=1):
        # Make placeholder names more readable
        readable_name = placeholder.replace('_', ' ').title()
        print(f"{i}. {readable_name}")
    print("="*50)


# ========== PLACEHOLDER FILLING ==========
def get_placeholder_values(placeholders):
    """Get values for all placeholders from user"""
    values = {}
    
    print("\nPlease provide the following information:")
    print("(Press Enter to skip optional fields)")
    print("-"*50)
    
    for placeholder in sorted(placeholders):
        # Make placeholder name readable
        readable_name = placeholder.replace('_', ' ').title()
        
        # Get value from user
        value = input(f"{readable_name}: ").strip()
        
        # If empty, use placeholder as default
        if not value:
            value = f"[{placeholder}]"
        
        values[placeholder] = value
    
    return values


def fill_template(template, values):
    """Replace placeholders with actual values"""
    filled_template = template
    
    # Replace each placeholder
    for placeholder, value in values.items():
        # Replace {placeholder} with value
        filled_template = filled_template.replace(f"{{{placeholder}}}", value)
    
    return filled_template


# ========== MANUAL TEMPLATE CREATION ==========
def create_custom_template():
    """Allow user to create their own template"""
    print("\n" + "="*50)
    print("CREATE CUSTOM TEMPLATE")
    print("="*50)
    print("\nTips:")
    print("- Use {placeholder_name} for values to fill later")
    print("- Example: Dear {name}, Welcome to {company}!")
    print("- Type 'DONE' on a new line when finished")
    print("-"*50)
    
    lines = []
    print("\nEnter your template (line by line):")
    
    while True:
        line = input()
        if line.strip().upper() == 'DONE':
            break
        lines.append(line)
    
    template_content = '\n'.join(lines)
    
    # Save template
    template_name = input("\nEnter template name (without .txt): ").strip()
    if not template_name:
        template_name = "custom_template"
    
    filename = f"templates/{template_name}.txt"
    
    try:
        with open(filename, 'w') as file:
            file.write(template_content)
        print(f"✓ Template saved to: {filename}")
        return filename
    except Exception as e:
        print(f"❌ Error saving template: {e}")
        return None


# ========== BATCH PROCESSING ==========
def batch_fill_templates():
    """Fill template for multiple recipients"""
    print("\n" + "="*50)
    print("BATCH EMAIL GENERATION")
    print("="*50)
    
    # Select template
    template_file = select_template()
    if not template_file:
        return
    
    # Read template
    template = read_template(template_file)
    if not template:
        return
    
    # Find placeholders
    placeholders = find_placeholders(template)
    
    # Get number of emails
    try:
        num_emails = int(input("\nHow many emails do you want to generate? "))
    except ValueError:
        print("❌ Invalid number!")
        return
    
    print(f"\n📧 Generating {num_emails} emails...")
    
    # Generate each email
    for i in range(num_emails):
        print(f"\n--- Email #{i+1}/{num_emails} ---")
        
        # Get values for this email
        values = get_placeholder_values(placeholders)
        
        # Fill template
        filled_email = fill_template(template, values)
        
        # Save to file
        recipient_name = values.get('recipient_name', f'recipient_{i+1}')
        save_filled_email(filled_email, recipient_name)
    
    print(f"\n✓ Successfully generated {num_emails} emails!")


# ========== TEMPLATE SELECTION ==========
def select_template():
    """Let user select from available templates"""
    print("\n" + "="*50)
    print("AVAILABLE TEMPLATES:")
    print("="*50)
    
    # Get list of templates
    if not os.path.exists("templates"):
        print("❌ No templates folder found!")
        return None
    
    templates = [f for f in os.listdir("templates") if f.endswith('.txt')]
    
    if not templates:
        print("❌ No templates found!")
        return None
    
    # Display templates
    for i, template in enumerate(templates, start=1):
        print(f"{i}. {template}")
    
    # Get user choice
    try:
        choice = int(input("\nSelect template number: "))
        if 1 <= choice <= len(templates):
            return f"templates/{templates[choice-1]}"
        else:
            print("❌ Invalid choice!")
            return None
    except ValueError:
        print("❌ Please enter a number!")
        return None


# ========== PREVIEW FUNCTIONALITY ==========
def preview_template(template, values):
    """Show preview of filled template"""
    print("\n" + "="*50)
    print("EMAIL PREVIEW:")
    print("="*50)
    filled = fill_template(template, values)
    print(filled)
    print("="*50)


# ========== MAIN MENU ==========
def display_main_menu():
    """Display main menu"""
    print("\n" + "="*50)
    print("     📧 EMAIL TEMPLATE FILLER 📧")
    print("="*50)
    print("1. Fill Single Email Template")
    print("2. Batch Fill Multiple Emails")
    print("3. Create Custom Template")
    print("4. View Available Templates")
    print("5. Create Sample Templates")
    print("6. Exit")
    print("="*50)


def view_templates():
    """Display all available templates and their placeholders"""
    print("\n" + "="*50)
    print("TEMPLATE LIBRARY:")
    print("="*50)
    
    if not os.path.exists("templates"):
        print("❌ No templates folder found!")
        return
    
    templates = [f for f in os.listdir("templates") if f.endswith('.txt')]
    
    if not templates:
        print("❌ No templates found!")
        return
    
    for template_file in templates:
        print(f"\n📄 {template_file}")
        print("-"*50)
        
        template = read_template(f"templates/{template_file}")
        if template:
            placeholders = find_placeholders(template)
            print(f"Placeholders: {', '.join(sorted(placeholders))}")


def fill_single_email():
    """Main function to fill a single email"""
    # Select template
    template_file = select_template()
    if not template_file:
        return
    
    # Read template
    template = read_template(template_file)
    if not template:
        return
    
    # Find placeholders
    placeholders = find_placeholders(template)
    display_placeholders(placeholders)
    
    # Get values
    values = get_placeholder_values(placeholders)
    
    # Preview
    preview_template(template, values)
    
    # Ask if user wants to save
    save = input("\nSave this email? (yes/no): ").lower()
    if save in ['yes', 'y']:
        recipient_name = values.get('recipient_name', 'recipient')
        filename = save_filled_email(fill_template(template, values), recipient_name)
        
        if filename:
            print("\n✓ Email saved successfully!")
            
            # Ask if user wants to open the file
            open_file = input("Open the file? (yes/no): ").lower()
            if open_file in ['yes', 'y']:
                print(f"\n📄 Opening {filename}...\n")
                print("="*50)
                with open(filename, 'r') as file:
                    print(file.read())
                print("="*50)


# ========== MAIN PROGRAM ==========
def main():
    """Main program"""
    print("\n" + "📧"*25)
    print("   WELCOME TO EMAIL TEMPLATE FILLER!")
    print("📧"*25)
    print("\nAutomate your email writing with templates!")
    
    while True:
        display_main_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            fill_single_email()
        
        elif choice == '2':
            batch_fill_templates()
        
        elif choice == '3':
            create_custom_template()
        
        elif choice == '4':
            view_templates()
        
        elif choice == '5':
            create_sample_templates()
        
        elif choice == '6':
            print("\n✓ Thank you for using Email Template Filler!")
            print("📧 Happy emailing!\n")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-6.")
        
        input("\nPress Enter to continue...")


# Run the program
if __name__ == "__main__":
    main()