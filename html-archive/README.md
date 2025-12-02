# HTML Archive

This folder contains a minimal static site ready to be archived.

Files:
- `index.html` — Home page
- `about.html` — About / secondary page
- `styles.css` — Shared stylesheet
- `make-archive.ps1` — PowerShell script to create `html-archive.zip`

How to create the ZIP archive (PowerShell):

Open PowerShell, change directory into `html-archive`, then run:

```powershell
.\make-archive.ps1
```

Or run the single command from the parent folder:

```powershell
Compress-Archive -Path .\html-archive\* -DestinationPath .\html-archive.zip -Force
```

The produced file will be `html-archive.zip` in the parent folder.