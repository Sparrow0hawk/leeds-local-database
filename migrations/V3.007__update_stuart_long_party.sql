-- Stuart Long stood with no affiliation and declined to stand as an Independent
update election.results
set party_id = 49
where candidate_surname = 'Long' and candidate_forename LIKE 'Stuart%';
