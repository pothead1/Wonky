Here’s the UI Style Guide document for The GanjaGuru in Markdown format:

# UI Style Guide - The GanjaGuru

---

## Brand Colors

| Name            | Hex      | Usage                         |
|-----------------|----------|-------------------------------|
| Emerald Green   | #2ecc71  | Primary buttons, accents      |
| Cannabis Leaf   | #27ae60  | Highlights, icons             |
| Earth Brown     | #6e4a1e  | Backgrounds, footers          |
| Smoke Gray      | #95a5a6  | Text, secondary UI elements   |
| Sunset Orange   | #e67e22  | Call-to-action, alerts        |
| Midnight Black  | #2c3e50  | Headers, typography           |
| Cloud White     | #ecf0f1  | Backgrounds, cards            |

---

## Typography

- **Primary Font:** Montserrat (sans-serif)  
- **Secondary Font:** Futura (for headings)  
- **Body Font Size:** 16px  
- **Heading Sizes:**  
  - H1: 48px bold  
  - H2: 36px semi-bold  
  - H3: 28px medium  
- **Line Height:** 1.5  
- **Letter Spacing:** 0.5px  

---

## Buttons

- **Primary Button**  
  - Background: Emerald Green (#2ecc71)  
  - Text: Cloud White (#ecf0f1)  
  - Border Radius: 8px  
  - Hover: Darker green (#27ae60)  

- **Secondary Button**  
  - Background: Smoke Gray (#95a5a6)  
  - Text: Midnight Black (#2c3e50)  
  - Border Radius: 8px  
  - Hover: Lighter gray (#bdc3c7)  

---

## Icons & Graphics

- Style: Line art with bold strokes  
- Color: Use Cannabis Leaf green or Smoke Gray  
- Size: Standard 24px for UI elements  
- Animation: Subtle hover scaling and color shifts  

---

## Layout & Spacing

- Grid: 12-column responsive grid  
- Margins: 24px outer margins on desktop  
- Padding: 16px within cards and modules  
- Spacing between sections: 48px  
- Floating Elements: Use soft shadows and slight blur for depth  

---

## Imagery

- Style: Vibrant, natural, and lifestyle-focused  
- Use AR/VR rendered product visuals where possible  
- Avoid stock photography unless heavily edited  

---

## Accessibility

- Contrast ratio: Minimum 4.5:1 for text  
- Focus states: Clear outlines and color shifts  
- Keyboard navigation: Full support on all interactive elements  
- ARIA labels: Applied consistently for screen readers  

---

## Motion & Animation

- Use gentle ease-in-out transitions (300ms)  
- Floating UI elements to have slow, subtle oscillation  
- Feedback animations for button clicks and form submissions  
- Avoid motion sickness triggers; allow user control to reduce motion  

---

## Voice UI

- Microphone button: Prominent, circular, cannabis leaf icon  
- Active listening state: Pulsing green ring  
- Error feedback: Soft orange alert with sound  

---

## Example Component

```jsx
<button class="primary-btn">
  Explore Strains
</button>

.primary-btn {
  background-color: #2ecc71;
  color: #ecf0f1;
  border-radius: 8px;
  padding: 12px 24px;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  font-size: 16px;
  transition: background-color 0.3s ease;
}
.primary-btn:hover {
  background-color: #27ae60;
  cursor: pointer;
}

If you want this as a downloadable `.md` or integrated with your style assets, just holler!