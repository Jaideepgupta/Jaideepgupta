<div align="center">

<picture><source media="(prefers-color-scheme: light)" srcset="./assets/profile-banner-light.svg" /><img src="./assets/profile-banner.svg" alt="Jaideep Gupta: Tableau Developer moving into Analytics & Data Engineering. Animated pipeline from sources through bronze, silver and gold layers to Tableau and Power BI." width="100%" /></picture>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=18&duration=3500&pause=900&color=3ECF8E&center=true&vCenter=true&width=800&height=30&lines=4%2B+years+in+BI+%7C+11+client+engagements;Now+building+the+pipelines+behind+the+dashboards;ADF+%E2%86%92+Databricks+%E2%86%92+dbt+%E2%86%92+Power+BI+%7C+Kafka+%2B+Airflow" alt="4+ years in BI, 11 client engagements. Now building the pipelines behind the dashboards." />
</a>

<br>

[![Email](https://img.shields.io/badge/-Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jaideepg.jg@gmail.com)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/guptajaideep)
[![Tableau Public](https://img.shields.io/badge/-Tableau%20Public-1A73E8?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/jaideep.gupta7070/vizzes)
[![Portfolio](https://img.shields.io/badge/-Portfolio-6E40C9?style=for-the-badge&logo=googlechrome&logoColor=white)](https://codebasics.io/portfolio/Jaideep-Gupta)
[![YouTube](https://img.shields.io/badge/-YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UCMU9RMjwpglKIhV7HZ0m_5w)

<sub>📍 India &nbsp;·&nbsp; M.Sc. Economics, IIT Roorkee &nbsp;·&nbsp; B.Sc. Statistics & Mathematics, CSJMU</sub>

<br>

<a href="#about"><img alt="About" src="https://img.shields.io/badge/About-21262d?style=flat-square&labelColor=21262d&color=21262d" /></a> <a href="#projects"><img alt="Projects" src="https://img.shields.io/badge/Projects-21262d?style=flat-square&labelColor=21262d&color=21262d" /></a> <a href="#stack"><img alt="Stack" src="https://img.shields.io/badge/Stack-21262d?style=flat-square&labelColor=21262d&color=21262d" /></a> <a href="#experience"><img alt="Experience" src="https://img.shields.io/badge/Experience-21262d?style=flat-square&labelColor=21262d&color=21262d" /></a> <a href="#focus"><img alt="Current focus" src="https://img.shields.io/badge/Current%20focus-21262d?style=flat-square&labelColor=21262d&color=21262d" /></a>

</div>

<br>

## 🧭 About <a id="about"></a>

I'm a Tableau Developer with 4+ years building BI for **Healthcare, Real Estate, EdTech, and Enterprise** teams, delivering Tableau and Tableau Next solutions across **11 client engagements** in **6+ industries**. Working on the reporting layer showed me that most problems in a dashboard start upstream, in ingestion, modeling, and data quality. So I've moved into engineering that upstream layer myself.

My recent work is end to end: metadata-driven ingestion with ADF, medallion transforms on Databricks, a dbt Gold layer with tests in CI, Kafka + Structured Streaming with Airflow, and the Power BI / Tableau layer on top. I'm looking for **Tableau Developer** and **Analytics Engineer** roles where I can own the path from raw data to a dashboard number the business trusts.

<picture><source media="(prefers-color-scheme: light)" srcset="./assets/stats-light.svg" /><img src="./assets/stats.svg" alt="4+ years in BI and analytics · 11 client engagements · 6+ industries · 6 Tableau Next POCs" width="100%" /></picture>

<br>

## 🚀 Featured Projects <a id="projects"></a>

### 🛠️ Data Engineering

<table>
<tr>
<td valign="top">

#### 🛒 AtliQ Commerce: End-to-End Data Platform (Batch + Real-Time)

<a href="https://github.com/Jaideepgupta/AtliQ-Commerce-End-to-End-Capstone"><picture><source media="(prefers-color-scheme: light)" srcset="./assets/atliq-architecture-light.svg" /><img src="./assets/atliq-architecture.svg" alt="AtliQ Commerce architecture. Batch: Azure SQL to ADF to Bronze on ADLS Gen2, Silver on Databricks, Gold in dbt, Power BI on Fabric. Streaming: Kafka to Structured Streaming bronze, silver and gold, run by Airflow." width="100%" /></picture></a>

<img alt="Azure Data Factory" src="https://img.shields.io/badge/Azure%20Data%20Factory-21262d?style=flat-square&logo=microsoftazure&logoColor=0078D4" />
<img alt="Databricks" src="https://img.shields.io/badge/Databricks-21262d?style=flat-square&logo=databricks&logoColor=FF3621" />
<img alt="dbt Core" src="https://img.shields.io/badge/dbt%20Core-21262d?style=flat-square&logo=dbt&logoColor=FF694B" />
<img alt="Apache Kafka" src="https://img.shields.io/badge/Apache%20Kafka-21262d?style=flat-square&logo=apachekafka&logoColor=white" />
<img alt="Spark Streaming" src="https://img.shields.io/badge/Spark%20Streaming-21262d?style=flat-square&logo=apachespark&logoColor=E25A1C" />
<img alt="Apache Airflow" src="https://img.shields.io/badge/Apache%20Airflow-21262d?style=flat-square&logo=apacheairflow&logoColor=017CEE" />
<img alt="Microsoft Fabric" src="https://img.shields.io/badge/Microsoft%20Fabric-21262d?style=flat-square" />
<img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-21262d?style=flat-square&logo=githubactions&logoColor=2088FF" />

- **Batch:** a control-table-driven ADF pipeline lands OLTP data in Bronze. Databricks does incremental `MERGE` into Silver, and a dbt Gold star schema is served to Power BI / Fabric.
- **Streaming:** a Kafka producer feeds Structured Streaming Bronze → Silver → Gold, with watermarking, deduplication, and separate checkpoints. An Airflow DAG runs the operations.
- **Reliability:** dbt tests gate CI. Revenue, cost, and profit reconcile back to source, and re-running the full pipeline and diffing the results shows it is idempotent.

<img alt="dbt models: 13/13 passing" src="https://img.shields.io/badge/dbt%20models-13%2F13%20passing-3ecf8e?style=flat-square&labelColor=21262d" /> <img alt="dbt tests: 18/18 passing" src="https://img.shields.io/badge/dbt%20tests-18%2F18%20passing-3ecf8e?style=flat-square&labelColor=21262d" /> <img alt="idempotency: verified" src="https://img.shields.io/badge/idempotency-verified-3ecf8e?style=flat-square&labelColor=21262d" />

<a href="https://github.com/Jaideepgupta/AtliQ-Commerce-End-to-End-Capstone"><img alt="View Repo" src="https://img.shields.io/badge/View%20Repo-238636?style=for-the-badge&logo=github&logoColor=white" /></a>

</td>
</tr>
</table>

### 🤖 ML, NLP & Applied Engineering

<table>
<tr>
<td width="50%" valign="top">

#### 📉 Customer Churn Intelligence

<img alt="Python" src="https://img.shields.io/badge/Python-21262d?style=flat-square&logo=python&logoColor=3776AB" />
<img alt="scikit-learn" src="https://img.shields.io/badge/scikit--learn-21262d?style=flat-square&logo=scikitlearn&logoColor=F7931E" />
<img alt="NLP · TF-IDF" src="https://img.shields.io/badge/NLP%20%C2%B7%20TF--IDF-21262d?style=flat-square" />
<img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-21262d?style=flat-square&logo=streamlit&logoColor=FF4B4B" />
<img alt="pytest" src="https://img.shields.io/badge/pytest-21262d?style=flat-square&logo=pytest&logoColor=0A9EDC" />

Predicts which of 10,000 SaaS accounts will churn, using product telemetry plus sentiment features from support tickets. In the data, negative sentiment shows up **2–3 weeks before** usage drops.

<img alt="recall: 98.7%" src="https://img.shields.io/badge/recall-98.7%25-3ecf8e?style=flat-square&labelColor=21262d" /> <img alt="ARR at risk: $9.09M" src="https://img.shields.io/badge/ARR%20at%20risk-%249.09M-3ecf8e?style=flat-square&labelColor=21262d" /> <img alt="tests: 50/50" src="https://img.shields.io/badge/tests-50%2F50-3ecf8e?style=flat-square&labelColor=21262d" />

<a href="https://jaideepgupta-customer-churn-intelligence---predictiv-app-qaupr1.streamlit.app/"><img alt="Live App" src="https://img.shields.io/badge/Live%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" /></a> <a href="https://github.com/Jaideepgupta/Customer-Churn-Intelligence---Predictive-Analytics---NLP"><img alt="Repo" src="https://img.shields.io/badge/Repo-238636?style=for-the-badge&logo=github&logoColor=white" /></a>

</td>
<td width="50%" valign="top">

#### 🎬 VideoScribe

<img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-21262d?style=flat-square&logo=fastapi&logoColor=009688" />
<img alt="Celery" src="https://img.shields.io/badge/Celery-21262d?style=flat-square&logo=celery&logoColor=37814A" />
<img alt="Redis" src="https://img.shields.io/badge/Redis-21262d?style=flat-square&logo=redis&logoColor=FF4438" />
<img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-21262d?style=flat-square&logo=postgresql&logoColor=4169E1" />
<img alt="Next.js" src="https://img.shields.io/badge/Next.js-21262d?style=flat-square&logo=nextdotjs&logoColor=white" />
<img alt="Docker" src="https://img.shields.io/badge/Docker-21262d?style=flat-square&logo=docker&logoColor=2496ED" />

Turns a video link or upload into clean, searchable text. FastAPI hands jobs to Celery workers (yt-dlp + ffmpeg + speech-to-text), which write output to S3-compatible storage. Includes timestamp navigation, keyword search, and multi-format export.

<img alt="deploy: docker compose up" src="https://img.shields.io/badge/deploy-docker%20compose%20up-3ecf8e?style=flat-square&labelColor=21262d" />

<a href="https://github.com/Jaideepgupta/Videoscribe"><img alt="Repo" src="https://img.shields.io/badge/Repo-238636?style=for-the-badge&logo=github&logoColor=white" /></a>

</td>
</tr>
</table>

### 📊 BI & Analytics

<table>
<tr>
<td width="50%" valign="top">

#### 💊 Pharmacy Sales Dashboard

<img alt="Tableau" src="https://img.shields.io/badge/Tableau-21262d?style=flat-square&logo=tableau&logoColor=1A73E8" />
<img alt="Excel" src="https://img.shields.io/badge/Excel-21262d?style=flat-square" />

<a href="https://jaideepgupta.github.io/Jaideepgupta/pharmacy-dashboard.html"><img src="https://public.tableau.com/static/images/Ph/PharmacyDashboard_5_17696851082490/PharmacyPerformance/1.png" alt="Pharmacy dashboard preview" width="100%" /></a>

8 analytical views for pharma sales managers: rep performance, doctor engagement, effort vs. output, target achievement, and call-outcome quality.

<a href="https://jaideepgupta.github.io/Jaideepgupta/pharmacy-dashboard.html"><img alt="Live Dashboard" src="https://img.shields.io/badge/Live%20Dashboard-1A73E8?style=for-the-badge&logo=tableau&logoColor=white" /></a> <a href="https://github.com/Jaideepgupta/Pharmacy-sales-dashboard"><img alt="Repo" src="https://img.shields.io/badge/Repo-238636?style=for-the-badge&logo=github&logoColor=white" /></a>

</td>
<td width="50%" valign="top">

#### 📊 Business Insights 360

<img alt="Power BI" src="https://img.shields.io/badge/Power%20BI-21262d?style=flat-square&logo=powerbi&logoColor=F2C811" />
<img alt="SQL" src="https://img.shields.io/badge/SQL-21262d?style=flat-square" />
<img alt="DAX" src="https://img.shields.io/badge/DAX-21262d?style=flat-square" />

Finance, Sales, Marketing, Supply Chain, and Executive views for a consumer-electronics company across 27+ markets. Star schema over 1M+ transactions, tracking net sales, gross margin %, and forecast accuracy.

<img alt="markets: 27+" src="https://img.shields.io/badge/markets-27%2B-3ecf8e?style=flat-square&labelColor=21262d" /> <img alt="transactions: 1M+" src="https://img.shields.io/badge/transactions-1M%2B-3ecf8e?style=flat-square&labelColor=21262d" />

<a href="https://app.powerbi.com/view?r=eyJrIjoiMzBiNWE5NTgtYWRkYi00MmZlLWE3NmQtMzIzYmJmNzQzMWFkIiwidCI6ImM2ZTU0OWIzLTVmNDUtNDAzMi1hYWU5LWQ0MjQ0ZGM1YjJjNCJ9"><img alt="Live Dashboard" src="https://img.shields.io/badge/Live%20Dashboard-C9A800?style=for-the-badge&logo=powerbi&logoColor=white" /></a> <a href="https://github.com/Jaideepgupta/Business_Insights_360"><img alt="Repo" src="https://img.shields.io/badge/Repo-238636?style=for-the-badge&logo=github&logoColor=white" /></a>

</td>
</tr>
</table>

<details>
<summary><b>More projects</b></summary>
<br>

- **[BRSR / ESG Data Story](https://jaideepgupta.github.io/brsr-esg-data-story/)**: an interactive walkthrough of ESG capability data for 99 companies, covering Spearman correlation with Holm correction, Poisson regression (IRR), robust SEs, and ANOVA.
- **[E-commerce Lakehouse ML Pipeline](https://github.com/Jaideepgupta/ecommerce-lakehouse-ml-pipeline)**: Databricks Bronze/Silver/Gold feature pipeline feeding purchase-prediction and recommendation models.
- **[AtliQ Hotels — Hospitality EDA](https://github.com/Jaideepgupta/hospitality-eda-atliq-hotels)**: Pandas analysis of occupancy, revenue, cancellations, and channel mix across four cities.
- **[Sales & Finance Analytics](https://github.com/Jaideepgupta/Excel-Sales-Analytics)**: Excel / Power Query P&L across 15+ markets and 200+ customers.
- **Reference notes:** [dbt cheatsheet](https://github.com/Jaideepgupta/dbt-cheatsheet) · [Tableau cheatsheet](https://github.com/Jaideepgupta/tableau-cheatsheet) · [SQL prep](https://github.com/Jaideepgupta/sql-prep)

</details>

<br>

## 🧰 Stack <a id="stack"></a>

<div align="center">

**BI & Visualization**
<br>
<img alt="Tableau" src="https://img.shields.io/badge/Tableau-1A73E8?style=flat-square&logo=tableau&logoColor=white" />
<img alt="Tableau Next" src="https://img.shields.io/badge/Tableau%20Next-1A73E8?style=flat-square&logo=salesforce&logoColor=white" />
<img alt="Salesforce Data Cloud" src="https://img.shields.io/badge/Salesforce%20Data%20Cloud-00A1E0?style=flat-square&logo=salesforce&logoColor=white" />
<img alt="Power BI" src="https://img.shields.io/badge/Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black" />
<img alt="DAX" src="https://img.shields.io/badge/DAX-000000?style=flat-square" />
<img alt="Excel" src="https://img.shields.io/badge/Excel-217346?style=flat-square&logo=microsoftexcel&logoColor=white" />
<img alt="Mixpanel" src="https://img.shields.io/badge/Mixpanel-7856FF?style=flat-square&logo=mixpanel&logoColor=white" />

**Analytics Engineering & Data Platforms**
<br>
<img alt="Databricks" src="https://img.shields.io/badge/Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white" />
<img alt="dbt" src="https://img.shields.io/badge/dbt-FF694B?style=flat-square&logo=dbt&logoColor=white" />
<img alt="Apache Spark" src="https://img.shields.io/badge/Apache%20Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white" />
<img alt="Apache Kafka" src="https://img.shields.io/badge/Apache%20Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white" />
<img alt="Apache Airflow" src="https://img.shields.io/badge/Apache%20Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white" />
<img alt="Azure Data Factory" src="https://img.shields.io/badge/Azure%20Data%20Factory-0078D4?style=flat-square&logo=microsoftazure&logoColor=white" />
<img alt="Microsoft Fabric" src="https://img.shields.io/badge/Microsoft%20Fabric-117865?style=flat-square" />

**Languages, Databases & Tooling**
<br>
<img alt="SQL" src="https://img.shields.io/badge/SQL-025E8C?style=flat-square&logo=postgresql&logoColor=white" />
<img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
<img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" />
<img alt="MySQL" src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white" />
<img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" />
<img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
<img alt="Git" src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" />
<img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" />

</div>

<br>

## 💼 Experience <a id="experience"></a>

```
Aug 2025 ── Present     Tableau Developer · Kloudrac Group
Sep 2024 ── Aug 2025    Freelance Data Analyst
Jan 2024 ── Sep 2024    Associate Solution Leader · Brane Enterprises
Jun 2022 ── Dec 2023    SME → Product Analyst · TutorBin
```

<details open>
<summary><b>Tableau Developer</b> · Kloudrac Group &nbsp; <code>Aug 2025 – Present</code></summary>
<br>

- Delivered Tableau analytics for **11 client engagements across 6+ industries** (healthcare, pharma, real estate, logistics, manufacturing, renewable energy), from requirements gathering to dashboard handover
- Built a **5-page Tableau app** for an 8-hospital doctor-referral program (30K+ field visits, 3.8K referrals, 45+ reps), with drill-through from network to hospital to rep, parameters and month-on-month calculations
- Standardized **6 program KPIs** with definitions documented inside the dashboard, so all 8 hospitals measured performance the same way
- Built an executive revenue and inventory dashboard for a real-estate business, with quarter-on-quarter comparisons and 5-level sales-hierarchy filters across 15+ projects
- Built **6 Tableau Next POCs** on Salesforce Data Cloud for manufacturing, real-estate and healthcare prospects, showing agentic analytics and AI-driven insights

</details>

<details>
<summary><b>Freelance Data Analyst</b> &nbsp; <code>Sep 2024 – Aug 2025</code></summary>
<br>

- Delivered analytics projects for clients in Tableau, Power BI, SQL and Excel, covering data cleaning, KPI design and dashboards
- Built revenue, retention and lead-conversion dashboards that moved clients' recurring reporting from manual Excel files to interactive BI
- Trained 50+ students and professionals in SQL, Tableau and Power BI

</details>

<details>
<summary><b>Associate Solution Leader</b> · Brane Enterprises &nbsp; <code>Jan 2024 – Sep 2024</code></summary>
<br>

- Delivered BI and reporting projects for enterprise stakeholders end to end, from requirements gathering to sign-off
- Built reusable SQL templates and standardized KPI definitions so teams reported with consistent metric logic instead of separate spreadsheets

</details>

<details>
<summary><b>Subject Matter Expert → Product Analyst</b> · TutorBin &nbsp; <code>Jun 2022 – Dec 2023</code></summary>
<br>

- Analysed onboarding behaviour in Mixpanel and identified funnel drop-off points, giving the product team evidence to prioritise improvements
- Built dashboards tracking DAU, 30-day retention, conversion and feature adoption for product and leadership
- Ran funnel and cohort analyses to compare user groups and inform feature prioritisation
- Mentored 50+ students and professionals in statistics, SQL, Power BI and Tableau; supervised interns

</details>

<br>

## 🌱 Current Focus <a id="focus"></a>

- **Snowflake + AWS S3:** loading raw files from S3 into Snowflake (external stages, `COPY INTO`, Snowpipe), with Tableau running on top of Snowflake
- **Analytics engineering in depth:** dbt incremental models, snapshots (SCD2), contracts, and data-quality testing
- **Tableau at scale:** semantic layers, extract vs. live trade-offs, and performance tuning on warehouse-backed data sources
- **AI for analytics:** Tableau Next / agentic analytics, LLM applications and MCP servers over governed warehouse data

<br>

## 🎓 Education & Certifications

<table>
<tr>
<td valign="top" width="50%">

**Education**
- M.Sc. Economics — IIT Roorkee `2017–2019`
- B.Sc. Statistics & Mathematics — CSJMU `2014–2017`

</td>
<td valign="top" width="50%">

**Certifications** (Codebasics)
- SQL (Beginner to Advanced)
- Power BI Data Analytics
- Excel: Mother of Business Intelligence

</td>
</tr>
</table>

<br>

<div align="center">

**Open to Tableau Developer and Analytics Engineer roles.** Always happy to talk about Tableau, data modeling, or moving from BI into engineering.
<br>
[LinkedIn](https://linkedin.com/in/guptajaideep) · [Email](mailto:jaideepg.jg@gmail.com)

<br><br>

<img src="https://komarev.com/ghpvc/?username=Jaideepgupta&style=flat-square&color=3ecf8e&label=Profile+Views" alt="Profile views" />

</div>
