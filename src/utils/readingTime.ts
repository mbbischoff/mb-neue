/**
 * Calculates the estimated reading time in minutes based on word count.
 * 
 * @param content The content to calculate reading time for
 * @param wordsPerMinute Average reading speed in words per minute (default: 200)
 * @returns Reading time in minutes
 */
export function calculateReadingTime(
  content: string,
  wordsPerMinute: number = 200
): number {
  if (!content) {
    return 1;
  }

  const words = content.trim().split(/\s+/).length;
  return Math.ceil(words / wordsPerMinute);
}

// For backward compatibility
export const readingTime = calculateReadingTime;