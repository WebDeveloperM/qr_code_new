import { ProgramType } from "./texnology";

export type GenericType = {
    id: number;
    name: string;
}

export type Compyuter = {
    id: number;
    departament: {
        id: number,
        name: string,
        boss_fullName: string
    };
    section: {
        id: number,
        department: string,
        name: string,
    };
    warehouse_manager: {
        id: number,
        name: string
    },
    type_compyuter: {
        id: number,
        name: string
    },
    motherboard: {
        id: number,
        name: string
    },
    motherboard_model: {
        id: number,
        name: string
    },
    CPU: {
        id: number,
        name: string
    },
    generation: {
        id: number,
        name: string
    },
    frequency: {
        id: number,
        name: string
    },
    HDD: {
        id: number,
        name: string
    },
    SSD: {
        id: number,
        name: string
    },
    disk_type: {
        id: number,
        name: string
    },
    RAM_type: {
        id: number,
        name: string
    },
    RAMSize: {
        id: number,
        name: string
    },
    GPU: {
        id: number,
        name: string
    },

    printer: GenericType[],

    scaner: GenericType[],
    mfo: GenericType[],

    type_webcamera: GenericType[],

    model_webcam: GenericType[],
    type_monitor: GenericType[],

    seal_number: string,
    user: string,
    ipadresss: string,
    mac_adress: string,

    qr_image: string,
    signature: string | null,
    joinDate: string,
    slug: string,
    isActive: boolean,
    addedUser: number,
    program_with_license_and_systemic: ProgramType[];
    program_with_license_and_additional: ProgramType[];
    program_with_no_license_and_systemic: ProgramType[];
    program_with_no_license_and_additional: ProgramType[];

    internet: boolean;
    OS: string
};


export type InfoComputerData = {
    all_compyuters_count: number,
    all_worked_compyuters_count: number,
    all_compyuters_with_printer: number,
    all_compyuters_with_scaner: number,
    all_compyuters_with_mfo: number,
    all_compyuters_with_webcam: number,
    all_compyuters_with_net: number,
    all_compyuters_with_no_net: number,
    all_noworked_compyuters_count: number
};



