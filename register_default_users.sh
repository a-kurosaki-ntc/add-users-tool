REGISTER_SCRIPT_PATH="./register_user.py"

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 USERS_FILE_PATH"
    exit 1
fi

USERS_FILE_PATH="$1"

while IFS=' ' read -r email is_admin
do
    echo $email $is_admin
    python3 $REGISTER_SCRIPT_PATH $email $is_admin
done < $USERS_FILE_PATH
