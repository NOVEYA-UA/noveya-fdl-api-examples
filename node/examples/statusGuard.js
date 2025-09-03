export class StatusGuard {
  constructor({
    enabled = process.env.STATUS_GUARD === "1",
    windowSec = Number(process.env.STATUS_GUARD_WINDOW || 60),
    tripErrors = Number(process.env.STATUS_GUARD_TRIP || 3)
  } = {}) {
    this.enabled = enabled;
    this.windowSec = windowSec;
    this.tripErrors = tripErrors;
    this.errors = [];
  }
  noteError() {
    const now = Date.now();
    this.errors.push(now);
    this.errors = this.errors.filter(t => now - t <= this.windowSec * 1000);
  }
  degraded() {
    if (!this.enabled) return false;
    if ((process.env.OPENAI_STATUS || "").toLowerCase() === "incident") return true;
    const now = Date.now();
    this.errors = this.errors.filter(t => now - t <= this.windowSec * 1000);
    return this.errors.length >= this.tripErrors;
  }
  suggestOpts() {
    return this.degraded() ? { stream: false, max_output_tokens: 800 } : { stream: true };
  }
}

// === пример использования ===
// import { StatusGuard } from "./statusGuard.mjs";
// const guard = new StatusGuard();
// let opts = guard.suggestOpts();
// try {
//   const resp = await client.responses.create({ model:"gpt-4o", input: prompt, response_format, ...opts });
// } catch (e) {
//   guard.noteError();
//   const resp = await client.responses.create({ model:"gpt-4o", input: prompt, response_format, stream:false });
// }
