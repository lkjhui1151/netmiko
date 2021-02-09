from paramiko import SSHClient, AutoAddPolicy
from time import sleep
from re import match


def get_output(session):
    return session.recv(65535).decode('utf-8').rstrip()


def find_prompt(output):
    last_line = output.splitlines()[-1].strip()
    if match(r'([\w-]+)(>|(?:\(config.*\))*#)', last_line):
        return True
    return False


def send_command(session, command):
    cmd_output = ''
    session.send(command + '\n')
    sleep(0.3)
    while True:
        _output = get_output(session)
        cmd_output += _output
        if find_prompt(_output):
            break
    return cmd_output


def main(output ):
    output = ''
    with SSHClient() as client:
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(
            hostname='10.1.1.10',
            username='admin',
            password='admin',
            look_for_keys=False
        )
        session = client.invoke_shell()
        _output = get_output(session)
        output += _output
        if find_prompt(_output):
            cmd_output = send_command(session, 'show running-config  | include hostname')
            output += cmd_output
            cmd_output = send_command(session, 'show running-config')
            output += cmd_output
            print(output.strip())
            u = print(output.strip())


def save_file():
    file = open('txt.txt', "w")
    for i in main():
        file.write(i)
        file.write("\n")
    file.close()


if __name__ == '__main__':
    main()
    save_file()
