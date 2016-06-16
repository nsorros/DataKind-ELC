# Land Classification
  
## Send postcode, get alc data that overlaps with inspire polys within postcode
  
```sql
SELECT
	distinct a.inspire_id, a.inspire_poly, d.overlap_pc, e.alc_grade, e.alc_spatial_poly
FROM
	inspire a, mapping_lsoa b, lsoa c, mapping_alc d, alc e
WHERE
	a.inspire_id=b.inspire_id and
	b.lsoa_11_cd = c.lsoa_11_cd and
	a.inspire_id = d.inspire_id and
	d.ogr_fid = e.ogr_fid and
	c.postcode = 'BS40 8SB'
```
  
## Send InspireID, get alc data for a specific parcel
  
```sql
SELECT
	distinct a.inspire_id, a.inspire_poly, d.overlap_pc, e.alc_grade,
	e.alc_spatial_poly, e.area_sqkm, e.area_sqmi
FROM
	inspire a, mapping_alc d, alc e
WHERE
	a.inspire_id = d.inspire_id and
	d.ogr_fid = e.ogr_fid and
	a.inspire_id=19422598
```