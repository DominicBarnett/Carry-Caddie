# Carry-Caddie
 
Carry Caddie is an application where a User can enter the carry yardages of a given golf club to store for later reference. The User can also compare those yardages with that of the average pga tour pro

CSS Styling Updates Summary
This README provides an overview of the CSS changes made for the web project, detailing adjustments to layout, typography, form elements, buttons, and general styling for improved visual design and consistency.

1. Global Styles
Font & Color Scheme: The primary font used is Open Sans with a color scheme based on oklch for better color readability and contrast.
Background: The page has a light background color, with the main content and form sections using subtle background shades for better legibility and focus.
2. Background Styling
Fixed Background: A fixed background image (CourseCollage.webp) is set to cover the full viewport, with a slight darkening effect (brightness(0.7)) to ensure that text remains readable.
3. Main Content Styling
Content Box: The main content box is styled with a maximum width of 800px and a light tan background. It is centered on the page and has a large box shadow to provide a prominent and clean look.
4. Typography Changes
Headings (h1, h2):
Removed the bottom margin of h1 and h2 elements for tighter spacing between the headings and subsequent elements.
Paragraphs (p):
Margin: Removed the margin on all paragraphs for tighter vertical alignment.
Line Height: Added a line-height of 1.6 for better readability and text flow.
Spacing for Last Paragraph: The last paragraph in a group has a bottom margin of 20px to separate it from following elements (e.g., buttons).
5. Button Styles
Unified Button Styling: The styling of #begin-button and input[type=submit] has been standardized:
Background color of a bright green (oklch(45% 0.25 140)).
Font size: 1.2em for consistency.
Padding of 10px 20px and border-radius of 5px.
Hover effect: Background color turns into a more vibrant yellow on hover (oklch(90% 0.2 95)).
Both buttons now share the same look, creating a consistent user interface throughout the project.
6. Form and Fieldset Styling
Fieldsets:
Fieldsets have a subtle border with a light background color (oklch(98% 0.01 95)).
The text within the fieldsets has dark color (oklch(15% 0.02 80)) for readability.
Legend Styling: The legend text inside fieldsets is bold and slightly larger (1.2em), ensuring it stands out.
7. Store Section Styling
Item Cards:
Cards are now less transparent (rgba(255, 255, 255, 0.85)), making the background less see-through while still allowing some transparency for depth.
Hover effect: A smooth scaling transformation (transform: scale(1.05)) for a more interactive feel.
8. Table Styling
Table:
The table now has a more prominent box shadow to make it stand out from the rest of the content.
Table cells (th, td) have consistent padding and a subtle border with alternating background colors for headers and data cells.
9. Responsive Design Adjustments
On smaller screens (max-width: 768px), layout adjustments include:
Main Content: The width is reduced to 95% with adjusted padding for better fit.
Navigation Bar: Flexbox direction switches to column mode, aligning items at the center for better mobile display.
Store Section: Item display is adjusted to center items within the available width.
10. General Aesthetic Enhancements
Color Adjustments: The use of oklch color space helps ensure better contrast ratios for readability and accessibility.
Hover Transitions: Buttons, links, and interactive elements have smooth hover transitions for a modern, dynamic feel.
Summary of Key Design Improvements:
Unified and consistent button styling.
Improved typography and spacing for readability.
Subtle background adjustments for better content legibility.
Enhancements for mobile responsiveness, ensuring a good user experience across devices.
These updates have improved the visual appearance, consistency, and user interaction of the website, providing a more polished and functional design.
