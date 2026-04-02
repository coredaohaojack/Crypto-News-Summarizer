# 📰 Crypto News Summarizer

**TL;DR for crypto news, but on-chain and trustless.**

---

### The idea

Every day there are hundreds of crypto articles. Most are noise. A few move markets. This contract figures out what matters.

It's an Intelligent Contract on GenLayer that:
1. 🌐 Reads live market sentiment data
2. 🧠 Uses AI to identify the most likely headline driving the mood
3. 📊 Classifies the market impact
4. 🏷️ Categorizes it
5. ✅ Gets consensus from multiple AI validators

### Example

Call `summarize_news` and get:

```json
{
  "headline": "Market fear hits extreme levels amid macro uncertainty",
  "impact": "VERY_BEARISH",
  "category": "MACRO",
  "summary": "Extreme fear dominates crypto markets. Risk-off sentiment prevails."
}
```

### Impact scale

🔴 VERY_BEARISH → 🟠 BEARISH → 🟡 NEUTRAL → 🟢 BULLISH → 🟢 VERY_BULLISH

### Categories

`REGULATION` · `DEFI` · `EXCHANGE` · `MACRO` · `TECHNOLOGY` · `ADOPTION`

### Get started

[GenLayer Studio](https://studio.genlayer.com/contracts) → paste contract → `param` = `test` → deploy → `summarize_news`

### Stack

GenLayer · Python · GenVM SDK · Optimistic Democracy · *MIT License*
