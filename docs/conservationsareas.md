# Conservation Areas
  
## Send postcode, get data that overlaps with inspire polys within postcode`
 
```sql 
SELECT
	distinct a.inspire_id, a.inspire_poly, d.overlap_pc, e.conservation_key, e.wak, e.sssi_name, e.owner_title, e.owner_name, e.owner_org, e.start_date, e.expire_date, e.area, e.theme, e.theme_id, e.amount, e.conservation_area_poly, e.area_sqkm, e.area_sqmi
FROM inspire a, mapping_lsoa b, lsoa c, mapping_conservation d, conservation e
WHERE
	a.inspire_id=b.inspire_id and
	b.lsoa_11_cd = c.lsoa_11_cd and
	a.inspire_id = d.inspire_id and
	d.conservation_key = e.conservation_key and
	c.postcode = 'BS40 8SB'
```

## Send InspireID, get  data for a specific parcel

SELECT distinct a.inspire_id, a.inspire_poly, d.overlap_pc, e.conservation_key, e.wak, e.sssi_name, e.owner_title, e.owner_name, e.owner_org, e.start_date, e.expire_date, e.area, e.theme, e.theme_id, e.amount, e.conservation_area_poly, e.area_sqkm, e.area_sqmi
FROM inspire a, mapping_conservation d, conservation e
WHERE a.inspire_id = d.inspire_id
AND d.conservation_key = e.conservation_key
AND a.inspire_id=19422598

Contours

- 1. Send postcode, get data that overlaps with inspire polys within postcode

SELECT distinct a.inspire_id, a.inspire_poly, e.id, e.feat_type, e.sub_type, e.prop_value, e.contours_line
FROM inspire a, mapping_lsoa b, lsoa c, mapping_contours d, contours e
WHERE a.inspire_id=b.inspire_id 
AND b.lsoa_11_cd = c.lsoa_11_cd
AND a.inspire_id = d.inspire_id
AND d.id = e.id
AND c.postcode = 'BS40 8SB'

- 2. Send InspireID, get  data for a specific parcel

SELECT distinct a.inspire_id, a.inspire_poly, e.id, e.feat_type, e.sub_type, e.prop_value, e.contours_line
FROM inspire a, mapping_contours d, contours e
WHERE a.inspire_id = d.inspire_id
AND d.id = e.id
AND a.inspire_id=19904460



