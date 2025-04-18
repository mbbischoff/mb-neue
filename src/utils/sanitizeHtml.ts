/**
 * Sanitizes HTML content by removing HTML tags
 * 
 * @param html The HTML string to sanitize
 * @returns Sanitized text without HTML tags
 */
export function sanitizeHtml(html: string): string {
  if (!html) return '';
  
  // Remove any content that looks like HTML, including incomplete tags
  return html.replace(/<[^>]*/g, '');
}