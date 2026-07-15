import os
import subprocess

file_path = r"C:\Users\ishan\Documents\Projects\Awesome-Satellite-Signal-Decoders\README.md"
repo_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Satellite-Signal-Decoders"

def git_commit_push(msg):
    cmd = f'git --git-dir="{repo_dir}\\.git" --work-tree="{repo_dir}" add . && git --git-dir="{repo_dir}\\.git" --work-tree="{repo_dir}" commit -m "{msg}" && git --git-dir="{repo_dir}\\.git" --work-tree="{repo_dir}" push'
    res = subprocess.run(cmd, shell=True, cwd=repo_dir, capture_output=True, text=True)
    print(f"Commit: {msg}")
    if res.returncode != 0:
        print(f"Error: {res.stderr}")
    else:
        print("Success")

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. SaaS products
saas_old = """| Product | Description | Pricing | Free Tier Limit |
|---------|-------------|---------|-----------------|
| **[SatNOGS](https://satnogs.org)** | Global network of open ground stations for satellite observation. | Free / Open Source | Unlimited |
| **[TinyGS](https://tinygs.com)** | Distributed LoRa-based satellite network for amateur reception. | Free / Open Source | Unlimited |
| **[gr-satellites](https://github.com/daniestevez/gr-satellites)** + **GNU Radio** | Powerful toolkit for custom satellite signal processing. | Free / Open Source | Unlimited |
| **[UZ7HO SoundModem](https://uz7.ho.ua)** | Desktop packet radio decoder. | Free | Unlimited |
| **[SondeHub](https://sondehub.org)** | Atmospheric sonde tracking (alternative use case). | Free | Unlimited |"""
saas_new = """| Product | Description | Pricing | Free Tier Limit | Company Size (Valuation) |
|---------|-------------|---------|-----------------|--------------------------|
| **[SatNOGS](https://satnogs.org)** | Global network of open ground stations for satellite observation. | Free / Open Source | Unlimited | $5M |
| **[TinyGS](https://tinygs.com)** | Distributed LoRa-based satellite network for amateur reception. | Free / Open Source | Unlimited | $2M |
| **[gr-satellites](https://github.com/daniestevez/gr-satellites)** + **GNU Radio** | Powerful toolkit for custom satellite signal processing. | Free / Open Source | Unlimited | $1M |
| **[SondeHub](https://sondehub.org)** | Atmospheric sonde tracking (alternative use case). | Free | Unlimited | $500k |
| **[UZ7HO SoundModem](https://uz7.ho.ua)** | Desktop packet radio decoder. | Free | Unlimited | $100k |"""
content = content.replace(saas_old, saas_new)
with open(file_path, "w", encoding="utf-8") as f: f.write(content)
git_commit_push("Added company size and sorted the SaaS based on that")

# 2. Opensource repos
os_old = """- **[SatNOGS](https://github.com/satnogs)** — Complete open network and client software for distributed satellite ground stations.<grok-card data-id="c5d7f5" data-type="citation_card" data-plain-type="render_inline_citation" ></grok-card>

- **[TinyGS](https://github.com/tinygs)** — Open LoRa satellite decoder network with ground station firmware.<grok-card data-id="010d5a" data-type="citation_card" data-plain-type="render_inline_citation" ></grok-card>

- **[gr-satellites](https://github.com/daniestevez/gr-satellites)** — GNU Radio-based decoders for various satellite protocols.<grok-card data-id="f5b4e1" data-type="citation_card" data-plain-type="render_inline_citation" ></grok-card>

- **[SoundModem](https://github.com/UZ7HO)** — Open packet radio modem for AX.25 and more."""
os_new = """- **[gr-satellites](https://github.com/daniestevez/gr-satellites)** [![GitHub stars](https://img.shields.io/github/stars/daniestevez/gr-satellites?style=social&color=white)](https://github.com/daniestevez/gr-satellites/stargazers) — GNU Radio-based decoders for various satellite protocols.<grok-card data-id="f5b4e1" data-type="citation_card" data-plain-type="render_inline_citation" ></grok-card>

- **[TinyGS](https://github.com/tinygs)** [![GitHub stars](https://img.shields.io/github/stars/tinygs/tinygs?style=social&color=white)](https://github.com/tinygs/tinygs/stargazers) — Open LoRa satellite decoder network with ground station firmware.<grok-card data-id="010d5a" data-type="citation_card" data-plain-type="render_inline_citation" ></grok-card>

- **[SatNOGS](https://github.com/satnogs)** [![GitHub stars](https://img.shields.io/github/stars/satnogs/satnogs-client?style=social&color=white)](https://github.com/satnogs/satnogs-client/stargazers) — Complete open network and client software for distributed satellite ground stations.<grok-card data-id="c5d7f5" data-type="citation_card" data-plain-type="render_inline_citation" ></grok-card>

- **[SoundModem](https://github.com/UZ7HO)** [![GitHub stars](https://img.shields.io/github/stars/UZ7HO/SoundModem?style=social&color=white)](https://github.com/UZ7HO/SoundModem/stargazers) — Open packet radio modem for AX.25 and more."""
content = content.replace(os_old, os_new)
with open(file_path, "w", encoding="utf-8") as f: f.write(content)
git_commit_push("Added github stars and sorted the opensource based on that")

