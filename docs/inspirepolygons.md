# Inspire Polygons

## Send Postcode, get inspire data

```sql
SELECT
	distinct a.inspire_id, a.inspire_poly, a.gml_id, a.valid_from_dt,
	a.begin_lifespan_dt, a.area_sqkm, a.area_sqmi, a.acres
FROM
	inspire a, mapping_lsoa b, lsoa c
WHERE
	a.inspire_id=b.inspire_id and
	b.lsoa_11_cd = c.lsoa_11_cd and
	c.postcode = 'BS40 8SB'
```

- 2. Send InspireID, get inspire data

SELECT distinct a.inspire_id, a.inspire_poly, a.gml_id, a.valid_from_dt, a.begin_lifespan_dt, a.area_sqkm, a.area_sqmi, a.acres
FROM inspire a
WHERE a.inspire_id=19422598
