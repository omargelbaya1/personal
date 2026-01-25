--Find how many times each artist appeared on the Spotify ranking list.
--Output the artist name along with the corresponding number of occurrences.
--Order records by the number of occurrences in descending order.


select artist,count(*) as no_of_occurrences from spotify_worldwide_daily_song_ranking
group by 1
order by 2 desc;


--other variation:
select artist, count(id) as occurrences
from spotify_worldwide_daily_song_ranking
group by 1
order by 2 desc