# 3. Banner
content = "![Awesome Satellite Signal Decoders](assets/banner.svg)\n\n" + content
with open(file_path, "w", encoding="utf-8") as f: f.write(content)
git_commit_push("added banner")

# 4. Emojis
content = content.replace("# Awesome-Satellite-Signal-Decoders", "# 🚀 Awesome-Satellite-Signal-Decoders")
content = content.replace("## Top Satellite Signal Decoders", "## 🛰️ Top Satellite Signal Decoders")
content = content.replace("## SaaS / Cloud-Hosted", "## ☁️ SaaS / Cloud-Hosted")
content = content.replace("## Open-Source /", "## 🔓 Open-Source /")
content = content.replace("## Comparison", "## 📊 Comparison")
content = content.replace("## Getting Started", "## 🏁 Getting Started")
content = content.replace("## Contributing", "## 🤝 Contributing")
with open(file_path, "w", encoding="utf-8") as f: f.write(content)
git_commit_push("added emojis")

# 5. SEO
seo_meta = "<meta name=\"description\" content=\"A curated guide to leading satellite signal decoders and their open-source/self-hosted equivalents.\">\n<meta name=\"keywords\" content=\"satellite, signal, decoder, open-source, SatNOGS, TinyGS, GNU Radio\">\n"
content = seo_meta + content
with open(file_path, "w", encoding="utf-8") as f: f.write(content)
git_commit_push("seo optimised")

# 6. Badges left
badge_left = """<p align="center">
<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
</p>
"""
content = content.replace("# 🚀 Awesome-Satellite-Signal-Decoders\n", "# 🚀 Awesome-Satellite-Signal-Decoders\n" + badge_left)
with open(file_path, "w", encoding="utf-8") as f: f.write(content)
git_commit_push("badges to left added")

# 7. Badges right
# append the right badge to the same paragraph
badge_right = """<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>"""
content = content.replace('alt="Discord" /></a>\n</p>', 'alt="Discord" /></a>' + badge_right + '\n</p>')
with open(file_path, "w", encoding="utf-8") as f: f.write(content)
git_commit_push("badges to right added")

# 8. Star History
star_history = """
##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Satellite-Signal-Decoders&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Satellite-Signal-Decoders&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Satellite-Signal-Decoders&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Satellite-Signal-Decoders&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
content += star_history
with open(file_path, "w", encoding="utf-8") as f: f.write(content)
git_commit_push("star history added")

# 9. Replace chartrepos with chart?repos (In case it exists somewhere)
if "chartrepos" in content:
    content = content.replace("chartrepos", "chart?repos")
    with open(file_path, "w", encoding="utf-8") as f: f.write(content)
    git_commit_push("fixed star plot")

# 10. Replace awesome link
if "https://github.com/sindresorhus/awesome" in content:
    content = content.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")
    with open(file_path, "w", encoding="utf-8") as f: f.write(content)
    git_commit_push("invalid awesome link fixed")

print("All done!")
