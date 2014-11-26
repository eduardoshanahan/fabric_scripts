import socket
import boto
import boto.ec2
from fabric.api import task


def load():
    """
    Make sure env.ec2 exists and has valid credentials
    """
    if 'aws' not in env:
        env.aws = {}
        if 'credentials' not in env.aws:
            with open('../aws_credentials.json') as credentials:
                env.aws['credentials'] = json.load(credentials)
        if 'ec2' not in env.aws:
            with open('../ec2_details.json') as ec2new:
                env.aws['ec2'] = json.load(ec2new)
    if 'ec2' not in env:
        env.ec2 = {}


@task
def load_region(region_name=''):
    """
    AWS region
    """
    load_ec2()
    if region_name not in env.aws['ec2']['regions']:
        region_name = env.aws['ec2']['defaults']['region']
        print ('Region unknown, selecting default')
    env.ec2['region_name'] = region_name
    env.ec2['region'] = env.aws['ec2']['regions'][region_name]
    print('Region selected: {0} - {1}'.format(env.ec2['region_name'],
                                              env.ec2['region']))


@task
def connect(region_name=''):
    """
    Create a connection to AWS
    """
    load_ec2()
    if 'region' not in env.ec2:
        load_ec2_region(region_name)

    print('Access Key {0}'.format(
        env.aws['credentials']['aws_access_key_id']))
    print('Secret Access Key {0}'.format(
        env.aws['credentials']['aws_secret_access_key']))

    env.ec2['connection'] = boto.ec2.connect_to_region(
        env.ec2['region'],
        aws_access_key_id=env.aws['credentials']['aws_access_key_id'],
        aws_secret_access_key=env.aws['credentials'][
            'aws_secret_access_key'])

    if env.ec2['connection'] is None:
        raise Exception(
            'Cannot connect to AWS region {0} using {1} and {2} '
            .format(env.ec2.region_name, env.ec2.aws_access_key_id,
                    env.ec2.aws_secret_access_key))

    print('Connection {0}'.format(env.ec2['connection']))


@task
def load_ami_name(image_name='', region_name=''):
    """
    Select an image available to the region
    """
    load_ec2()
    if 'region' not in env.ec2:
        load_ec2_region(region_name)
    region_name = env.ec2['region_name']
    if image_name not in env.aws['ec2']['images'][region_name]:
        image_name = env.aws['ec2']['defaults']['imageName']
        print ('Image unknown, selecting default')
    env.ec2['ami_name'] = env.aws['ec2']['images'][region_name][
        image_name]
    print('Image selected: {0}'.format(image_name))
    print ('AMI selected: {0}'.format(env.ec2['ami_name']))


@task
def load_ec2_image(image_name='', region_name=''):
    """
    Grab an image from AWS
    """
    load_ec2()
    if 'connection' not in env.ec2:
        connect_ec2(region_name)
    if 'ami_name' not in env.ec2:
        load_ec2_ami_name(image_name, region_name)
    print(env.ec2['connection'])
    env.ec2['image'] = env.ec2['connection'].get_image(
        env.ec2['ami_name'])
    print('Image selected: {0}'.format(env.ec2['image']))


@task
def load_ec2_instance_type(instance_type=''):
    """
    Select instance type for EC2
    """
    load_ec2()
    if instance_type not in env.aws['ec2']['instanceTypes']:
        instance_type = env.aws['ec2']['defaults']['instanceType']
        print ('Instance type unknown, selecting default')
    env.ec2['instance_type'] = instance_type
    print ('Instance type selected: {0}'.format(instance_type))


@task
def ensure_key_name(key_name=''):
    """
    Grab a key from AWS
    """
    load_ec2()
    if env.key_filename is None:
        if key_name == '':
            key_name = env.aws['ec2']['defaults']['key_name']
            print ('Key name unspecified, selecting default')
        env.ec2['key_name'] = key_name
    else:
        key_filename = env.key_filename[0]
        filename = os.path.basename(key_filename)
        keyname = os.path.splitext(filename)[0]
        env.ec2['key_name'] = keyname


@task
def ensure_ec2_key(key_name='', region_name=''):
    """
    Create a key in AWS and store it locally
    """
    load_ec2()
    if 'key' not in env.ec2:
        if 'connection' not in env.ec2:
            connect_ec2(region_name)
        ensure_key_name(key_name)
        key = env.ec2['connection'].get_key_pair(env.ec2['key_name'])
        if key is None:
            key = env.ec2['connection'].create_key_pair(
                env.ec2['key_name'])
            save_key_pairs_local(key, env.ec2['region_name'])
        else:
            print ('Key already exists')
        env.ec2['key'] = key

    key_filename = get_local_key_filename_from_ec2()
    print('Key filename is {0}'.format(key_filename))


def get_local_key_filename_from_ec2():
    working_directory = os.getcwd()
    keys_directory = os.path.join(working_directory, 'synchResources',
                                  'Keys', env.ec2['region_name'])
    key_filename = os.path.join(keys_directory,
                                env.ec2['key'].name + '.pem')
    return key_filename


def save_key_pairs_local(key_pair, region_name):
    """
    Keep a copy of the key
    """
    working_directory = os.getcwd()
    keys_directory = os.path.join(working_directory, 'synchResources',
                                  'Keys', region_name)
    save_key_pair_on_disk(key_pair, keys_directory)


