import os
import paramiko
import json
import logging
import sys

def read_info_json_file(filename):
    try:
        with open(filename, "r") as jsonfile:
            config_file = json.load(jsonfile)
            logging.info(f"Import of JSON formatted device config file '{filename}' was successful.")
        return config_file
    except Exception as e:  # TODO: obviously way to broad, clean this up
        logging.error(e)
        sys.exit()

def move_files_to_server():
    custom_temp = 'SONiC.yml'
    image_file = 'virtioa.qcow2'
    intel_temp_path = f'/opt/unetlab/html/templates/intel/{custom_temp}'
    amd_temp_path = f'/opt/unetlab/html/templates/amd/{custom_temp}'
    image_file_dir = '/opt/unetlab/addons/qemu/SONiC-4.1.1'
    image_file_path = f'{image_file_dir}/{image_file}'

    # connect to eve-ng server
    ssh = paramiko.SSHClient()
    ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    ssh.connect(server_config['server_ip'], username=server_config['username'], password=server_config['password']) #try except

    # place template into templates directory
    sftp = ssh.open_sftp()
    sftp.put(custom_temp, intel_temp_path)
    sftp.put(custom_temp, amd_temp_path)

    # create directory for image and place image in directory
    sftp.mkdir(image_file_dir)
    sftp.put(image_file, image_file_path)

    # close ssh session
    sftp.close()
    ssh.close()

    print("Transfer Complete")


if __name__ == '__main__':
    server_config = read_info_json_file("config.json")
    move_files_to_server()




