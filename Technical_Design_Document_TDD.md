# Technical Design Document (TDD) - The GanjaGuru

**Owner:** Lead Architect  
**Version:** 1.0  
**Last Updated:** 2025-07-16  
**Purpose:** This document defines the system architecture, component relationships, APIs, data flow, and technical decisions that bring the Product Requirements Document (PRD) to life for The GanjaGuru platform.

---

## 1. System Overview

The GanjaGuru is a multimodal, AI-powered cannabis assistant featuring:

- Anti-gravity floating UI/UX  
- Voice-activated strain recommendations  
- AR/VR exploration and 3DPoD commerce  
- Personalized data-driven journeys  
- Fully offline/online capability with lightweight deployment  

---

## 2. System Components

### Frontend

| Technology | Purpose |
|------------|---------|
| **HTML5 + CSS3** | Core semantic layout and styling |
| **JavaScript** | Interactivity, app logic |
| **WebGL / Three.js** | Anti-gravity visual effects, floating portals |
| **AR.js** | Marker-based and markerless AR product preview |
| **TensorFlow.js** | On-device ML for personalization and inference |
| **Vosk SDK (WebAssembly)** | Offline voice command processing |

---

### Backend

| Technology | Role |
|------------|------|
| **Node.js + Express.js** | API gateway, auth, session handling |
| **Python (Flask or FastAPI)** | ML model serving, strain recommendation engine |
| **WebSockets** | Real-time voice and AR data streaming |
| **FFmpeg (optional)** | Audio/video pre-processing for voice features |

---

### LLM / NLP Engine

| Feature | Details |
|--------|---------|
| **Model Base** | Replit-code-v1-3b |
| **Custom Training** | Cannabis-specific intents, product embeddings |
| **Components** | Tokenizer, RAG, context memory, prompt generator |
| **Execution** | Local or via GPU API on Hugging Face or Modal Labs |

---

### Database & Caching

| DB Type | Use Case |
|--------|-----------|
| **MongoDB (NoSQL)** | User profiles, sessions, strain data, logs |
| **Redis** | Session caching, gamification counters, voice intent cache |
| **DuckDB (optional)** | In-browser OLAP-style query processing |

---

### 3DPoD & AR/VR Modules

| Module | Stack |
|--------|-------|
| **3DPoD Viewer** | Babylon.js + custom WebGL pipeline |
| **Printify API** | Real-time catalog sync and PoD fulfillment |
| **Portal Nav** | Canvas rendering + DOM portals |
| **Voice Shop Assist** | Voice input triggers PoD and strain previews |
| **AR Previews** | AR.js with WebXR compatibility |

---

### Hosting / Deployment

| Platform | Purpose |
|----------|---------|
| **Netlify/Vercel** | Frontend CI/CD, CDN edge deployment |
| **S3-Compatible Storage** | AR assets, image uploads, journals |
| **Render / Railway / Modal** | Python microservices, model APIs |
| **Service Worker + PWA** | Offline-ready, push notifications, app shell |

---

## 3. Key API Interfaces

### `/api/strain/recommend`
- **Method:** POST  
- **Payload:** `{ "intent": "relax", "context": { user_id, location, preferences } }`  
- **Returns:** Ranked strain list, AR preview links

### `/api/chat`
- **Method:** POST  
- **Payload:** `{ "message": "What strain helps with migraines?" }`  
- **Returns:** LLM-generated advice with inline links and voice-ready payload

### `/api/ar/init`
- **Method:** GET  
- **Returns:** List of AR-ready assets (markers, products, 3DPoD previews)

---

## 4. Voice Interaction Pipeline

1. **Voice capture:** Mic input using WebRTC → WAV/OGG  
2. **Transcription:** Vosk → WebAssembly  
3. **NLU Parsing:** Custom tokenizer → intent extractor (Replit-based)  
4. **Response Gen:** Dynamic LLM call or rules engine  
5. **Output:** Spoken response via TTS or chatbot UI  

---

## 5. Data Flow Architecture

```plaintext
[User] --> [Voice / Text Input] --> [Frontend JS Engine]
       --> [API Gateway (Node.js)] --> [NLU Pipeline (Python)]
       --> [MongoDB + Redis] --> [ML Model or AR Service]
       --> [Response] --> [Floating UI + AR Viewer + Voice Output]