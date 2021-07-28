# Example Hardware probe of multiple models
# To be used when running validation tests
from Resources import device_probe

class MacBookPro:

    MacBookPro92_Stock = device_probe.Computer(
        real_model="MacBookPro9,2",
        real_board_id="Mac-6F01561E16C75D06",
        reported_model="MacBookPro9,2", 
        reported_board_id="Mac-6F01561E16C75D06", 
        gpus=[device_probe.Intel(vendor_id=32902, device_id=358, class_code=196608, name="IGPU", model="Intel HD Graphics 4000", pci_path="PciRoot(0x0)/Pci(0x2,0x0)")], 
        igpu=device_probe.Intel(vendor_id=32902, device_id=358, class_code=196608, name="IGPU", model="Intel HD Graphics 4000", pci_path="PciRoot(0x0)/Pci(0x2,0x0)"),
        dgpu=None,
        storage=[device_probe.SATAController(vendor_id=32902, device_id=7683, class_code=67073, name="SATA", model=None, pci_path="PciRoot(0x0)/Pci(0x1f,0x2)")],
        wifi=device_probe.Broadcom(vendor_id=5348, device_id=17201, class_code=163840, name="ARPT", model=None, pci_path="PciRoot(0x0)/Pci(0x1c,0x1)/Pci(0x0,0x0)"),
        cpu=device_probe.CPU(
            name='Intel(R) Core(TM) i5-3210M CPU @ 2.50GHz', 
            flags=['FPU', 'VME', 'DE', 'PSE', 'TSC', 'MSR', 'PAE', 'MCE', 'CX8', 'APIC', 'SEP', 'MTRR', 'PGE', 'MCA', 'CMOV', 'PAT', 'PSE36', 'CLFSH', 'DS', 'ACPI', 'MMX', 'FXSR', 'SSE', 'SSE2', 'SS', 'HTT', 'TM', 'PBE', 'SSE3', 'PCLMULQDQ', 'DTES64', 'MON', 'DSCPL', 'VMX', 'EST', 'TM2', 'SSSE3', 'CX16', 'TPR', 'PDCM', 'SSE4.1', 'SSE4.2', 'x2APIC', 'POPCNT', 'AES', 'PCID', 'XSAVE', 'OSXSAVE', 'TSCTMR', 'AVX1.0', 'RDRAND', 'F16C']
        ),
        oclp_version=None,
        opencore_version=None,
    )

    MacBookPro171_Stock = device_probe.Computer(
        real_model="MacBookPro17,1",
        real_board_id="J293",
        reported_model="MacBookPro17,1",
        reported_board_id="J293",
        gpus=[device_probe.AMD(vendor_id=4098, device_id=26640, class_code=196608, name="display", model="Unknown Unknown", pci_path="")],
        igpu=None,
        dgpu=None,
        storage=[],
        wifi=device_probe.Broadcom(vendor_id=5348, device_id=17445, class_code=163840, name="wlan", model=None, pci_path=""),
        cpu=device_probe.CPU(
            name="Apple M1",
            flags=["FPU", "VME", "DE", "PSE", "TSC", "MSR", "PAE", "MCE", "CX8", "APIC", "SEP", "MTRR", "PGE", "MCA", "CMOV", "PAT", "PSE36", "CLFSH", "DS", "ACPI", "MMX", "FXSR", "SSE", "SSE2", "SS", "HTT", "TM", "PBE", "SSE3", "PCLMULQDQ", "DTSE64", "MON", "DSCPL", "VMX", "EST", "TM2", "SSSE3", "CX16", "TPR", "PDCM", "SSE4.1", "SSE4.2", "AES", "SEGLIM64"],
        ),
        oclp_version=None,
        opencore_version=None,
    )

