# Feature Engineering Plan - The GanjaGuru

---

## 1. Overview

This plan outlines the strategic approach for designing, constructing, and optimizing machine learning features across The GanjaGuru ecosystem—including recommendation engines, voice interfaces, grow assistants, AR/VR modules, and cannabis e-commerce personalization.

---

## 2. Objectives

- Convert raw cannabis data into actionable ML features
- Enhance personalization and prediction accuracy
- Support multimodal input: text, voice, AR, user behavior
- Enable explainable, ethical, and compliant ML pipelines

---

## 3. Data Sources

- Strain metadata (effects, lineage, terpenes)
- Product catalog (SKUs, categories, pricing, formats)
- User interaction logs (queries, ratings, purchases)
- Grow journal entries (text, images, timestamps)
- Voice and text logs from AI assistant
- AR/VR usage data (device orientation, context tags)
- Community content (reviews, comments, upvotes)
- Environmental context (geolocation, time of day, light level)

---

## 4. Feature Categories

### A. User-Level Features
- `user_profile_embedding` – vector from profile traits
- `avg_session_time`
- `strain_affinity_vector` – multi-hot encoding + weights
- `voice_interaction_count`
- `preferred_effects` – derived from behavior + NLP

### B. Product/Strain-Level Features
- `terpene_vector` – one-hot + PCA-reduced
- `strain_popularity_score` – based on engagement
- `price_bucket` – low, med, high
- `availability_zone_index`
- `AR_interaction_score` – based on frequency & duration

### C. Contextual Features
- `device_type` – mobile, desktop, AR headset
- `local_time_bucket` – morning, afternoon, night
- `ambient_light_index` – from sensor (if consented)
- `geo_region_tag` – encoded for local compliance filtering
- `user_sentiment_score` – from NLP classifier

### D. Grower-Specific Features
- `grow_stage_tag` – seedling, veg, flower, harvest
- `journal_entry_vector` – text embedding (SBERT)
- `photo_quality_score` – blur detection / lighting index
- `task_adherence_score` – from task log timestamps

---

## 5. Engineering Techniques

- **One-Hot Encoding** – for terpene classes, strain types
- **TF-IDF / Embeddings** – for user queries, grow logs
- **Label Encoding** – for categorical location/device tags
- **Bucketization** – price, session length, effects scale
- **Dimensionality Reduction** – PCA / UMAP for terpene + effect vectors
- **Rolling Aggregates** – for time-series session logs
- **Vector Fusion** – combining embeddings across modalities
- **Time-Based Features** – hour-of-day, weekday, lunar phase (for growers)
- **Interaction Scoring** – AR usage intensity, chat frequency, voice queries

---

## 6. Tools & Pipelines

- **Scikit-learn** – preprocessing, scaling, transformations
- **spaCy / SBERT / HuggingFace** – text embeddings
- **OpenCV / PIL** – photo metadata extraction
- **NumPy / Pandas** – vector ops and dataset structuring
- **Featuretools** – for automated feature synthesis
- **MLflow / DVC** – version control for feature sets

---

## 7. Feature Storage & Retrieval

- **Online Features:** Redis + Faiss for real-time recommendations  
- **Offline Features:** Stored in DuckDB / Parquet in data lake  
- **Training Pipelines:** Orchestrated via Airflow  
- **Inference Serving:** TensorFlow Serving / FastAPI + Faiss hybrid

---

## 8. Governance

- **Feature Registry:** Centralized with metadata, versioning, owners
- **Explainability Mapping:** Every feature tagged with “human-meaningful” label
- **Privacy Tags:** Features flagged if tied to user PII
- **Bias Audits:** Features scored by fairness filter pipeline
- **Retention Policies:** Usage logs auto-purged after 90 days (user config)

---

## 9. Experimental / Future Features

- `eye_tracking_engagement` – from AR headset integrations
- `mood_vector` – emotion classification from voice input
- `NFT_profile_traits` – derived from wallet-linked strain badges
- `group_recommendation_contexts` – session-level shared filtering
- `cannabinoid_diffusion_score` – used in grow prediction AI

---

## 10. Feature Quality Metrics

| Metric                    | Target Threshold   |
|---------------------------|--------------------|
| Null Ratio                | < 2%               |
| Feature Drift (PSI)       | < 0.1              |
| Variance Contribution     | > 0.2 (for PCA)    |
| Correlation Redundancy    | < 0.85             |
| Predictive Importance     | Above 5% threshold |
| Explainability Score      | 80%+ features labeled human-meaningful |
| Bias Score (Δ across groups) | < 10% difference   |

---

## 11. Collaboration Protocols

- All feature requests logged in JIRA under “ML:Feature” tags  
- Changes require PRs to shared `feature_defs.yaml` repo  
- Features linked to specific model experiments via MLflow runs  
- Weekly feature review with AI/UX/Data teams

---