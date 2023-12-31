# Plotly dashboard template
A template repository for creating data dashboards with Plotly.

**This is a template, and should not be overwritten.** There are instructions below on how to set up your own development repository.

## Getting started

### Creating a copy of the template

1. Choose a name for the repository to house your code. Please note this name should conform to [snake case (e.g. example_data_dashboard)](https://betterprogramming.pub/string-case-styles-camel-pascal-snake-and-kebab-case-981407998841) to avoid annoying errors later!
1. Create a new repository to house your dashboard from this template, instructions can be found [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template). **Do not overwrite this template repository.** 

### Configuring GitHub policies
By default, GitHub  does not apply any branch protection policies to newly created repositories. We use these policies to enforce things like: Requiring pull requests to commit changes into the main branch, requiring any comments on pull requests to be resolved and requiring status checks to pass before pull requests can be merged.

1. Open the Settings menu for your GitHub repository ***(Your user needs to be assigned the Admin role to see this option. If it's missing contact your GitHub owner for permission)***

    ![Settings](images/policies/menu_bar.png)

1. Click the Add branch protection rule button
    
    ![Add protection rules](images/policies/unset_branch_protections.png)

1. Set the options in the below screenshot
    
    ![Branch Policy](images/policies/branch_policy.png)


### Installation
## Getting Started

### Set up your local development environment (DLUHC set up - others may vary)
**Note: This section only needs completing once**
1.  Set your default browser to Google Chrome - [instructions][Make Chrome your default browser].
1.  Open Anaconda Navigator via Start menu. **Note:** Anaconda asks if you want to update it, but it won't work.
1.  Install and launch VS Code (Visual Studio Code) from within the Anaconda Navigator. **Note** after installing VS Code, a Getting Started walkthrough is shown. Click the back button to escape.
1.  Navigate to the `Git CMD` from the start menu and execute the below commands. Once you have executed the commands close `Git CMD`.

    **Note: You need to change the name/email to match your own and you need to include the quotation marks. You may like to copy the commands into a word document to edit them.**

```shell
git config --global user.name "Your Name"
git config --global user.email "Your.Name@levellingup.gov.uk"
``` 

[Make Chrome your default browser]: https://support.google.com/chrome/answer/95417?hl=en-GB&co=GENIE.Platform%3DDesktop

### Downloading the code from GitHub

1.  Create a folder on your desktop, for storing source code within if you don't have one already.
1.  From VS Code open the [Explorer window][explorer_window], the overlapping pages icon on left hand menu. Select the option to "Clone Repository". Click "Clone from GitHub"
1.  If prompted, authorize with GitHub.
1.  You should be prompted to enter a repository name. Type "communitiesuk/&lt;Your repository name&gt;". Then click on communitiesuk/&lt;Your repository name&gt;.
1.  As a destination, select your folder for storing the source code. Select "Sign in with browser" if the GitHub authorisation popup is shown.
1.  This pulls the code from GitHub to your local folder.
    Click "Open folder" option, and navigate to your newly created folder containing the repository code.
1.  Select "Yes, I trust the authors".

[explorer_window]: https://code.visualstudio.com/docs/getstarted/userinterface#_explorer

### Installing packages

1.  [Open a command prompt terminal within VS Code][open-terminal], in which you'll start executing some commands. By default, the initial terminal will be a powershell terminal, and you will need to [switch to a command prompt shell][terminal-switch]. 
1.  Update the name field in environment.yml to the dashboard name
1.  Create a new conda environment by typing `conda env create -f environment.yml` into the terminal and executing the command by pressing the Enter key.
1.  Activate your conda environment with `conda activate <dashboard name> `
1. Close VS Code. Open Anaconda Navigator, select "&lt; Dashboard name &gt;" for the 'Application on' drop down menu, then select "Launch" VS Code. Click the bin icon on the terminal toolbar to close the terminal. Click the plus icon on the terminal toolbar to launch a new terminal.
1.  Install the [Microsoft Python][python_extension] extension for VS Code.
1.  Follow the [instructions for configuring the Python interpreter][configure_python_interpreter].


[open-terminal]: https://code.visualstudio.com/docs/editor/integrated-terminal
[terminal-switch]: https://code.visualstudio.com/docs/editor/integrated-terminal#_terminal-shells
[python_extension]: https://marketplace.visualstudio.com/items?itemName=ms-python.python
[configure_python_interpreter]: https://code.visualstudio.com/docs/python/python-tutorial#_select-a-python-interpreter

### Configuring GitHub triggers

1. Navigate to `check-before-merging.yml` in the workflows folder
1. Uncomment the GitHub triggers for the Automated checks
1. Update the application-name environment variable to the application name, which should match the value set in the dashboard.

### Setting environment variables
1. From VS Code, open the `.env` file. If this file does not exist, then create it at the root of the project. The `.env` file is excluded from git commits, so can contain secrets such as AWS Access keys as they will only be present on an individual developer laptop
1. Inside the `.env file`, add the new environment variable in the format `ENVIRONMENT_VARIABLE=VALUE`. An example is `STAGE="production"`. There is a file called `.env.example` that be used for reference


### Running the application
1.  From your VS Code terminal, execute `python run.py`
1.  Wait for the message "Dash is running on ..." message to appear
1.  Navigate to http://localhost:8080/ in your browser within the AWS workspace. Note that http://localhost:8080/ is the address that dash will run on in your local machine.
1. Use Ctrl-C in the terminal to quit the python server. 

    **Note:** Terminal can only handle one command at a time, if the python server is running the terminal will not handle any further commands. To restart the server use `python run.py`



## Customisation 

### Adding figure to dashboard
1.  Create figure function for specific chart type and save in figure folder on dashboard file
1.  Set a variable equal to the figure function and pass in the necessary parameters
1.  In order to return a graph, set a new variable and pass in dcc.Graph(with the id of your new figure)
```
barchart = bar_chart(df, "Category", "Value", color="Category")
barchart_dash = dcc.Graph(id="example bar chart", responsive=True, figure=barchart)
dashboard_content = [card(barchart_dash)]
```

## Deploying to Gov PaaS
1. Log in to Gov UK PaaS through Cloud Foundry, enter the email address and password registered with Gov PaaS
```bash
cf login
```
2. Create an organisation and space within Gov PaaS. Add users to the space within Gov PaaS with correct permissions [Managing organisation and spaces](https://docs.cloud.service.gov.uk/orgs_spaces_users.html#managing-organisations-spaces-and-users)

Create a space using:
```bash
cf create-space SPACE -o ORGNAME
```
where SPACE is the name of the space, and ORGNAME is the name of the org

3. Once the space has been created, you will need to target that space using:
```bash
cf target -s <SPACE NAME>
```
4. Push the application to the space using:
```bash
cf push <APP_NAME> --no-route
```
5. Create a route for your application using:
```bash
cf create-route <DOMAIN> --hostname <HOSTNAME>
```
6. Once you have created your route, the route will need to be mapped to your application using:
```bash
cf map-route <APP_NAME> <DOMAIN> --hostname <HOSTNAME>
```
7. Update required fields in `.github/workflows/deployment.yml` indicated by &lt;&gt; and a comment. 
8. Set up dedicated accounts - do not use your normal GOV.UK PaaS credentials whilst deploying with GitHub actions.
    Find out more about [configuring your CI tool accounts](https://docs.cloud.service.gov.uk/using_ci.html#configure-your-ci-tool-accounts) in GOV.UK PaaS.
9. [Store the newly created credentials in GitHub Actions][store_creds] - You should store your sensitive credentials in GitHub Actions. 
    Store the username with secret name `GOV_PAAS_USER` and the password with secret name `GOV_PAAS_PASS`.

## OPTIONAL: Create a shared username/password for accessing the hosted dashboard
This can be useful if you want to prevent curious individuals from accessing your dashboard while in development, but does not give any security against malicious actors.

GOV.UK PaaS provide guidance on how to do this under the title [Example: Route service to add username and password authentication][basic_auth], you will need to have access to the `cf` command installed and configured, which can be requested through DAP support. However following the GOV.UK PaaS method you cannot have both basic authentication and IP restricitons in place as your app can only have one routing service. If you would like your app to have basic authentication and IP restrictions, please follow the below steps to add basic authentication using flask:

1. In your GitHub repository, add environment secrets for `APP_USERNAME` and `APP_PASSWORD`
1. In `deployment.yml` under the `deploy-staging` job, for the task `Set environment variables` add the below to the run command:
    ```python 
    cf set-env ${{ env.application-name }} APP_USERNAME ${{ secrets.APP_USERNAME }}
    cf set-env ${{ env.application-name }} APP_PASSWORD ${{ secrets.APP_PASSWORD }}
    ```
1. In 'app.py' add:
    ```python
    from gov_uk_dashboards.lib.enable_basic_auth import enable_basic_auth

    enable_basic_auth(app)
    ```

**Note:** to update basic authentication credentials, update the `APP_USERNAME` and `APP_PASSWORD` secrets in GitHub and re-deploy your app.

More information on secrets can be found [here](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

[store_creds]: https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository
[basic_auth]: https://docs.cloud.service.gov.uk/deploying_services/route_services/#example-route-service-to-add-username-and-password-authentication


## Development

### Running tests

Writing and running automated tests ensures software is correct, reduces risk that users will experience bugs, and allows developers to move much faster as they can make changes with confidence that any breaks will be caught be the test suite. Once you have set up unit tests:

```bash
python -u -m pytest tests
```

### Running the code formatter

The [code formatter](https://black.readthedocs.io/en/stable/) ensures source code is formatted consistently. Running the code formatter makes changes automatically that then need to be committed.

```bash
black ./
```

### Running the linter

The linter checks for basic logic errors and bugs. Linting reports rule violations that must be corrected manually.  

```bash
pylint <Dashboard name>
```