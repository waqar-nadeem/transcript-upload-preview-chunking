import streamlit as st

# -------------------------------------------------
# Page configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Mehfil Meeting Transcript Summariser",
    page_icon="📝",
    layout="wide",
)

# -------------------------------------------------
# Helper function required by Task 2
# -------------------------------------------------
def chunk_text(text: str, max_words: int = 400) -> list[str]:
    """
    Split a long transcript into chunks of at most `max_words` words.
    Returns a list of strings. Each string contains ≤ max_words words.
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i : i + max_words])
        chunks.append(chunk)
    return chunks


# -------------------------------------------------
# Main UI
# -------------------------------------------------
st.title("📝 AI-Powered Meeting Transcript Summariser")
st.caption("Built for Mehfil Event Planners • Task 2 – Upload, Preview & Chunking")

st.markdown("---")

# File uploader
uploaded_file = st.file_uploader(
    "Upload a meeting transcript (.txt)",
    type=["txt"],
    help="Only plain-text .txt files are supported in this version.",
)

if uploaded_file is not None:
    # 1. Read the uploaded file into a string variable
    try:
        # Streamlit UploadedFile is a file-like object
        transcript = uploaded_file.read().decode("utf-8")
    except Exception as e:
        st.error(f"Could not read the file: {e}")
        st.stop()

    # Store raw transcript in session state (useful for later tasks)
    st.session_state["transcript"] = transcript

    # 2. Show the first 300 characters as a preview
    st.subheader("📄 Transcript Preview")
    preview = transcript[:300]
    st.write(preview + ("..." if len(transcript) > 300 else ""))

    # 3 & 4. Chunk the text and store in session state
    chunks = chunk_text(transcript, max_words=400)
    st.session_state["chunks"] = chunks

    # 5. Display the total number of chunks
    st.success(f"✅ Detected **{len(chunks)}** chunks ready for summarisation")

    # Extra helpful info (not required, but useful)
    with st.expander("See chunk details"):
        st.write(f"Total characters in transcript: {len(transcript):,}")
        st.write(f"Total words in transcript: {len(transcript.split()):,}")
        st.write(f"Number of chunks: {len(chunks)}")
        if chunks:
            st.write(f"Words in first chunk: {len(chunks[0].split())}")
            st.write(f"Words in last chunk: {len(chunks[-1].split())}")

else:
    # Clear previous state when no file is uploaded
    if "transcript" in st.session_state:
        del st.session_state["transcript"]
    if "chunks" in st.session_state:
        del st.session_state["chunks"]

    st.info("👆 Please upload a `.txt` meeting transcript to get started.")

# Footer
st.markdown("---")
st.caption("Mehfil Event Planners • AI Internship Project • Task 2 complete")