class iMac:

    iMac81_Stock = device_probe.Computer(
        # Stock Model
        real_model="iMac8,1", 
        real_board_id="Mac-F226BEC8", 
        reported_model="iMac8,1", 
        reported_board_id="Mac-F226BEC8", 
        gpus=[
            device_probe.AMD(vendor_id=4098, device_id=38088, class_code=196608, name="GFX0", model="ATI Radeon HD 2400", pci_path="PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x0)")
        ], 
        igpu=None, 
        dgpu=device_probe.AMD(vendor_id=4098, device_id=38088, class_code=196608, name="GFX0", model="ATI Radeon HD 2400", pci_path="PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x0)"), 
        storage=[
            device_probe.SATAController(vendor_id=32902, device_id=10281, class_code=67073, name="SATA", model=None, pci_path="PciRoot(0x0)/Pci(0x1f,0x2)")
        ], 
        wifi=device_probe.Broadcom(vendor_id=5348, device_id=17192, class_code=163840, name="ARPT", model=None, pci_path="PciRoot(0x0)/Pci(0x1c,0x4)/Pci(0x0,0x0)"), 
        cpu=device_probe.CPU(
            name="Intel(R) Core(TM)2 Duo CPU     E8135  @ 2.40GHz", 
            flags=["FPU", "VME", "DE", "PSE", "TSC", "MSR", "PAE", "MCE", "CX8", "APIC", "SEP", "MTRR", "PGE", "MCA", "CMOV", "PAT", "PSE36", "CLFSH", "DS", "ACPI", "MMX", "FXSR", "SSE", "SSE2", "SS", "HTT", "TM", "PBE", "SSE3", "DTES64", "MON", "DSCPL", "VMX", "EST", "TM2", "SSSE3", "CX16", "TPR", "PDCM", "SSE4.1"]
        ), 
        oclp_version=None,
        opencore_version=None,
    )

    iMac112_Stock = device_probe.Computer(
        # Stock Model
        real_model="iMac11,2", 
        real_board_id="Mac-F2238AC8", 
        reported_model="iMac11,2", 
        reported_board_id="Mac-F2238AC8", 
        gpus=[
            device_probe.AMD(vendor_id=4098, device_id=38024, class_code=196608, name="GFX0", model="ATI Radeon HD 4670", pci_path="PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x0)")
        ], 
        igpu=None, 
        dgpu=device_probe.AMD(vendor_id=4098, device_id=38024, class_code=196608, name="GFX0", model="ATI Radeon HD 4670", pci_path="PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x0)"), 
        storage=[
            device_probe.SATAController(vendor_id=32902, device_id=15138, class_code=67073, name="SATA", model=None, pci_path="PciRoot(0x0)/Pci(0x1f,0x2)")
        ], 
        wifi=device_probe.Atheros(vendor_id=5772, device_id=42, class_code=163840, name="ARPT", model=None, pci_path="PciRoot(0x0)/Pci(0x1c,0x1)/Pci(0x0,0x0)"), 
        cpu=device_probe.CPU(
            name="Intel(R) Core(TM) i3 CPU         540  @ 3.07GHz", 
            flags=["FPU", "VME", "DE", "PSE", "TSC", "MSR", "PAE", "MCE", "CX8", "APIC", "SEP", "MTRR", "PGE", "MCA", "CMOV", "PAT", "PSE36", "CLFSH", "DS", "ACPI", "MMX", "FXSR", "SSE", "SSE2", "SS", "HTT", "TM", "PBE", "SSE3", "DTES64", "MON", "DSCPL", "VMX", "EST", "TM2", "SSSE3", "CX16", "TPR", "PDCM", "SSE4.1", "SSE4.2", "POPCNT", "PCID"]
        ), 
        oclp_version=None, 
        opencore_version=None
    )

