"""Start an async job and wait for its result."""

from autom import AutomClient

with AutomClient() as client:  # reads AUTOM_API_KEY
    submitted = client.google_search(query="web scraping api", is_async=True)
    job = client.wait_for_job(
        submitted.data["job_id"],
        on_progress=lambda j: print(j["status"], j.get("progress")),
    )
    print(job.data)
