import pronto
from pathlib import Path

INPUT_OBO  = r"C:\Users\Dell\OneDrive - Hanoi University of Mining and Geology\Tai_lieu_cong_viec\Personas\persona_analysis_2.obo"
OUTPUT_HTML = r"C:\Users\Dell\OneDrive - Hanoi University of Mining and Geology\Tai_lieu_cong_viec\Personas\persona_analysis_2.html"

onto = pronto.Ontology(INPUT_OBO)

terms = []
for term in onto.terms():
    superclasses = [
        {"id": s.id, "name": s.name}
        for s in term.superclasses(distance=1)
        if s.id != term.id
    ]
    rels = {}
    for rel, targets in term.relationships.items():
        rels[rel.name] = [{"id": t.id, "name": t.name} for t in targets]

    terms.append({
        "id": term.id,
        "name": term.name or "",
        "definition": str(term.definition) if term.definition else "",
        "superclasses": superclasses,
        "relationships": rels,
    })

# terms.sort(key=lambda t: t["id"])

html_parts = ["""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>Persona Ontology Documentation</title>
<style>
  body {
      font-family: Arial, sans-serif;
      margin: 0;
  }

#sidebar {
    position: fixed;
    left: 0;
    top: 0;
    width: 320px;
    height: 100vh;
    background: #f0f0f0;
    padding: 16px;
    box-sizing: border-box;
    overflow-y: auto;
    overflow-x: hidden; 
}

  #sidebar h2 {
      font-size: 14px;
      margin-bottom: 8px;
  }

  #sidebar a {
      display: block;
      font-size: 12px;
      color: #0066cc;
      text-decoration: none;
      padding: 2px 0;
  }

  #sidebar a:hover {
      text-decoration: underline;
  }

  input#search {
      width: 100%;
      padding: 6px;
      margin-bottom: 10px;
      box-sizing: border-box;
      font-size: 13px;
  }

  #content {
      margin-left: 300px;
      padding: 24px;
      box-sizing: border-box;
  }

  .term {
      border: 1px solid #ddd;
      border-radius: 6px;
      padding: 16px;
      margin-bottom: 20px;
  }

  .term h2 {
      margin: 0 0 4px;
      font-size: 18px;
  }

  .term-id {
      color: #888;
      font-size: 13px;
      margin-bottom: 10px;
  }

  .label {
      font-weight: bold;
      color: #444;
  }

  .rel-tag {
      display: inline-block;
      background: #e0f0ff;
      border-radius: 4px;
      padding: 2px 8px;
      margin: 2px;
      font-size: 13px;
  }
</style>
</head>
<body>

<div id="sidebar">
  <h2>Persona Ontology</h2>
  <input id="search"
         placeholder="Tìm term..."
         oninput="filterSidebar(this.value)">
  <div id="sidebar-links">
"""]

for t in terms:
    html_parts.append(
        f'    <a href="#{t["id"]}" class="slink">'
        f'{t["id"]}: {t["name"]}</a>\n'
    )

html_parts.append("  </div>\n</div>\n<div id=\"content\">\n")

for t in terms:
    html_parts.append(f'<div class="term" id="{t["id"]}">\n')
    html_parts.append(f'  <h2>{t["name"]}</h2>\n')
    html_parts.append(f'  <div class="term-id">{t["id"]}</div>\n')
    if t["definition"]:
        html_parts.append(
            f'  <p><span class="label">Định nghĩa:</span> {t["definition"]}</p>\n'
        )
    if t["superclasses"]:
        links = ", ".join(
            f'<a href="#{s["id"]}">{s["name"] or s["id"]}</a>'
            for s in t["superclasses"]
        )
        html_parts.append(
            f'  <p><span class="label">is_a:</span> {links}</p>\n'
        )
    for rel_name, targets in t["relationships"].items():
        links = " ".join(
            f'<span class="rel-tag">'
            f'<a href="#{tg["id"]}">{tg["name"] or tg["id"]}</a></span>'
            for tg in targets
        )
        html_parts.append(
            f'  <p><span class="label">{rel_name}:</span> {links}</p>\n'
        )
    html_parts.append("</div>\n")

html_parts.append("""</div>
<script>
function filterSidebar(q) {
  q = q.toLowerCase();
  document.querySelectorAll('.slink').forEach(a => {
    a.style.display = a.textContent.toLowerCase().includes(q) ? 'block' : 'none';
  });
}
</script>
</body></html>""")

Path(OUTPUT_HTML).write_text("".join(html_parts), encoding="utf-8")
print(f"Done! Mở file: {OUTPUT_HTML}")