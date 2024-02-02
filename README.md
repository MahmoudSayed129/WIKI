# Wikipedia-like Online Encyclopedia
## Demonstration
Watch the [YouTube video](https://youtu.be/sJlBCyezEkk) to see the application in action.

## Project Overview
This project is a Django-based web application that emulates the core functionalities of Wikipedia, including viewing, searching, editing, and creating encyclopedia entries. It leverages Markdown for entry storage, allowing for a human-friendly editing and creation process, while dynamically converting Markdown to HTML for display.

### Features
- **Entry Viewing**: Access individual encyclopedia entries by navigating to `/wiki/TITLE`.
- **Search Functionality**: Integrated search to find entries or list potential matches.
- **Create New Entries**: Users can add new entries using Markdown formatting.
- **Edit Existing Entries**: Entries can be edited, promoting collaborative knowledge building.
- **Random Entry**: Navigate to a random encyclopedia entry for exploratory learning.
- **Markdown to HTML Conversion**: Seamlessly converts user-contributed Markdown to HTML for consistent and safe web display.

## Getting Started

### Prerequisites
- Python 3.x
- Django 2.x or 3.x
- markdown2 (for Markdown to HTML conversion)

### Installation
1. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/MahmoudSayed129/Wikipedia-like-Online-Encyclopedia.git
   ```
2. Navigate to the project directory:
   ```sh
   cd wikipedia-like-encyclopedia
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the Django development server:
   ```sh
   python manage.py runserver
   ```
2. Open a web browser and navigate to `http://127.0.0.1:8000` to view the application.

## Usage
- **Viewing an Entry**: Click on any entry title from the homepage or search for a specific entry using the search bar.
- **Adding a New Entry**: Click on "Create New Page" in the sidebar, fill in the title and Markdown content, and submit.
- **Editing an Entry**: On the entry page, click "Edit" to modify the content of an entry.
- **Random Entry**: Click on "Random Page" in the sidebar to view a random entry.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments
- Harvard University's CS50 course for the project idea and initial guidelines.
- The Django and Python communities for their invaluable resources and support.
