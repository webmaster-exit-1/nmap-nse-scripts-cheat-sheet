import subprocess
import re
import typer

app = typer.Typer()

def run_nmap(nse_script: str, target: str, parameters: str):
    command = f"nmap --script={nse_script} {parameters} {target}"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        print(f"Error: {error.decode()}")
    else:
        print(output.decode())  # decode bytes to string

def load_nse_scripts(file_path):
    nse_scripts = {}
    with open(file_path, 'r') as f:
        content = f.read()

    matches = re.findall(r'(.*\.nse)\n\n```bash\n(nmap .+?)\n```', content, re.DOTALL)

    for match in matches:
        script, command = match
        script = script.strip()  # Strip leading/trailing white spaces from script name
        arguments = re.findall(r'<(.*?)>', command)  # Extract arguments from command
        nse_scripts[script] = arguments

    return nse_scripts

@app.command()
def main():
    nse_scripts = load_nse_scripts('cheat-sheet.md')

    print("Please choose an NSE script:")
    for i, script in enumerate(nse_scripts.keys(), start=1):
        print(f"{i}. {script}")

    choice = int(typer.prompt("Enter your choice: "))

    if choice < 1 or choice > len(nse_scripts):
        print("Invalid choice. Please select a number from the list.")
        return

    chosen_script = list(nse_scripts.keys())[choice-1]
    arguments = nse_scripts[chosen_script]

    # Prompt the user for each argument
    arg_values = {}
    for arg in arguments:
        value = typer.prompt(f"Enter the value for {arg}: ")
        arg_values[arg] = value

    # Construct the parameters string
    parameters = ' '.join(f'--script-args {arg}={value}' for arg, value in arg_values.items())

    target = typer.prompt("Enter the target: ")

    run_nmap(chosen_script, target, parameters)

if __name__ == "__main__":
    app()