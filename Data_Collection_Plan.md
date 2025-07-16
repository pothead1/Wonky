# Data Collection Plan - The GanjaGuru

---

## 1. Purpose

This document outlines the comprehensive strategy for collecting, validating, and managing data for The GanjaGuru AI platform. The plan ensures alignment with platform goals: hyper-personalized cannabis discovery, smart e-commerce, AR/VR experiences, grow coaching, and AI-powered assistance—while maintaining compliance, quality, and user trust.

---

## 2. Data Categories & Objectives

| Data Category        | Purpose                                                           |
|----------------------|-------------------------------------------------------------------|
| Strain Metadata      | Fuel recommendations, search, effects filtering                   |
| Product Catalog      | Power e-commerce, 3DPoD previews, AR gear matching                |
| User Profiles        | Drive personalization, safety guidance, loyalty tracking          |
| Grow Logs            | Enhance AI coaching, build user grow archives                     |
| Voice Interaction    | Train & tune voice AI assistant (Budtender)                       |
| Community Content    | Support reviews, social loops, training of moderation models      |
| App Usage Analytics  | UX tuning, model feedback loops, personalization intelligence     |
| Sensor/AR Input      | Enable immersive grow room tools, real-world context              |

---

## 3. Collection Methods

### A. API Integrations
- **Vendors / Distributors:** Pull inventory, pricing, product metadata  
- **Strain Databases:** Sync from licensed repositories (e.g., Leafly API)  
- **Legal Authorities:** Import state-level compliance data for medical use

### B. User Input
- **Signup / Onboarding:** Consent-driven profile intake  
- **Budtender Queries:** Voice and typed prompts stored (optional opt-in)  
- **Grow Journal Entries:** Photos, notes, schedule data (structured + unstructured)  
- **Reviews / Comments:** Markdown + rich media enabled

### C. Automated Sensors
- **AR Grow Tools:** User camera + LiDAR (where available) to collect spatial data  
- **App Device Sensors:** (with consent) - light exposure, temp readings, time-on-task

### D. In-App Behavior
- **Clickstream Logging:** Navigation paths, button taps, time-on-page  
- **Feature Usage:** Tracks voice search, AR previews, smart filters  
- **Voice & Text Logs:** Used for NLU training (de-identified)

### E. Community Contributions
- **Strain Additions:** Form-based strain submission with admin review  
- **User-Uploaded 3D Models:** For PoD or AR/VR environments  
- **Grow Forum Posts:** Indexed for social graph & language patterns

---

## 4. Data Sources & Formats

| Source                      | Format                  | Frequency        |
|-----------------------------|-------------------------|------------------|
| Leafly / Weedmaps APIs      | JSON / XML              | Daily            |
| Vendor Product Catalogs     | CSV / JSON              | 4–6 hour sync    |
| User Profile Intake         | Encrypted JSON          | Real-time        |
| Voice Assistant             | Audio → Text + Embedding| Real-time        |
| Grow Photos / Logs          | JPG/PNG + Markdown      | On event         |
| Sensor Data (AR, WebXR)     | WebXR JSON + glTF       | Real-time        |
| Community Forums            | Markdown + Media        | Continuous       |

---

## 5. Consent & Ethical Handling

- **User Consent Flow:**  
  - Mandatory opt-in for medical tracking, camera/mic use, AR  
  - Granular controls for data categories  
  - Clear "Download My Data" and "Delete My Data" options

- **Anonymization Pipeline:**  
  - Logs & interactions pseudonymized  
  - Biometric/AR sensor data removed from training sets  
  - All de-identified logs timestamped and token-masked

- **Compliance Certifications:**  
  - GDPR, CCPA, HIPAA (for medical-tagged data)  
  - WCAG 2.1 AA for ARIA labels and voice capture

---

## 6. Validation & Cleaning

- Schema validation on all JSON/XML  
- Mandatory fields: strain ID, product ID, user UUID  
- Terpene/Effect tags verified via NLP autoclassifier  
- Duplicates flagged by hash-based detection  
- Image quality filter (blur/redaction detection)

---

## 7. Storage & Access

- **Strain/Product Data:** MongoDB (NoSQL), Redis for fast filters  
- **User Profiles / Logs:** PostgreSQL, encrypted columns  
- **Images / 3D Assets:** AWS S3 / IPFS for distributed access  
- **Voice/Chat Logs:** Time-series DB + TensorStore (vector logs)  
- **Data Lake (Training/Analytics):** BigQuery / DuckDB / Delta Lake

---

## 8. Collection Frequency Summary

| Data Type            | Method             | Frequency         |
|----------------------|--------------------|-------------------|
| Strain Metadata      | API / Manual       | Daily             |
| Product Inventory    | Vendor API         | 4–6 hours         |
| User Inputs          | App Input          | Real-time         |
| Grow Logs            | User Upload        | As entered        |
| Voice Interactions   | Assistant Session  | Per utterance     |
| 3D/AR Interactions   | WebXR Feed         | Session-based     |
| Forum Content        | Markdown Posts     | On submission     |
| Model Feedback       | Chat Logs          | Passive tracking  |

---

## 9. Tooling & Instrumentation

- **Airbyte** / **Fivetran** – ETL ingestion from external APIs  
- **DBT** – Transformations and schema validation  
- **Amplitude / PostHog** – In-app behavior analytics  
- **Label Studio** – Manual annotation and training data review  
- **Kibana / Grafana** – Real-time log visualization

---

## 10. Future Collection Enhancements

- Eye-tracking (via AR device integration)  
- Thermal/humidity sensors for smart grow environments  
- NFT/Wallet-based identity layers for personalization  
- Passive biometric feedback integration (privacy-aware)

---