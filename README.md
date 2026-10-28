# Task 2: Transcript Upload Handling and Preview with Chunking

**Project:** AI-Powered Meeting Transcript Summariser for Mehfil Event Planners  
**Client:** Mehfil Event Planners  
**Intern:** Waqar Nadeem  
**Technology:** Artificial Intelligence (Streamlit + Python)

## Task Overview
Extend the app to read an uploaded `.txt` meeting transcript, display the first 300 characters as a preview, and split the full transcript into ≤400-word chunks stored in session state.

**Status:** Task 2 Complete

## Features Implemented
- Upload a plain-text (`.txt`) meeting transcript
- Instant preview of the first 300 characters
- Automatic splitting into chunks of ≤ 400 words (approx. 500 tokens)
- Chunks stored in Streamlit session state for later summarisation
- Clear feedback: “Detected X chunks ready for summarisation”

## How to Run Locally

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd transcript-upload-preview-chunking

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

Open the URL shown in the terminal (usually http://localhost:8501).

## Sample Data
A realistic wedding-planning meeting transcript is provided in:
```
sample_data/sample_meeting_transcript.txt
```
Upload this file to test the app.

## Project Structure
```
transcript-upload-preview-chunking/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── .gitignore
└── sample_data/
    └── sample_meeting_transcript.txt
```

## Task Progress
| # | Task                                      | Status     | Days |
|---|-------------------------------------------|------------|------|
| 1 | Project repository, environment, landing page | Done (base) | 2    |
| 2 | Transcript upload, preview & chunking     | **Completed** | 3 |
| 3 | Integrate open-source summarisation model | Pending    | 4    |
| 4 | Quality checklist for the summary         | Pending    | 2    |
| 5 | Downloadable report (Markdown → PDF)      | Pending    | 3    |
| 6 | Deploy to Streamlit Cloud + handover doc | Pending    | 3    |

## Notes for Mentor (Task 2)
- Implemented `chunk_text()` using simple word splitting (max 400 words per chunk).
- Preview shows exactly the first 300 characters via `st.write`.
- Chunks are stored in `st.session_state["chunks"]`.
- The page clearly displays the number of detected chunks.
- Sample transcript included for easy testing.

## Next Steps (Task 3)
Integrate an open-source summarisation model (e.g. Hugging Face `facebook/bart-large-cnn` or a lightweight alternative) to summarise each chunk and then combine the results.