class MacPro:

    MacPro31_Stock = device_probe.Computer(
        # Stock Model, stock TS1 GPU and no Wifi card
        real_model="MacPro3,1",
        real_board_id="Mac-F42C88C8",
        reported_model="MacPro3,1",
        reported_board_id="Mac-F42C88C8",
        gpus=[
            device_probe.AMD(vendor_id=4098, device_id=38272, class_code=196608, name="GFX0", model="ATI Radeon HD 2600", pci_path="PciRoot(0x0)/Pci(0x5,0x0)/Pci(0x0,0x0)")
        ],
        igpu=None,
        dgpu=device_probe.AMD(vendor_id=4098, device_id=38272, class_code=196608, name="GFX0", model="ATI Radeon HD 2600", pci_path="PciRoot(0x0)/Pci(0x5,0x0)/Pci(0x0,0x0)"),
        storage=[
            device_probe.SATAController(vendor_id=32902, device_id=9857, class_code=67073, name="SATA", model=None, pci_path="PciRoot(0x0)/Pci(0x1f,0x2)")
        ],
        wifi=None,
        cpu=device_probe.CPU(
            name="Intel(R) Xeon(R) CPU           X5482  @ 3.20GHz",
            flags=["FPU", "VME", "DE", "PSE", "TSC", "MSR", "PAE", "MCE", "CX8", "APIC", "SEP", "MTRR", "PGE", "MCA", "CMOV", "PAT", "PSE36", "CLFSH", "DS", "ACPI", "MMX", "FXSR", "SSE", "SSE2", "SS", "HTT", "TM", "PBE", "SSE3", "DTES64", "MON", "DSCPL", "VMX", "EST", "TM2", "SSSE3", "CX16", "TPR", "PDCM", "SSE4.1"],
        ),
        oclp_version=None,
        opencore_version=None,
    )

    MacPro31_Upgrade = device_probe.Computer(
        # Upgraded Model, TS2 GPU and El-Capitan era Wifi card
        real_model="MacPro3,1",
        real_board_id="Mac-F42C88C8",
        reported_model="MacPro3,1",
        reported_board_id="Mac-F42C88C8",
        gpus=[
            device_probe.AMD(vendor_id=4098, device_id=26808, class_code=196608, name="GFX0", model="ATI Radeon HD 5770", pci_path="PciRoot(0x0)/Pci(0x5,0x0)/Pci(0x0,0x0)")
        ],
        igpu=None,
        dgpu=device_probe.AMD(vendor_id=4098, device_id=26808, class_code=196608, name="GFX0", model="ATI Radeon HD 5770", pci_path="PciRoot(0x0)/Pci(0x5,0x0)/Pci(0x0,0x0)"),
        storage=[
            device_probe.SATAController(vendor_id=32902, device_id=9857, class_code=67073, name="SATA", model=None, pci_path="PciRoot(0x0)/Pci(0x1f,0x2)")
        ],
        wifi=device_probe.Broadcom(
            vendor_id=5348, device_id=17192, class_code=163840, name="ARPT", model=None, pci_path="PciRoot(0x0)/Pci(0x1c,0x3)/Pci(0x0,0x0)"
        ),
        cpu=device_probe.CPU(
            name="Intel(R) Xeon(R) CPU           X5482  @ 3.20GHz",
            flags=["FPU", "VME", "DE", "PSE", "TSC", "MSR", "PAE", "MCE", "CX8", "APIC", "SEP", "MTRR", "PGE", "MCA", "CMOV", "PAT", "PSE36", "CLFSH", "DS", "ACPI", "MMX", "FXSR", "SSE", "SSE2", "SS", "HTT", "TM", "PBE", "SSE3", "DTES64", "MON", "DSCPL", "VMX", "EST", "TM2", "SSSE3", "CX16", "TPR", "PDCM", "SSE4.1"],
        ),
        oclp_version=None,
        opencore_version=None,
    )

    MacPro31_Modern_AMD = device_probe.Computer(
        # Upgraded Model, Polaris GPU and BCM94360CD
        real_model="MacPro3,1",
        real_board_id="Mac-F42C88C8",
        reported_model="MacPro3,1",
        reported_board_id="Mac-F42C88C8",
        gpus=[
            device_probe.AMD(vendor_id=4098, device_id=26591, class_code=196608, name="GFX0", model="Radeon RX 470/570", pci_path="PciRoot(0x0)/Pci(0x5,0x0)/Pci(0x0,0x0)")
        ],
        igpu=None,
        dgpu=device_probe.AMD(vendor_id=4098, device_id=26591, class_code=196608, name="GFX0", model="Radeon RX 470/570", pci_path="PciRoot(0x0)/Pci(0x5,0x0)/Pci(0x0,0x0)"),
        storage=[
            device_probe.SATAController(vendor_id=32902, device_id=9857, class_code=67073, name="SATA", model=None, pci_path="PciRoot(0x0)/Pci(0x1f,0x2)")
        ],
        wifi=device_probe.Broadcom(
            vendor_id=5348, device_id=17312, class_code=163840, name="ARPT", model=None, pci_path="PciRoot(0x0)/Pci(0x1c,0x3)/Pci(0x0,0x0)"
        ),
        cpu=device_probe.CPU(
            name="Intel(R) Xeon(R) CPU           X5482  @ 3.20GHz",
            flags=["FPU", "VME", "DE", "PSE", "TSC", "MSR", "PAE", "MCE", "CX8", "APIC", "SEP", "MTRR", "PGE", "MCA", "CMOV", "PAT", "PSE36", "CLFSH", "DS", "ACPI", "MMX", "FXSR", "SSE", "SSE2", "SS", "HTT", "TM", "PBE", "SSE3", "DTES64", "MON", "DSCPL", "VMX", "EST", "TM2", "SSSE3", "CX16", "TPR", "PDCM", "SSE4.1"],
        ),
        oclp_version=None,
        opencore_version=None,
    )
