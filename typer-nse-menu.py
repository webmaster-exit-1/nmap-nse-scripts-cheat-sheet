import subprocess
import re
import typer

app = typer.Typer()

def run_nmap(nse_script: str, target: str, parameters: str):
    command = f"nmap --script={nse_script} {parameters} {target}"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        print(f"Error: {error}")
    else:
        print(output.decode())  # decode bytes to string

def load_nse_scripts(file_path):
    nse_scripts = {}
    with open(file_path, 'r') as f:
        content = f.read()

    # Matches the script name and parameters
    matches = re.findall(r'(.*\.nse)\n\n```bash\n(nmap .+?)\n```', content, re.DOTALL)

    for match in matches:
        script, command = match
        parameters = command.replace('nmap ', '').replace('<target>', '').replace(f'--script {script}', '').strip()
        nse_scripts[script] = parameters  # keep .nse extension

    return nse_scripts

@app.command()
def main():
    nse_scripts = load_nse_scripts('cheat-sheet.md')

    print("Please choose an NSE script:")
    for i, script in enumerate(nse_scripts.keys(), start=1):
        print(f"{i}. {script}")

    choice = int(typer.prompt("Enter your choice: "))
    target = typer.prompt("Enter the target: ")

    chosen_script = list(nse_scripts.keys())[choice-1]
    run_nmap(chosen_script, target, nse_scripts[chosen_script])

if __name__ == "__main__":
    app()
