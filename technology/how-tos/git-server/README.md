# Setting Up a Git Server with SSH Key-Based Access

This guide explains how to set up a Git server with SSH key-based authentication.

## Prerequisites
- A Linux server with SSH access.
- Git installed on the server (`sudo apt install git` for Debian-based systems).
- A client machine with SSH installed.

## Steps

### 1. Create a Git User
On the server, create a dedicated user for Git operations:
```bash
sudo adduser git
```

### 2. Configure SSH Access
1. Switch to the `git` user:
    ```bash
    sudo su - git
    ```
2. Create an `.ssh` directory:
    ```bash
    mkdir -p ~/.ssh && chmod 700 ~/.ssh
    ```
3. Add the client's public SSH key to `~/.ssh/authorized_keys`:
    ```bash
    echo "your-client-public-key" >> ~/.ssh/authorized_keys
    chmod 600 ~/.ssh/authorized_keys
    ```

### 3. Initialize a Bare Repository
1. Create a directory for the repository:
    ```bash
    mkdir -p ~/repositories/my-project.git
    ```
2. Initialize it as a bare repository:
    ```bash
    git init --bare ~/repositories/my-project.git
    ```

### 4. Set Repository Permissions
Ensure the `git` user owns the repository:
```bash
chown -R git:git ~/repositories/my-project.git
```

### 5. Clone the Repository on the Client
On the client machine, clone the repository:
```bash
git clone git@your-server-ip:repositories/my-project.git
```

## Adding Users with Specific Permissions

To allow additional users to access the Git server with specific permissions, follow these steps:

### 1. Add a New User
On the server, create a new user for Git access:
```bash
sudo adduser newuser
```

### 2. Configure SSH Access for the New User
1. Switch to the new user:
    ```bash
    sudo su - newuser
    ```
2. Create an `.ssh` directory:
    ```bash
    mkdir -p ~/.ssh && chmod 700 ~/.ssh
    ```
3. Add the client's public SSH key to `~/.ssh/authorized_keys`:
    ```bash
    echo "new-client-public-key" >> ~/.ssh/authorized_keys
    chmod 600 ~/.ssh/authorized_keys
    ```

### 3. Assign Repository Permissions
To grant the new user access to a specific repository:
1. Add the new user to the `git` group:
    ```bash
    sudo usermod -aG git newuser
    ```
2. Ensure the repository directory has the correct group ownership:
    ```bash
    sudo chown -R git:git ~/repositories/my-project.git
    ```
3. Set group write permissions if needed:
    ```bash
    sudo chmod -R g+rw ~/repositories/my-project.git
    ```
4. Verify the permissions:
    ```bash
    ls -ld ~/repositories/my-project.git
    ```

### 4. Restrict Access (Optional)
If you want to restrict the new user to read-only access:
1. Remove write permissions for the group:
    ```bash
    sudo chmod -R g-w ~/repositories/my-project.git
    ```
2. Ensure the new user is part of the `git` group for read access.

### Notes
- Replace `new-client-public-key` with the actual public key of the new user.
- Adjust permissions based on the level of access required (read-only or read-write).
- Test the new user's access by attempting to clone or push to the repository.
- Replace `your-client-public-key` with the actual public key.
- Replace `your-server-ip` with the server's IP address or hostname.

## Generating SSH Keys

To use SSH key-based authentication, you need to generate an SSH key pair on the client machine. Follow these steps:

### 1. Generate the Key Pair
Run the following command on the client machine:
```bash
ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
```
- Replace `your-email@example.com` with your email address.
- This will create a 4096-bit RSA key pair.

### 2. Save the Key Pair
When prompted:
1. Enter the file path to save the key (or press Enter to use the default location, `~/.ssh/id_rsa`).
2. Optionally, set a passphrase for added security.

### 3. Verify the Keys
Ensure the keys were generated:
```bash
ls ~/.ssh/id_rsa ~/.ssh/id_rsa.pub
```
- `id_rsa` is the private key (keep this secure).
- `id_rsa.pub` is the public key (share this with the server).

### 4. Copy the Public Key to the Server
Use the `ssh-copy-id` command to copy the public key to the server:
```bash
ssh-copy-id git@your-server-ip
```
- Replace `git@your-server-ip` with the appropriate username and server IP address.

Alternatively, manually copy the contents of `~/.ssh/id_rsa.pub` to the server's `~/.ssh/authorized_keys` file.

### Notes
- Ensure the SSH service is running on the server.
- Use a strong passphrase for enhanced security.
- Keep your private key secure and never share it.
- Replace `your-server-ip` with the server's IP address or hostname.

## Troubleshooting
- Ensure the SSH service is running on the server.
- Verify file permissions for `.ssh` and `authorized_keys`.

## References
- [Git Documentation](https://git-scm.com/doc)
- [OpenSSH Documentation](https://www.openssh.com/manual.html)