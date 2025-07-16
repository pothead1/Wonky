# Component Library Documentation - The GanjaGuru

---

## Overview

This document outlines the standardized, reusable UI components for The GanjaGuru platform. Each component follows accessibility best practices, is styled according to the brand design system, and supports both dark and light modes.

---

## 1. Buttons

### Variants:
- **Primary Button**  
- **Secondary Button**  
- **Icon Button**  
- **Ghost Button**  
- **Voice Command Button**

### States:
- Default  
- Hover  
- Focus  
- Disabled  
- Loading

### Props:
- `label` (string)  
- `onClick` (function)  
- `variant` (enum)  
- `disabled` (boolean)  
- `icon` (component, optional)

---

## 2. Inputs

### Types:
- Text Field  
- Search Bar  
- Number Input  
- Date Picker  
- File Upload  
- Voice Input Field

### States:
- Active  
- Focused  
- Error  
- Disabled

### Features:
- Clearable input  
- Accessible labels & aria support  
- Auto-complete support  
- Voice recording feedback

---

## 3. Modals

### Use Cases:
- Product Detail Popups  
- AI Recommendations  
- Checkout Confirmations

### Props:
- `title`  
- `content`  
- `isOpen`  
- `onClose`

### Accessibility:
- Focus trap  
- Escape key to close  
- Announced via screen reader

---

## 4. Cards

### Variants:
- **Strain Card** (image, rating, effects, price)  
- **Accessory Card**  
- **Blog Post Card**  
- **User Profile Card**

### Props:
- `image`  
- `title`  
- `description`  
- `cta`  
- `rating`  
- `tags`

---

## 5. Navigation

### Components:
- **Top Navigation Bar**  
- **Bottom Tab Navigation (Mobile)**  
- **Floating Orbital Menu (AR/VR)**  
- **Sidebar (Dashboard)**

### Features:
- Keyboard and voice navigable  
- Sticky and responsive  
- Deep-link support

---

## 6. Voice Interaction UI

### Components:
- Microphone Button  
- Voice Feedback Bubbles  
- Live Transcription Box  
- Command History Tray

### Features:
- Start/stop listening  
- Visual waveform animation  
- NLP contextual feedback

---

## 7. Product Gallery

### Features:
- Horizontal/vertical scroll  
- Zoom-in on hover  
- AR preview trigger  
- 3DPoD carousel for customization

---

## 8. Notifications

### Types:
- Toasts (success, error, info)  
- Push notifications  
- In-app banners  
- Gamified rewards popups

### Props:
- `type`  
- `message`  
- `timeout`  
- `action` (optional)

---

## 9. Forms

### Form Patterns:
- Checkout  
- Profile Setup  
- Grow Log Submission  
- Budtender Consult Intake

### Features:
- Progressive steps  
- Real-time validation  
- Voice input enabled  
- ARIA support for all inputs

---

## 10. Custom Elements

### Floating UI Islands
- Anti-gravity section containers  
- Modular, draggable on desktop  
- Snap-to-grid system for accessibility

### Portal Elements
- Used for navigation between experience layers  
- Trigger AR scenes or immersive zones  
- Voice-activated

---

## Theming & Responsiveness

- Components respond to breakpoints: `xs`, `sm`, `md`, `lg`, `xl`  
- Full support for dark mode / light mode  
- Custom themes per user profile (e.g., Medical, Recreational, Grower)

---

## Developer Integration

- **Framework:** React (modular)  
- **Styling:** TailwindCSS + custom tokens  
- **Theming:** CSS variables and context providers  
- **Accessibility:** WCAG 2.1 AA compliant  
- **Testing:** Storybook, Jest, Axe-core

---

## Asset Repository

- Icons (SVG & Font-based)  
- Animations (Lottie JSON)  
- 3D Models (GLB for AR/VR components)  
- Audio (Feedback tones, voice prompt FX)

---

## Versioning & Contribution

- Version: `v1.0.0`  
- Repo: [internal link or GitHub]  
- Contribution guide: See `CONTRIBUTING.md`  
- Changelog: See `CHANGELOG.md`

---