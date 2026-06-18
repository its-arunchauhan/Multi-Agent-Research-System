from src.pipelines.pipeline import run_research_pipeline

def main():
    topic = "The impact of AI on the job market in 2026"

    print("\n" + "=" * 80)
    print("STARTING PIPELINE TEST")
    print("=" * 80)

    result = run_research_pipeline(topic)

    print("\n" + "=" * 80)
    print("PIPELINE COMPLETED")
    print("=" * 80)

    print("\nReturned State Keys:")
    print(result.keys())

    print("\nSearch Results Preview:")
    print(result["search_results"][:500])

    print("\nScraped Content Preview:")
    print(result["scraped_content"][:500])

    print("\nReport Preview:")
    print(result["report"][:1000])

    print("\nFeedback Preview:")
    print(result["feedback"])

if __name__ == "__main__":
    main()