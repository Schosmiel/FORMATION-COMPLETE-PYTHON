from pathlib import Path

# Dictionnaire des extensions et de leurs dossiers correspondants
dirs = {
    '.txt': 'TextFiles',
    '.pdf': 'Documents',
    '.jpg': 'Images',
    '.mp3': 'Musique',
    '.mp4': 'Videos',
    '.zip': 'Archives',
    '.jpeg': 'Images',
    '.json': 'JSON',
    '.doc': 'Documents',
    '.docx': 'Documents',
    '.csv': 'Excel',
    '.wav': 'Musique',
    '.avi': 'Videos',
    '.mov': 'Videos',
    '.gif': 'Images',
    '.ppt': 'Presentations',
    '.pptx': 'Presentations',
}

tri_dir = Path.home() / "Tri"
print(tri_dir)
files = [f for f in tri_dir.iterdir() if f.is_file()]
for f in files:
    print(f.name)
    output_dir = tri_dir / dirs.get(f.suffix, "Autres")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)
