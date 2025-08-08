
import streamlit as st
from agents import research_topic
from exports import export_to_pdf, export_to_markdown

st.title("AutoResearcher --")
query = st.text_input("Enter your research topic:")
if st.button("Run Research") and query:
    with st.spinner("Researching..."):
        results = research_topic(query)
        st.success("Research complete!")
        for item in results:
            st.write(f"**Source:** {item['url']}")
            st.write(item['summary'])
        export_to_pdf(results, "report.pdf")
        export_to_markdown(results, "report.md")
        st.download_button("Download PDF", open("report.pdf", "rb"), "application/pdf")
        st.download_button("Download Markdown", open("report.md", "rb"), "text/markdown")
