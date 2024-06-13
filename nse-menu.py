import subprocess

def run_nmap(nse_script, target, parameters):
    command = f"nmap --script={nse_script} {parameters} {target}"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        print(f"Error: {error}")
    else:
        print(output)

def main():
    nse_scripts = {
        "vuln": "",
        "auth": "--script-args user=foo,pass=bar",
        # Add more scripts and their parameters here...
    }

    print("Please choose an NSE script:")
    for i, script in enumerate(nse_scripts.keys(), start=1):
        print(f"{i}. {script}")

    choice = int(input("Enter your choice: "))
    target = input("Enter the target: ")

    chosen_script = list(nse_scripts.keys())[choice-1]
    run_nmap(chosen_script, target, nse_scripts[chosen_script])

if __name__ == "__main__":
    main()