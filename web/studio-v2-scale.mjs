/* Coordinates are relative to the top of the measured 583 px audio strip. */
export const meterMarks = [
  [10, 394], [6, 408], [0, 424], [-6, 441], [-12, 456],
  [-24, 474], [-36, 490], [-48, 503], [-72, 513],
];

const meterStops = [[12, 380], ...meterMarks, [-84, 522]];
const faderStops = [[12, 394], [6, 408], [0, 423], [-6, 441], [-12, 456],
  [-24, 474], [-36, 490], [-60, 503]];

function interpolate(value, points, axis) {
  const output = 1 - axis;
  if (value <= points[0][axis]) return points[0][output];
  for (let i = 1; i < points.length; i++) {
    const lower = points[i - 1];
    const upper = points[i];
    if (value <= upper[axis]) {
      const fraction = (value - lower[axis]) / (upper[axis] - lower[axis]);
      return lower[output] + fraction * (upper[output] - lower[output]);
    }
  }
  return points.at(-1)[output];
}

const ascendingMeter = [...meterStops].reverse();
const ascendingFader = [...faderStops].reverse();
export const faderResolution = 10000;
export const meterFraction = db => (522 - interpolate(db, ascendingMeter, 0)) / 142;
export const faderPosition = db => Math.round((503 - interpolate(db, ascendingFader, 0)) / 109 * faderResolution);
export const faderGain = position => {
  const y = 503 - position / faderResolution * 109;
  return Math.round(interpolate(y, faderStops, 1) * 10) / 10 || 0;
};
