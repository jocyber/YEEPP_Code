echo "Committing to repository."
echo ""

git add ./*

read -p "Commit message: " message
git commit -m "$message"

git push origin main

echo "End of commit."
