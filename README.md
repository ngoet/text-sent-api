# TextSentiment API
An API for running sentiment analysis on texts, based on FastAPI and TextBlob.

## Testing the endpoints
Endpoints can be tested locally ([test_local](tests/test_local.py)), or directly with your deployed API ([test_integration](tests/test_integration.py)).

### Start Local debugging
To run the local endpoint tests, you first need to start local debugging using the following command:
```bash
uvicorn main:app --reload
```

### Coding standards
This project uses `pre-commit` hooks to reformat non-compliant code and enforce code quality.
For a full list of enabled pre-commit hooks, please consult the [.pre-commit-config.yaml](.pre-commit-config.yaml) file.


### Pull requests/commit policy
All commits and PRs (should) follow the [Conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) commit style.

The project uses [commitizen](https://commitizen-tools.github.io/commitizen/) to enforce this commit style policy throughout.
Commitizen is a command-line interface that allows you to write compliant messages. Use:

```bash
git add <changed files>
cz commit
```

You will get the following prompt, where you'll be able to select the type that best suits the change you are making.

```bash
? Select the type of change you are committing  (Use arrow keys)
 » fix: A bug fix. Correlates with PATCH in SemVer
   feat: A new feature. Correlates with MINOR in SemVer
   docs: Documentation only changes
   style: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-col
   refactor: A code change that neither fixes a bug nor adds a feature
   perf: A code change that improves performance
   test: Adding missing or correcting existing tests
   build: Changes that affect the build system or external dependencies (example scopes: pip, docker, npm)
   ci: Changes to our CI configuration files and scripts (example scopes: GitLabCI)
```

Please use the Commitizen interface for all commits. If you want to remove certain commit messages, please rebase your branch.

### Versioning
The semantic versioning convention is used: `MAJOR.MINOR.PATCH`

A pre-commit ([commitizen](https://commitizen-tools.github.io/commitizen/)) is used to bump the version automatically based on commit history.

Upon merging to the `main` branch, please run the following commands, which will update the version, the Changelog, and make a commit with your changes.
```bash
cz bump --changelog --check-consistency
git push
git push --tags
```


## Deploying with Serverless
Further reading:
* [https://adem.sh/blog/tutorial-fastapi-aws-lambda-serverless](https://adem.sh/blog/tutorial-fastapi-aws-lambda-serverless)
* [https://www.serverless.com](https://www.serverless.com)

The infrastructure is specified in [serverless.yaml](serverless.yaml).

Install serverless with:

```
npm install -g serverless
```

Install the serverless plugins:
```
serverless plugin install -n serverless-python-requirements
serverless plugin install -n serverless-add-api-key
```

Config credentials:
```
serverless config credentials --provider aws --key <YOUR-KEY> --secret <YOUR-SECRET-KEY>
```

Deploy with (make sure Docker is running prior to this step!
Also note that this requires you to have configured the right IAM permissions for the AWS user that you added in the
previous step):

```
sls deploy --aws-profile <YOUR-AWS-PROFILE-NAME> --stage <ENV>
```

Or [deploy a single function](https://www.serverless.com/framework/docs/providers/aws/cli-reference/deploy-function):
```
serverless deploy --aws-profile <YOUR-AWS-PROFILE-NAME> function -f <FUNCTION-NAME>
```

Afterwards, make sure you add permissions to invoke the API on the Lambda Role.
Also make sure that you [whitelist IPs](https://lobster1234.github.io/2018/04/14/amazon-api-gateway-ip-whitelisting/), e.g.:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "execute-api:Invoke",
            "Resource": "<ENDPOINT-ARN>",
            "Condition": {
                "IpAddress": {
                    "aws:SourceIp": [
                        "<MY_IPS>"
                    ]
                }
            }
        }
    ]
}
```

Delete with:

```
sls remove --aws-profile <YOUR-AWS-PROFILE-NAME> --stage <ENV>
```
