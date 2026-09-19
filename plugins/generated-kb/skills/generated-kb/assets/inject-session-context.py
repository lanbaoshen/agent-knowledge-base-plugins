import html
import json
import re
from pathlib import Path

knowledge_root = Path.cwd() / "knowledge-base"
frontmatter_pattern = re.compile(
    r"\A---[ \t]*\r?\n(.*?)^---[ \t]*\r?\n", re.DOTALL | re.MULTILINE
)


def parse_frontmatter(raw_frontmatter):
    metadata = {}
    for line in raw_frontmatter.splitlines():
        if ":" not in line or line[:1] in (" ", "\t") or line.lstrip().startswith(("#", "-")):
            continue
        key, value = map(str.strip, line.split(":", 1))
        value = value.strip('"')
        if key and value:
            metadata[key] = value
    return metadata


def xml_name(name):
    safe_name = re.sub(r"[^A-Za-z0-9_.-]", "_", name)
    return safe_name if re.match(r"[A-Za-z_]", safe_name) else "_" + safe_name


def xml_element(name, value):
    name = xml_name(name)
    return f"<{name}>{html.escape(str(value), quote=False)}</{name}>"


def knowledge_base_context():
    nodes = []
    total_file_size = 0
    for path in sorted(knowledge_root.rglob("*.md")):
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        total_file_size += path.stat().st_size
        match = frontmatter_pattern.match(content)
        metadata = parse_frontmatter(match.group(1)) if match else {}
        fields = [xml_element("file", path)]
        fields.extend(xml_element(field, value) for field, value in metadata.items())
        nodes.append("<knowledge>" + "".join(fields) + "</knowledge>")

    instructions = (
        "This catalog lists repository-specific knowledge for a recurring task. "
        "Read the repository-local knowledge skill before selecting and reading relevant documents. "
        "Each entry contains only a document path and frontmatter metadata; read relevant document "
        "bodies before relying on them and ignore unrelated entries.\n\n"
        "Available knowledge:\n"
    )
    context = f"<knowledge-base>{instructions}{''.join(nodes)}</knowledge-base>"
    return context, len(nodes), total_file_size


knowledge_context, knowledge_count, total_file_size = knowledge_base_context()
injected_character_count = len(knowledge_context)
estimated_token_count = (injected_character_count + 3) // 4
total_file_size_mb = total_file_size / (1024 * 1024)
system_message = (
    f"Knowledge injected from {knowledge_root}: {knowledge_count} file entries. {total_file_size_mb:.2f} MB total.\n"
    f"Injected context: {injected_character_count} characters, approximately {estimated_token_count} tokens."
)

print(
    json.dumps(
        {
            "systemMessage": system_message,
            "hookSpecificOutput": {"additionalContext": knowledge_context},
            "additionalContext": knowledge_context,
        }
    )
)
