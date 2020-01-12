SELECT bs.lc_home,bs.product,
		(select count(bs2.id_application) 
		   from analitics_aiesec bs2
		   where extract(year from approved_at) = '2019'
		   and bs2.lc_home = bs.lc_home
		   and bs2.product = bs.product) as approved,
		   	(select count(id_application) 
		   from analitics_aiesec bs2
		   where extract(year from realized_at) = '2019'
		   and bs2.lc_home = bs.lc_home
		   and bs2.product = bs.product) as realized,
				(select count(id_application) 
		   from analitics_aiesec bs2
		   where extract(year from completed_at) = '2019'
		   and bs2.lc_home = bs.lc_home
		   and bs2.product = bs.product) as completed
FROM analitics_aiesec bs
where extract(year from approved_at) >= '2019'
and mc_home = 'Brazil'
group by lc_home,product
order by lc_home ;