# Security runbook

> **Status: ACTION REQUIRED.** Live database credentials were committed to this repo
> (originally in the Django `settings.py` and in `fastapi/user-management/.env`). The
> code now reads secrets from the environment and the working-tree secret has been
> removed, but the credentials still exist in **git history** and must be treated as
> compromised.

## 1. Rotate the leaked credentials (do this first)

The exposed Neon PostgreSQL credentials must be considered public:
- Host: `ep-black-art-a1tqxy0x-pooler.ap-southeast-1.aws.neon.tech`
- User: `neondb_owner`

Steps:
1. In the Neon console, **reset the `neondb_owner` password** (or rotate the role).
2. Rotate the Django `SECRET_KEY` (it was hardcoded):
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key as g; print(g())"
   ```
3. Put new values only in local `.env` files (already gitignored). Never commit them.

## 2. Commit the restructure (removes artifacts from the tree)

The reorganization already moved databases, build output, `helper.txt`, and other
junk **out of the repo** (into `~/Learning/_learning-code-quarantine/`) and relocated
everything into the new folder structure. Stage and commit it all, then remove the
now-empty folders:

```bash
cd learning-code
find . -name .DS_Store -delete
rmdir ai angular database fastapi javascript multi-tenant-architecture \
      program reactjs vuejs django full-stack python
git add -A
git commit -m "chore: restructure repo, remove secrets/artifacts, harden config"
```

## 3. Purge the secrets from git history (the critical step)

Deleting files does not remove them from past commits. Scrub the secret **values**
from all history — robust even though files were moved/renamed. Using
`git filter-repo` (recommended):

```bash
pip install git-filter-repo

cat > /tmp/secrets.txt <<'EOF'
npg_GK1cHmojC9TE==>REDACTED
neondb_owner==>REDACTED
EOF
# add the old Django SECRET_KEY string here too, one per line, as VALUE==>REDACTED

git filter-repo --replace-text /tmp/secrets.txt
git push --force --all      # rewrites remote history
```

**Simplest safe alternative** — start clean history from the fixed tree and archive
the old repo privately:
```bash
rm -rf .git && git init && git add . && git commit -m "Initial clean import"
```

## 4. Apply the Django model change

`Member.phone` changed from `IntegerField` to `CharField`:
```bash
cd projects/django-tennis-club
python manage.py makemigrations members
python manage.py migrate
```

## 5. Verify nothing secret remains

```bash
git grep -nEi "npg_|neondb_owner|django-insecure" $(git rev-list --all) | head
```
Should return nothing once history is purged.

## Going forward
- CI runs **gitleaks** on every push/PR (`.github/workflows/ci.yml`).
- All config comes from environment variables; see the `.env.example` files.
