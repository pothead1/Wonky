Here’s your Design System document for The GanjaGuru in Markdown format:

# Design System - The GanjaGuru

---

## Introduction

The GanjaGuru Design System is a comprehensive set of guidelines, components, and assets aimed at creating a consistent, scalable, and delightful user experience across all platforms. It reflects the brand’s vibe—bold, chill, and futuristic with cannabis-inspired aesthetics.

---

## Foundations

### Colors

| Name            | Hex      | Usage                         |
|-----------------|----------|-------------------------------|
| Emerald Green   | #2ecc71  | Primary actions, highlights    |
| Cannabis Leaf   | #27ae60  | Secondary accents, icons       |
| Earth Brown     | #6e4a1e  | Backgrounds, grounding elements|
| Smoke Gray      | #95a5a6  | Text, borders, subtle UI parts |
| Sunset Orange   | #e67e22  | Warnings, CTAs, attention grabs|
| Midnight Black  | #2c3e50  | Primary text, headers          |
| Cloud White     | #ecf0f1  | Backgrounds, cards             |

---

### Typography

- **Primary:** Montserrat (sans-serif), modern and clean  
- **Secondary:** Futura for headings, bold and geometric  
- **Font Sizes:**  
  - H1: 48px  
  - H2: 36px  
  - H3: 28px  
  - Body: 16px  
- **Weight:** Use 400 for body, 700 for headings  
- **Line Height:** 1.5 for readability  

---

## Layout & Grid

- **Grid:** 12-column responsive grid system  
- **Spacing:**  
  - Margins: 24px (desktop), 16px (mobile)  
  - Padding: 16px standard within containers  
  - Gutters: 16px between columns  
- **Containers:** Max-width 1200px centered on screen  

---

## Components

### Buttons

- **Primary Button**  
  - Background: Emerald Green (#2ecc71)  
  - Text: Cloud White (#ecf0f1)  
  - Border-radius: 8px  
  - Hover: Darker green (#27ae60)  

- **Secondary Button**  
  - Background: Smoke Gray (#95a5a6)  
  - Text: Midnight Black (#2c3e50)  
  - Border-radius: 8px  
  - Hover: Light gray (#bdc3c7)  

---

### Forms

- **Inputs**  
  - Border: 1.5px solid Smoke Gray (#95a5a6)  
  - Focus: Border color Emerald Green (#2ecc71)  
  - Padding: 12px  
  - Border-radius: 6px  

- **Labels**  
  - Font-weight: 600  
  - Color: Midnight Black (#2c3e50)  

---

### Cards

- **Background:** Cloud White (#ecf0f1)  
- **Border-radius:** 12px  
- **Shadow:** Soft shadow with rgba(0,0,0,0.1)  
- **Padding:** 24px  

---

### Icons

- Style: Line art, bold strokes  
- Color: Cannabis Leaf (#27ae60) or Smoke Gray (#95a5a6)  
- Size: 24px standard, scalable  

---

## Motion & Interaction

- Transitions: Ease-in-out, 300ms  
- Floating elements: Subtle oscillation and shadow changes  
- Feedback: Click/tap animations on buttons and cards  
- Voice UI: Pulsing mic button on active listening  

---

## Accessibility

- Contrast ratio: Minimum 4.5:1 for text  
- Keyboard navigation: Full tab support  
- ARIA roles and labels: Applied consistently  
- Motion reduction: User-controlled preferences  

---

## Branding Elements

- Logo variations: Full color, monochrome, icon-only  
- Usage: Clear space rules and minimum sizes  
- Tone of voice: Friendly, chill, knowledgeable  

---

## Versioning & Maintenance

- System version: 1.0  
- Update cadence: Quarterly reviews and updates  
- Contribution guidelines: Documented for design and dev teams  

---

## Resources & Assets

- Sketch and Figma libraries  
- Icon sets and SVGs  
- Color palette files (ASE, SVG)  
- Typography files and licenses  

---

## Example Component Usage

```jsx
<Button variant="primary">Explore Strains</Button>

.button-primary {
  background-color: #2ecc71;
  color: #ecf0f1;
  border-radius: 8px;
  padding: 12px 24px;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  transition: background-color 0.3s ease;
}
.button-primary:hover {
  background-color: #27ae60;
  cursor: pointer;
}

If you want me to export this as a `.md` or bundle with your other docs, just say the word!