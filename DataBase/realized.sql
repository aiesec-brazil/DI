select (extract(month from realized_at)) AS month,
		lc_home,
		product,
		count(id_application)as quantidade
FROM analitics_aiesec
where extract(year from realized_at) = '2019'
and mc_home = 'Brazil'
group by extract(month from realized_at),lc_home,product
order by extract(month from realized_at) ;

-- ICX
select (extract(month from realized_at)) AS month,
		lc_host,
		product,
		count(id_application)as quantidade
FROM analitics_aiesec
where extract(year from realized_at) = '2019'
and mc_host = 'Brazil'
group by extract(month from realized_at),lc_host,product
order by extract(month from realized_at) ;
