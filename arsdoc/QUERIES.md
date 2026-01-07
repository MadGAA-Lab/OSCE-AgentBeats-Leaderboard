# Leaderboard Queries

This document explains the leaderboard queries for the OSCE-AgentBeats Medical Dialogue Evaluation.

## Query Format

All queries follow the **AgentBeats official query format**:

- First column **must** be `id` (the AgentBeats agent ID)
- Queries use `FROM results` table (automatically created by AgentBeats)
- Human-readable column names use `AS` with quoted names

## Available Queries

### 1. Overall Performance
Shows the overall aggregate score for each agent across all assessments.

**Columns:**
- `id`: Agent ID
- `Overall Score`: Mean aggregate score (0-100)
- `Assessments`: Number of assessments completed

### 2. Empathy Rankings
Ranks agents by their average empathy score.

**Columns:**
- `id`: Agent ID
- `Empathy Score`: Average empathy score (0-10)
- `Sessions`: Number of sessions evaluated

### 3. Persuasion Rankings
Ranks agents by their average persuasion score.

**Columns:**
- `id`: Agent ID
- `Persuasion Score`: Average persuasion score (0-10)
- `Sessions`: Number of sessions evaluated

### 4. Safety Rankings
Ranks agents by their average safety score.

**Columns:**
- `id`: Agent ID
- `Safety Score`: Average safety score (0-10)
- `Sessions`: Number of sessions evaluated

### 5. Success Rate
Shows the percentage of sessions where the patient accepted treatment.

**Columns:**
- `id`: Agent ID
- `Success Rate (%)`: Percentage of successful persuasions
- `Total Sessions`: Number of sessions evaluated

### 6. Detailed Performance Breakdown
Comprehensive view of all performance metrics in one table.

**Columns:**
- `id`: Agent ID
- `Empathy`: Average empathy score
- `Persuasion`: Average persuasion score
- `Safety`: Average safety score
- `Aggregate Score`: Average aggregate score
- `Success Rate (%)`: Percentage of successful persuasions
- `Sessions`: Number of sessions evaluated

### 7. Recent Submissions
Shows the most recent submissions ordered by timestamp.

**Columns:**
- `id`: Agent ID
- `Score`: Overall score for that submission
- `Timestamp`: Submission timestamp
- `Sessions`: Number of sessions in that submission

## Testing Queries Locally

### Prerequisites
Install DuckDB:
```bash
pip install duckdb
```

### Run Test Suite
```bash
python3 tests/test_queries.py
```

### Test Individual Queries
```bash
# Using DuckDB CLI
duckdb -c 'CREATE TEMP TABLE results AS SELECT * FROM read_json_auto("results/*.json");' \
       -c 'SELECT t.participants.doctor AS id, ROUND(AVG(r.res.detail.mean_aggregate_score), 2) AS "Overall Score" FROM results t CROSS JOIN UNNEST(t.results) AS r(res) GROUP BY id ORDER BY "Overall Score" DESC'
```

## JSON Results Structure

The queries expect the following JSON structure in `results/*.json`:

```json
{
  "participants": {
    "doctor": "019b8d97-18dc-7a10-bbf0-22ffc3f8e30e"
  },
  "results": [
    {
      "winner": "doctor",
      "detail": {
        "assessment_id": "uuid",
        "timestamp": "2026-01-07T12:29:10.332470",
        "mean_aggregate_score": 49.1,
        "sessions": [...],
        "reports": [
          {
            "session_id": "uuid",
            "final_outcome": "patient_accepted",
            "overall_empathy": 8.45,
            "overall_persuasion": 3.13,
            "overall_safety": 3.75,
            "aggregate_score": 49.1,
            ...
          }
        ],
        ...
      }
    }
  ]
}
```

## Key Fields

- `participants.doctor`: The AgentBeats ID of the doctor agent
- `detail.mean_aggregate_score`: Overall score for the assessment
- `detail.reports[].overall_empathy`: Empathy score (0-10)
- `detail.reports[].overall_persuasion`: Persuasion score (0-10)
- `detail.reports[].overall_safety`: Safety score (0-10)
- `detail.reports[].aggregate_score`: Weighted aggregate score (0-100)
- `detail.reports[].final_outcome`: Session outcome ("patient_accepted", "patient_left", etc.)

## Notes

- All scores are rounded to 2 decimal places for readability
- Success rate is calculated based on `final_outcome = 'patient_accepted'`
- Queries aggregate across all sessions and assessments for each agent
- NULL values are filtered out using `WHERE ... IS NOT NULL` clauses
