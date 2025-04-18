import json
def generate_summary(extracted_data):
    # Step 1: Validate and sanitize the input data
    if not isinstance(extracted_data, dict):
        return "Invalid input: extracted_data must be a dictionary."

    # Helper function to safely access nested fields
    def safe_get(data, key, default="Not provided"):
        value = data.get(key, default)
        return value if value else default

    # Step 2: Dynamically extract and format fields
    summary_parts = []

    # Add full name (if available)
    full_name = safe_get(extracted_data, "full_name", "No name provided")
    summary_parts.append(f"Applicant: {full_name}")

    # Add contact information (email, phone, LinkedIn, GitHub)
    contact_info = []
    for field in ["email", "phone", "linkedin", "github"]:
        value = safe_get(extracted_data, field, "Not provided")
        contact_info.append(f"{field.capitalize()}: {value}")
    if contact_info:
        summary_parts.append("Contact Information:")
        summary_parts.extend([f"  {info}" for info in contact_info])

    # Add professional summary (if available)
    summary_text = safe_get(extracted_data, "summary", "No summary provided")
    summary_parts.append(f"Summary: {summary_text}")

    # Dynamically process other fields
    for key, value in extracted_data.items():
        if key in ["full_name", "email", "phone", "linkedin", "github", "summary"]:
            continue  # Skip already processed fields

        if isinstance(value, list):
            # Handle lists (e.g., certifications, projects)
            formatted_list = ", ".join(map(str, value)) if value else "None listed"
            summary_parts.append(f"{key.capitalize()}: {formatted_list}")

        elif isinstance(value, dict):
            # Handle nested dictionaries (e.g., skills, education)
            nested_parts = []
            for sub_key, sub_value in value.items():
                if isinstance(sub_value, list):
                    sub_value = ", ".join(sub_value) if sub_value else "None listed"
                nested_parts.append(f"{sub_key.capitalize()}: {sub_value}")
            summary_parts.append(f"{key.capitalize()}:")
            summary_parts.extend([f"  {part}" for part in nested_parts])

        else:
            # Handle simple key-value pairs
            summary_parts.append(f"{key.capitalize()}: {value}")

    # Step 3: Combine all parts into a single summary string
    return "\n".join(summary_parts)
