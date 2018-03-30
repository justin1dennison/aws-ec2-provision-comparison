import os
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

ec2_access = os.environ.get('AWS_ACCESS') 
ec2_secret = os.environ.get('AWS_SECRET')
image = 'ami-1853ac65'
size = 't2.micro'
Driver = get_driver(Provider.EC2)
conn = Driver(ec2_access, ec2_secret)


def main():
    images = [i for i in conn.list_images() if i.id == image]
    sizes = [s for s in conn.list_sizes() if s.id == size]
    node = conn.create_node(name='Apache Libcloud Sample', 
                            image=images[0], 
                            size=sizes[0])
    print(node)



if __name__ == '__main__':
    main()
