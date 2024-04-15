# from openstack import connection
#
# conn = connection.Connection(auth_url = "http://<your-identity-url>/identity/v3"
# project_name = "<your-project-name>"
# username = "<your-username>"
# password = "<your-password>"
# user_domain_id = "default"
# project_domain_id = "default")
#
# instance_name = 'my-instance-2'
# image_id = '5c5bd489-da21-4c88-8916-54e4504f3108'
# flavor_id = 'd2'
# network_name = 'pvt_network'
# key_pair = "ssh_key"
# security_groups = "ssh"
#
# # Find image, flavor, and network
# image = conn.compute.find_image(image_id)
# flavor = conn.compute.find_flavor(flavor_id)
# network = conn.network.find_network(network_name)
#
# # Create the instance
# server = conn.compute.create_server(
#     name=instance_name,
#     image_id=image.id,
#     flavor_id=flavor.id,
#     networks=[{'uuid': network.id}],
# )
#
# print(instance_name)


a = [99,22,33,11,21,222,444,32]
k =a[0]   #99
for i in a:
    if  k < i :
        k = i
    print(k)


# #debug
# 1------k= 99 i = 99
# 99 < 99
#
#
# 2---