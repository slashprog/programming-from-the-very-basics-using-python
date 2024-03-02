import struct

def read_elf_header(file_path):
    with open(file_path, 'rb') as f:
        # Read ELF identification data (e_ident)
        e_ident = f.read(16)
        
        # Verify that it's an ELF file
        if e_ident[:4] != b'\x7fELF':
            print("Not a valid ELF file.")
            return

        # Determine ELF class (32-bit or 64-bit)
        elf_class = e_ident[4]

        if elf_class == 1:  # 32-bit ELF
            e_type, e_machine, e_version, e_entry, e_phoff, e_shoff, e_flags, e_ehsize, e_phentsize, e_phnum, e_shentsize, e_shnum, e_shstrndx = struct.unpack('HHIIIIIHHHHHH', f.read(40))
        elif elf_class == 2:  # 64-bit ELF
            e_type, e_machine, e_version, e_entry, e_phoff, e_shoff, e_flags, e_ehsize, e_phentsize, e_phnum, e_shentsize, e_shnum, e_shstrndx = struct.unpack('HHIQQQIHHHHHH', f.read(48))
        else:
            print("Unknown ELF class.")
            return

        print("ELF Type:", e_type)
        print("Machine architecture:", e_machine)
        print("Entry point:", hex(e_entry))
        print("Program Header Offset:", e_phoff)
        print("Section Header Offset:", e_shoff)
        print("Number of program headers:", e_phnum)
        print("Number of section headers:", e_shnum)
        print("Section header string table index:", e_shstrndx)


# Example usage
elf_file = '/bin/ls'
read_elf_header(elf_file)