def save_key_pair_on_disk(key_pair, directory):
    """
    Drop the key in disk
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    key_pair.save(directory)


@task
def load_ec2_security_groups(security_groups_name='', region_name=''):
    """
    Select the security_groups for EC2
    """
    load_ec2()
    if security_groups_name not in env.aws['ec2']['securityGroups']:
        security_groups_name = env.aws['ec2']['defaults'][
            'securityGroupsName']
        print ('Security groups unknown, selecting default')

    env.ec2['security_groups'] = env.aws['ec2']['securityGroups'][
        security_groups_name]
    print (
        'Security groups selected: {0} - {1}'.format(
            security_groups_name,
            env.ec2[
                'security_groups']))

    if 'connection' not in env.ec2:
        connect_ec2(region_name)

    existing_groups_names = [x.name.encode('utf-8') for x in env.ec2[
        'connection'].get_all_security_groups()]
    print (
        'Existing group names are {0}'.format(existing_groups_names))

    missing_groups_names = [x for x in env.ec2['security_groups'] if
                            x not in existing_groups_names]

    if len(missing_groups_names) > 0:
        print (
            'Groups {0} are not in AWS, will be created empty'.format(
                missing_groups_names))
        description = 'Empty group created as part of deployment'
        create_group = (
            lambda g: env.ec2['connection']
            .create_security_group(g, description))
        [create_group(x) for x in missing_groups_names]


@task
def load_ec2_block_device_map(disk_size=''):
    """
    Get a block device map with a given disk size
    """
    load_ec2()
    if disk_size not in env.aws['ec2']['diskSizes']:
        disk_size = env.aws['ec2']['defaults']['diskSize']
        print ('Disk size unknown, selecting default')

    dev_sda1 = boto.ec2.blockdevicemapping.EBSBlockDeviceType()
    dev_sda1.size = disk_size
    bdm = boto.ec2.blockdevicemapping.BlockDeviceMapping()
    bdm['/dev/sda1'] = dev_sda1

    env.ec2['block_device_map'] = bdm
    print ('Disk size selected: {0}'.format(disk_size))


@task
def get_reservation(image_name='', instance_type='', key_name='',
                    security_groups_name='', region_name='',
                    disk_size=''):
    """
    Grab an instance to run
    """
    load_ec2()
    if 'reservation' not in env.ec2:
        if 'image' not in env.ec2:
            load_ec2_image(image_name, region_name)
        if 'instance_type' not in env.ec2:
            load_ec2_instance_type(instance_type)
        if 'key' not in env.ec2:
            ensure_ec2_key(key_name)
        if 'security_groups' not in env.ec2:
            load_ec2_security_groups(security_groups_name,
                                     region_name)
        if 'disk_size' not in env.ec2:
            load_ec2_block_device_map(disk_size)
        env.ec2['reservation'] = env.ec2['image'].run(
            instance_type=env.ec2['instance_type'],
            key_name=env.ec2['key_name'],
            security_groups=env.ec2['security_groups'],
            block_device_map=env.ec2['block_device_map'])
    print ('Reservation is {0}'.format(env.ec2['reservation']))


@task
def create_ec2_instance(machine_name='', image_name='',
                        instance_type='', key_name='',
                        security_groups_name='', region_name='',
                        disk_size=''):
    """
    Fire a server
    """
    load_ec2()
    if 'reservation' not in env.ec2:
        get_reservation(image_name, instance_type, key_name,
                        security_groups_name, region_name, disk_size)
    if machine_name == '':
        machine_name = env.aws['ec2']['defaults']['machineName']
    env.ec2['instance'] = env.ec2['reservation'].instances[0]
    env.ec2['connection'].create_tags([env.ec2['instance'].id],
                                      {'Name': machine_name})
    print ('Waiting for the instance to be ready...')
    while env.ec2['instance'].state != u'running':
        time.sleep(5)
        env.ec2['instance'].update()
    print ('Public address {0} - {1} at {2} with key {3}'.format(
        env.ec2['instance'].ip_address,
        env.ec2['instance'].public_dns_name, env.ec2['region_name'],
        env.ec2['key'].name))

    remaining_attempts = 20

    while remaining_attempts > 0:
        try:
            check_ssh(env.ec2['instance'].public_dns_name)
            remaining_attempts = 0
        except Exception:
            remaining_attempts -= 1

    print ('Server ready to fly and accessible by port 22')


def check_ssh(hostname, port_number=22):
    """
    Try to connect to ssh port
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        remaining_attempts = 30

        while remaining_attempts > 0:
            try:
                s.connect((hostname, port_number))
                print ('Port {0} reachable'.format(port_number))
                remaining_attempts = 0
            except Exception:
                remaining_attempts -= 1
                time.sleep(6)
    except socket.error as e:
        print 'Error on connect: {0}'.format(e)
    s.close()


@task
def create_ec2_deploy_fresh_server(machine_name='', image_name='',
                                   instance_type='', key_name='',
                                   security_groups_name='',
                                   region_name='', disk_size=''):
    """
    USE FOR EC2 - Make an instance in EC2
    and have it ready to deploy code
    """
    create_ec2_instance(machine_name, image_name, instance_type,
                        key_name, security_groups_name, region_name,
                        disk_size)
    env.user = 'ubuntu'
    env.hosts = [env.ec2['instance'].public_dns_name.encode('utf-8')]
    env.key_filename = [
        get_local_key_filename_from_ec2().encode('utf-8')]
    time.sleep(60)
    print ('Machine created, trying to identify')
    remaining_attempts = 20

    worked = False
    while remaining_attempts > 0:
        try:
            time.sleep(6)
            execute(identify_os)
            remaining_attempts = 0
            worked = True
        except Exception:
            remaining_attempts -= 1
            print('Bombed, {0} more attempts to try'.format(
                remaining_attempts))

    if worked:
        execute('server_update')
