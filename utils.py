from bs4 import BeautifulSoup
import re
from typing import Optional


def clean_html_text(html_content: str, max_length: Optional[int] = None) -> str:
    """
    Clean HTML content for use in cold email generation by:
    - Removing all HTML tags
    - Extracting meaningful text
    - Preserving key information
    - Normalizing whitespace

    Args:
        html_content: Raw HTML string to clean
        max_length: Optional max length for truncated output

    Returns:
        Cleaned plain text suitable for email generation
    """
    try:
        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Remove unwanted elements
        for element in soup(['script', 'style', 'nav', 'footer', 'form', 'iframe', 'img']):
            element.decompose()

        # Get text and clean it
        text = soup.get_text(strip=True)

        # Normalize whitespace and clean special characters
        text = re.sub(r'\s+', ' ', text)  # Replace multiple whitespace with single space
        text = re.sub(r'\[.*?]', '', text)  # Remove anything in brackets
        text = re.sub(r'\bhttps?://\S+|www\.\S+', '', text)  # Remove URLs
        text = re.sub(r'[^\w\s.,;:!?\-@#$%&*()]', '', text)  # Keep only common punctuation

        # Truncate if needed
        if max_length and len(text) > max_length:
            text = text[:max_length].rsplit(' ', 1)[0] + '...'

        return text.strip()

    except Exception as e:
        print(f"Error cleaning HTML: {str(e)}")
        # Fallback to simple regex cleaning if BeautifulSoup fails
        return re.sub(r'<[^>]+>', '', html_content)[:2000] if html_content else ""