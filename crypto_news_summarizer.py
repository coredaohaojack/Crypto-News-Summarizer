# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

import json
import typing


class CryptoNewsSummarizer(gl.Contract):
    has_scanned: bool
    headline: str
    impact: str
    analysis: str
    param: str

    def __init__(self, param: str):
        self.has_scanned = False
        self.headline = "none"
        self.impact = "NEUTRAL"
        self.analysis = "Awaiting scan"
        self.param = param

    @gl.public.write
    def summarize_news(self) -> typing.Any:

        if self.has_scanned:
            return "Already scanned"

        def nondet() -> str:
            fng = gl.nondet.web.render("https://alternative.me/crypto/fear-and-greed-index/", mode="text")
            print(fng)

            task = f"""You are a crypto news analyst. Based on market data, identify the most likely top headline driving sentiment.
            Here is current crypto market data:
            {fng[:1500]}

            Respond with the following JSON format:
            {{
                "headline": str,
                "impact": str,
                "category": str,
                "summary": str
            }}
            headline: the most likely important crypto headline today.
            impact: one of VERY_BEARISH, BEARISH, NEUTRAL, BULLISH, VERY_BULLISH.
            category: one of REGULATION, DEFI, EXCHANGE, MACRO, TECHNOLOGY, ADOPTION.
            summary: two sentence news summary.
            It is mandatory that you respond only using the JSON format above,
            nothing else. Don't include any other words or characters,
            your output must be only JSON without any formatting prefix or suffix.
            This result should be perfectly parsable by a JSON parser without errors.
            """
            result = gl.nondet.exec_prompt(task).replace("```json", "").replace("```", "")
            print(result)
            return json.dumps(json.loads(result), sort_keys=True)

        result_json = json.loads(gl.eq_principle.strict_eq(nondet))

        self.has_scanned = True
        self.headline = result_json["headline"]
        self.impact = result_json["impact"]
        self.analysis = result_json["summary"]

        return result_json
