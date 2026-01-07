# Changelog

## 2026-01-07 - Query Format Update

### Changed
- **Updated all queries to AgentBeats official format**
  - First column now uses `id` instead of `agent_id` (requirement from AgentBeats)
  - Changed from `read_json_auto('results/*.json') AS results` to `FROM results` table
  - Added human-readable column names with proper quoting

### Added
- **New queries:**
  - "Detailed Performance Breakdown" - Comprehensive view of all metrics
  - Improved "Overall Performance" with assessment count

- **Documentation:**
  - `QUERIES.md` - Comprehensive query documentation
  - Query testing instructions
  - JSON structure reference

- **Testing improvements:**
  - Updated `test_queries.py` to use official AgentBeats format
  - Creates `results` table matching production environment
  - Better error reporting

### Query Changes Summary

| Query Name | Old Format | New Format | Status |
|-----------|-----------|-----------|--------|
| Overall Performance | `agent_id`, basic score | `id`, rounded score with assessment count | ✅ Improved |
| Empathy Rankings | `agent_id`, empathy_score | `id`, "Empathy Score" (rounded) | ✅ Updated |
| Persuasion Rankings | `agent_id`, persuasion_score | `id`, "Persuasion Score" (rounded) | ✅ Updated |
| Safety Rankings | `agent_id`, safety_score | `id`, "Safety Score" (rounded) | ✅ Updated |
| Success Rate | `agent_id`, success_rate | `id`, "Success Rate (%)" | ✅ Updated |
| Persona Performance | N/A | N/A | ❌ Removed (not agent-focused) |
| Recent Submissions | `agent_id`, basic data | `id`, grouped data | ✅ Updated |
| Detailed Breakdown | N/A | All metrics in one view | ✅ New |

### Test Results
All 7 queries passed validation:
```
✓ Overall Performance
✓ Empathy Rankings
✓ Persuasion Rankings
✓ Safety Rankings
✓ Success Rate
✓ Detailed Performance Breakdown
✓ Recent Submissions
```

### Breaking Changes
- Column names changed to quoted, human-readable format
- `agent_id` renamed to `id` in all queries
- "Persona Performance" query removed (didn't fit agent-focused leaderboard format)

### Migration Guide
No action required for existing submissions. The queries now properly follow AgentBeats conventions and will display correctly on the official leaderboard.
