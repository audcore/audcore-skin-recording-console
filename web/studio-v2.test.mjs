import test from "node:test";
import assert from "node:assert/strict";


import { faderGain, faderPosition, faderResolution, meterFraction, meterMarks } from "./studio-v2-scale.mjs";



test("Studio V2 projects the actual dB values onto the measured meter and fader", () => {
  assert.equal(meterFraction(12), 1);
  assert.equal(meterFraction(-84), 0);
  for (const [db, y] of meterMarks) assert.ok(Math.abs(522 - meterFraction(db) * 142 - y) < 1e-9);
  assert.ok(Math.abs(503 - 109 * faderPosition(0) / faderResolution - 423) < .01);
  for (let tenth = -600; tenth <= 120; tenth++) {
    const db = tenth / 10;
    assert.equal(faderGain(faderPosition(db)), db);
  }
});
