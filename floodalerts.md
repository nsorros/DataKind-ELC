# Flood Alerts

`Send postcode, get data that overlaps with inspire polys within postcode`
  
```sql
SELECT
	distinct a.inspire_id, a.inspire_poly, d.overlap_pc, e.region,
	e.fwis_code, e.fwa_name, e.descrip, e.river_sea,
	e.county, e.e_qdial, e.w_region, e.w_fwa_name,
	e.w_descrip, e.w_afon, e.w_qdial, e.flood_alert_poly,
	e.area, e.fwd_tacode, e.area_sqkm, e.area_sqmi 
FROM
	inspire a, mapping_lsoa b, lsoa c, mapping_flood_alerts d, flood_alerts e
WHERE
	a.inspire_id=b.inspire_id and
	b.lsoa_11_cd = c.lsoa_11_cd and
	a.inspire_id = d.inspire_id and
	d.fwis_code = e.fwis_code and
	c.postcode = 'BS40 8SB'
```
  
`Send InspireID, get  data for a specific parcel`
  
```sql
SELECT
	distinct a.inspire_id, a.inspire_poly, d.overlap_pc, e.region,
	e.area, e.fwd_tacode, e.fwis_code, e.fwa_name,
	e.descrip, e.river_sea, e.county, e.e_qdial,
	e.w_region, e.w_fwa_name, e.w_descrip, e.w_afon,
	e.w_qdial, e.flood_alert_poly, e.area_sqkm, e.area_sqmi
FROM
	inspire a, mapping_flood_alerts d, flood_alerts e
WHERE
	a.inspire_id = d.inspire_id and
	d.fwis_code = e.fwis_code and
	a.inspire_id=19524093
```