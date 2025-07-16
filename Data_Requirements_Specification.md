# Data Requirements Specification - The GanjaGuru

---

## 1. Purpose

To define all required data types, sources, structures, and processing standards for the successful development and deployment of GanjaGuru’s AI/ML, AR/VR, personalization, e-commerce, and voice interaction systems.

---

## 2. Scope

This specification applies to all systems within The GanjaGuru ecosystem, including:

- AI Budtender (chatbot, voice, vision, multimodal)
- Cannabis strain and product recommendation engine
- 3DPoD e-commerce platform
- Grow planning and automation tools
- AR/VR-powered exploration and interactions
- User profiles and gamification layers

---

## 3. Data Categories

### A. User Data
| Field                  | Type         | Description                                 | Source         |
|------------------------|--------------|---------------------------------------------|----------------|
| `user_id`             | UUID         | Unique internal identifier                  | App backend    |
| `display_name`        | String       | Alias/nickname                              | User profile   |
| `session_logs`        | JSON         | Interactions with app                       | Frontend logs  |
| `voice_input`         | Audio/Text   | Voice queries, transcriptions               | Microphone     |
| `location`            | Geohash      | Approximate region (compliant & opt-in)     | GPS, IP        |
| `purchase_history`    | JSON         | Itemized orders                             | Commerce API   |
| `journal_entries`     | Text/Image   | Grow logs, medical notes                    | User uploads   |

### B. Product & Strain Data
| Field                   | Type        | Description                                 | Source         |
|-------------------------|-------------|---------------------------------------------|----------------|
| `strain_name`          | String      | Commercial or scientific strain name        | Cannabis DB    |
| `effect_profile`       | List<String>| Uplifted, sleepy, hungry, etc.              | Curated, NLP   |
| `terpenes`             | Dict        | Limonene, Myrcene %, etc.                   | Lab data       |
| `cannabinoid_content` | Dict        | THC, CBD, CBG %, etc.                       | Lab results    |
| `lineage`              | JSON        | Genetic history                             | Grower records |
| `price`                | Float       | Per gram or unit                            | Retail APIs    |
| `availability`         | JSON        | Zip-code availability matrix                | Store data     |

### C. Interaction Data
| Field               | Type      | Description                                | Source           |
|---------------------|-----------|--------------------------------------------|------------------|
| `click_stream`      | JSON      | Timestamps, navigation, dwell time         | Web/App frontend |
| `AR_usage_logs`     | JSON      | Position, zoom, rotation                   | AR SDKs          |
| `voice_query_type`  | Categorical| Informational / Transactional / Guidance  | NLP classifier   |
| `emoji_reactions`   | Enum      | ❤️ 👍 🤯 etc. from community               | Chat frontend    |

---

## 4. Data Sources

- **Internal:** GanjaGuru user logs, admin CMS, purchase system
- **External APIs:** Leafly, Weedmaps, Strain API, Google Maps, FDA/CDC compliance feeds
- **IoT/AR Devices:** AR headsets, environmental sensors, cameras (optional)
- **Open Datasets:** USDA soil and lighting maps, growing conditions, strain libraries
- **User-Generated Content:** Reviews, chats, grow journals, ratings

---

## 5. Data Quality Requirements

| Metric              | Target Value     |
|---------------------|------------------|
| Completeness        | > 98%            |
| Consistency         | > 99%            |
| Latency             | < 300ms (critical) |
| Label Accuracy      | > 95% (training) |
| Duplication Rate    | < 0.5%           |
| Noise Tolerance     | NLP & Vision > 90% clean |
| Accessibility Tags  | 100% where required |

---

## 6. Data Schema Versioning

- All schemas versioned using Semantic Versioning (`vX.Y.Z`)
- Schema changes logged in `/data/schema/changelog.md`
- Major changes require deprecation and migration plan

---

## 7. Privacy, Compliance, and Consent

- **User Data Anonymization:** All AI training uses pseudonymized data
- **Opt-In Voice/AR:** All sensor-based input is opt-in only
- **HIPAA Readiness:** For medical users, aligned with U.S. HIPAA practices
- **GDPR / CCPA:** Compliant user data export, delete, and opt-out flows
- **PII Tags:** All sensitive fields flagged in schema with `pii=true`

---

## 8. Data Lifecycle

| Stage            | Tooling / Storage             |
|------------------|-------------------------------|
| Raw Ingest       | S3, MinIO, Firebase           |
| Preprocessed     | Pandas, Spark, DuckDB         |
| Feature Store    | Feast, Faiss, Redis           |
| Model Input      | Parquet, Torch Datasets       |
| Inference Logs   | MongoDB, BigQuery, InfluxDB   |
| Archived         | Glacier, GCS Coldline         |

---

## 9. Data Annotation Requirements

- **Text Data:** NLP-labeled intent, entity, sentiment (manual + semi-auto)
- **Image Data:** Crop/strain classification, AR object detection
- **Voice Data:** Transcription + emotion tagging
- **Medical/Grow Logs:** Labeled by certified growers, optionally GPT-assisted

---

## 10. Risks and Mitigations

| Risk                             | Mitigation                               |
|----------------------------------|------------------------------------------|
| Data Drift                       | Automated PSI monitoring + alerts       |
| Label Leakage                    | Cross-validation with masking            |
| Privacy Breach                   | End-to-end encryption + access auditing |
| Overfitting to Power Users       | Weighted sampling                        |
| Annotation Bias                  | Multi-label validation                   |

---

## 11. Data Ownership & Governance

- **Data Owners:** ML Lead, Product Owner, UX Research Lead
- **Access Control:** RBAC enforced via IAM policies
- **Auditing:** Daily logs, security alerts, access dashboards
- **Backup Schedule:** Hourly snapshots (critical), daily sync (bulk)

---

## 12. Change Log

| Version | Date       | Change Description                       |
|---------|------------|------------------------------------------|
| 1.0     | 2025-07-16 | Initial specification                    |
| 1.1     | 2025-07-18 | Added AR/IoT data schema & privacy layer |
| 1.2     | TBD        | [Pending additions]                      |

---