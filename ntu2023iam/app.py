from flask import Flask, request, jsonify
import boto3
import json

app = Flask(__name__)

@app.route('/iam/jwt', methods=['POST'])
def get_jwt():
    code = request.json.get('code')
    if not code:
        return jsonify({"error": "Code is required"}), 400

    # 使用 boto3 和授權碼獲取 JWT
    identity_pool_id = 'YOUR_IDENTITY_POOL_ID'
    client = boto3.client('cognito-identity')

    try:
        response = client.get_id(
            IdentityPoolId=identity_pool_id,
            Logins={
                'login.provider': code  # 這裡需要根據您的設定替換正確的 provider 和授權碼
            }
        )
        identity_id = response.get('IdentityId')

        # 獲取認證資訊
        credentials = client.get_credentials_for_identity(
            IdentityId=identity_id,
            Logins={
                'login.provider': code  # 這裡需要根據您的設定替換正確的 provider 和授權碼
            }
        )
        return jsonify(credentials)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
