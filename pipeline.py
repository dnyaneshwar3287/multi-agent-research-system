def run_research_pipeline(topic: str):
    print(f"Running pipeline for topic: {topic}")

    # Step 1: Simulated search
    search_results = f"Top search results about '{topic}'"

    # Step 2: Simulated research extraction
    research = f"Detailed research insights about '{topic}' including key points, trends, and facts."

    # Step 3: Draft report
    report = f"This is a draft report on '{topic}'. It summarizes the main findings."

    # Step 4: Final report
    final_report = f"""
    FINAL REPORT ON: {topic}

    1. Introduction
    {topic} is an important subject.

    2. Key Insights
    - Insight 1
    - Insight 2

    3. Conclusion
    This concludes the research on {topic}.
    """

    return {
        "search_results": search_results,
        "research": research,
        "report": report,
        "final_report": final_report
    }