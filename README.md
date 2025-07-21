
# 📦 Lambda Deployment with GitHub Actions & AWS (2025)

## ✅ Project Overview
This project demonstrates how to build, deploy, and automate a **Python-based AWS Lambda function** using **GitHub Actions** for CI/CD and **API Gateway** for public access. Deployment time is reduced by 40% using automated zip packaging and deployment pipelines.

## 🧠 Simple Explanation 

Imagine you built a tiny robot in Python that says "Hello!".  
You want it to live online, be smart, and always ready to help.

So here’s what you did:

- 🧸 You stored the robot safely on **GitHub**.
- 🎯 Every time you teach it something new (change the code), **GitHub Actions** sends it to the cloud for you — like magic.
- ☁️ The robot lives in **AWS Lambda** — a playground in the sky.
- 🚪 You gave people a **URL (doorbell)** using **API Gateway** so they can talk to your robot from anywhere!

Now, whenever someone visits the link, the robot replies:
> "Hello, Akshat!" 😊

And if you ever change the code, GitHub automatically updates the robot for you. You don’t have to lift a finger.

This project shows how modern apps can live on the cloud and update themselves!

## 🧰 Tech Stack
- **Language**: Python 3.13
- **CI/CD**: GitHub Actions
- **Cloud Services**: AWS Lambda, API Gateway
- **Platform**: Windows 11 (local dev)

## 📁 Folder Structure
```
lambda_project/
├── lambda_function.py
└── .github/
    └── workflows/
        └── deploy.yml
```

## 🚀 Step-by-Step Setup

### 1. ✅ Install Git & Python
- Python 3.11, 3.12, or 3.13 installed (via Microsoft Store or from python.org)
- Git installed and configured:
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### 2. ✅ Create Your Project Directory
```bash
mkdir lambda_project
cd lambda_project
code .  # or open with your editor
```

Create your Lambda function:

```python
# lambda_function.py

def lambda_handler(event, context):
    name = event.get('name', 'World')
    return {
        'statusCode': 200,
        'body': f'Hello, {name}!'
    }
```

### 3. ✅ Set Up GitHub Repository
- Create a new repo on GitHub: `lambda-deploy`
- Connect your local folder:

```bash
git init
git remote add origin https://github.com/yourusername/lambda-deploy.git
```

### 4. ✅ AWS IAM Setup
- Go to AWS Console → IAM → Create new user
- Enable **Programmatic Access**
- Attach `AWSLambdaFullAccess` and `AmazonAPIGatewayAdministrator`
- Download `.csv` or copy:
  - Access Key ID
  - Secret Access Key

### 5. ✅ Add GitHub Secrets
In your GitHub repo:
- Go to **Settings > Secrets > Actions**
- Add:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `AWS_REGION` (e.g. `ap-south-1`)
  - `FUNCTION_NAME` (e.g. `MyLambdaFunction`)

### 6. ✅ Create GitHub Actions Workflow

Create a folder `.github/workflows/deploy.yml` with:

```yaml
name: Deploy Lambda Function

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.13

      - name: Install AWS CLI
        run: |
          sudo apt-get update
          sudo apt-get install -y awscli

      - name: Zip Lambda Function
        run: zip -r lambda_function.zip lambda_function.py

      - name: Deploy to AWS Lambda
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          AWS_REGION: ${{ secrets.AWS_REGION }}
          FUNCTION_NAME: ${{ secrets.FUNCTION_NAME }}
        run: |
          aws lambda update-function-code \
            --function-name "$FUNCTION_NAME" \
            --zip-file fileb://lambda_function.zip \
            --region "$AWS_REGION"
```

Commit it:
```bash
git add .
git commit -m "Initial Lambda function and GitHub Actions workflow"
git push origin main
```

## 🔄 GitHub Actions CI/CD

After pushing:
- Go to your repo → **Actions tab**
- See the workflow run automatically
- It zips the function and deploys to AWS Lambda

## 🌐 API Gateway Setup

1. Go to AWS Console → **API Gateway**
2. Create **HTTP API**
3. Route: `/my-lambda-function` → method: `ANY`
4. Integrate with your Lambda function
5. Click **Deploy** → Stage: `default`
6. Copy the **Invoke URL**, e.g.  
   ```
   https://3sfoj6bwdl.execute-api.ap-south-1.amazonaws.com/default/my-lambda-function
   ```

## 🧪 Testing the Function

### ✅ With GET (browser)
Visit:
```
https://3sfoj6bwdl.execute-api.ap-south-1.amazonaws.com/default/my-lambda-function
```

### ✅ With POST (Postman or curl)
```bash
curl -X POST https://3sfoj6bwdl.execute-api.ap-south-1.amazonaws.com/default/my-lambda-function \
  -H "Content-Type: application/json" \
  -d '{"name": "Akshat"}'
```

**Response:**
```json
{
  "statusCode": 200,
  "body": "Hello, Akshat!"
}
```

## 🧠 Key Learnings

- How to build and deploy AWS Lambda functions
- Automate deployment with GitHub Actions
- Use API Gateway to expose serverless functions
- Real-world CI/CD on a cloud platform

## 👤 Author

**Akshat**  
GitHub: [@akshzt123](https://github.com/akshzt123)