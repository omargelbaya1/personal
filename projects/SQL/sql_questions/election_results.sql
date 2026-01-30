--The election is conducted in a city and everyone can vote for one or more candidates, or choose not to vote at all. Each person has 1 vote so if they vote for multiple candidates, their vote gets equally split across these candidates. For example, if a person votes for 2 candidates, these candidates receive an equivalent of 0.5 vote each. Some voters have chosen not to vote, which explains the blank entries in the dataset.
--
--
--Find out who got the most votes and won the election. Output the name of the candidate or multiple names in case of a tie.
--To avoid issues with a floating-point error you can round the number of votes received by a candidate to 3 decimal places.



WITH VOTE AS
(select voter,  count(distinct voter)/count(voter)::float as votes
from voting_results
where candidate is not null
group by voter)

select voting_results.candidate, sum(votes)
from voting_results
left join VOTE
on voting_results.voter = VOTE.voter
where voting_results.candidate is not null
group by candidate
order by sum(votes) desc
limit 1