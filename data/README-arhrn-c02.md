# ARHRN C-02 derived province-year panel (2016–2025)

This file is an AptToSell/ARHRN **B-grade practical data product**, not a peer-reviewed causal study or a DOI deposit.

**CSV:** [arhrn-c02-apartment-supply-net-migration-2016-2025.csv](./arhrn-c02-apartment-supply-net-migration-2016-2025.csv)

- Scope: 17 South Korean provinces/metropolitan cities × 10 years (2016–2025), 170 province-year observations; no person-level records.
- `completed_apartment_units`: annual apartment completions, units, from Ministry of Land, Infrastructure and Transport housing completion statistics.
- `previous_nov1_apartment_stock_units`: previous-year **November 1** apartment housing stock from KOSIS housing census `DT_1JU1501`; **not** December 31 stock.
- `derived_completion_ratio_pct`: 100 × completions / previous Nov 1 stock, not official occupancy or net-stock-growth rate.
- `net_migrants_people`: annual in-migration minus out-migration (persons).
- `official_net_migration_rate_pct_2dp`: official migration rate (%) as reported to two decimals. 2016–2024 values were transcribed from an official online table; independent full machine-readable source re-extraction has **not** been completed.
- `capital_area`: 수도권 means 서울·인천·경기; the other 14 regions are 비수도권.

Official sources:
- MOLIT completions: https://stat.molit.go.kr/portal/cate/statMetaView.do?hRsId=468
- KOSIS housing stock: https://kosis.kr/statisticsList/mass/mass_list.jsp?org_id=101&process=statHtml&tbl_id=DT_1JU1501
- Government migration indicator: https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?freq=Y&idx_cd=F0015&period=N&stts_cd=F001501

Interpretation: Correlation is not causation; aggregate region-year data cannot identify moves from old to new apartments or an individual complex's occupancy. The national 170-observation Pearson correlation was 0.843; removing all Sejong observations (160 observations) yielded 0.516. Year/region fixed-effects sensitivities did not establish a robust capital-vs-noncapital difference.

No source ZIPs, person-level records, or institutional endorsement are bundled. Check official data usage and amendment notices before further redistribution or high-stakes use. AI assisted data processing and drafting; human editorial review is required for subsequent changes.

Project id: ARHRN-NEW-SUPPLY-RESIDENTIAL-MOBILITY-C02-20261111. No DOI issued.
