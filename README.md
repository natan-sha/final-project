# German Hospitals — Data Project

A data project looking at German hospitals from 2010 to today, with the
goal of illustrating the trends for hospitals in the regions (Kreises) where population is ageing and on the opposite, where the population is getting younger.

## The context
In 2025, Germany has initialised a hospital reform. The goal is to alleviate the financial pressure on hospitals, and to concentrate on quality, rather than quantity of procedures. As a result, the smaller hospitals may be merged, repurposed, or converted into specialized care centres. 
According to World Bank most recent data (SH.MED.BEDS.ZS), Germany has second highest number of hospital beds per capita in the European Union, at 7.6 beds per 1,000 inhabitants in 2022, compared to the EU average of 5.1. 
I would like to track what has been happening in Germany before the reform, especially in regards to the hospital care for the most vulnerable group of population - the elderly. Has Germany really have too many hospitals? Where in Germany has hospital access already been eroding, even before the reform was announced?

## The questions I'm investigating

1. **Are aging regions losing hospital access faster than others?**
   An *over-time* story: where has hospital access
   deteriorated the most from 2011 to 2023, and does that overlap with where the
   population was already oldest?

2. *(Additional question)* **Which specialisations are disappearing fastest
   in the oldest regions?** 

3. *(Additional question)*  **Were there any observable trends in Kreises with the youngest population?**   

## Data sources

| Source | Content| Years | Format |
|---|---|---|---|
| Destatis *Krankenhausverzeichnis* | One row per hospital, with Kreis ID and Fachabteilungen | 2011, 2015, 2019, 2023 | XLSX |
| Regionalstatistik table 12411-03-03-4 *(Bevölkerung nach Altersgruppen, Kreise)* | Population by Kreis × age group × year | 2011 onward | CSV |



## Folder structure

```
German hospitals/
├── data/
│   ├── raw/         <- Original data files. 
│   └── processed/   <- Cleaned-up data, prepared for analysis.
├── notebooks/       <- Jupyter notebooks for exploration and analysis.
├── outputs/         <- Final charts, maps, exports.
└── README.md
```


## Tools

Python, with pandas for data wrangling and plotly for
charts. 

## Open questions 

- **Kreis boundary reforms** (especially Mecklenburg-Vorpommern 2011)
  How to compare regions over time, with the change of boundaries?
- **Hospital identity across years** — when a hospital "disappears"
  between two snapshots, did it really close, or did it merge / rebrand?
