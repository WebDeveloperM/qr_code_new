import React, { useState, useEffect, useRef } from 'react';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { InputText } from 'primereact/inputtext';
import { FilterMatchMode } from 'primereact/api';
import { OverlayPanel } from 'primereact/overlaypanel';
import { Compyuter } from '../../types/compyuters';
import axioss from '../../api/axios';
import { BASE_IMAGE_URL, BASE_URL } from '../../utils/urls';
import { Link } from 'react-router-dom';
import { GrEdit } from 'react-icons/gr';
import { ModalDeleteComponent } from '../Modal/ModalDelete';

interface IFilterField {
  value: string | null;
  matchMode: FilterMatchMode;
}

interface IFilters {
  [key: string]: IFilterField;
}

interface IFilterOptions {
  departments: { id: number; name: string }[];
  sections: { id: number; name: string }[];
  ip_addresses: string[];
  type_compyuters: { id: number; name: string }[];
}

type Props = {
  checkedComputer: Compyuter[];
  setDeleteCompForChecked: React.Dispatch<React.SetStateAction<boolean>>;
};

export default function ComputerTable({
  checkedComputer,
  setDeleteCompForChecked,
}: Props) {
  const [computers, setComputers] = useState<Compyuter[]>([]);
  const [openDeleteModal, setDeleteOpenModal] = useState(false);
  const [deleteModalData, setDeleteModalData] = useState('');
  const [deleteCompData, setDeleteCompData] = useState(false);
  const [checkedData, setCheckedData] = useState(false);

  const [filterOptions, setFilterOptions] = useState<IFilterOptions>({
    departments: [],
    sections: [],
    ip_addresses: [],
    type_compyuters: [],
  });

  useEffect(() => {
    axioss
      .get(`${BASE_URL}/filter-options/`)
      .then((response) => {
        setFilterOptions(response.data);
      })
      .catch((err) => console.error('Ошибка получения фильтров:', err));
  }, []);

  useEffect(() => {
    setComputers(checkedComputer.map((comp) => ({ ...comp })));
    setDeleteCompForChecked(deleteCompData);
  }, [checkedComputer]);

  const [filters, setFilters] = useState<IFilters>({
    global: { value: '', matchMode: FilterMatchMode.CONTAINS },
    'departament.name': { value: null, matchMode: FilterMatchMode.CONTAINS },
    'section.name': { value: null, matchMode: FilterMatchMode.CONTAINS },
    'type_compyuter.name': { value: null, matchMode: FilterMatchMode.CONTAINS },
    ipadresss: { value: null, matchMode: FilterMatchMode.CONTAINS },
    user: { value: null, matchMode: FilterMatchMode.CONTAINS },
  });

  useEffect(() => {
    axioss
      .get(`${BASE_URL}/all_compyuters/`)
      .then((response) => {
        setComputers(response.data);
      })
      .catch((err) => console.log(err));
  }, [deleteCompData]);

  useEffect(() => {
    axioss
      .get(`${BASE_URL}/get-mac/`)
      .then((response) => {
        setComputers(response.data);
      })
      .catch((error) => console.error('Error fetching MAC:', error));
  }, [checkedData]);

  const qrCodeBodyTemplate = (rowData: Compyuter) => {
    return (
      <img
        src={`${BASE_IMAGE_URL}${rowData.qr_image}`}
        alt="QR Code"
        width="70"
        className="ml-3"
      />
    );
  };

  const isActiveBodyTemplate = (rowData: Compyuter) => {
    return (
      <input
        type="checkbox"
        checked={rowData.isActive}
        disabled
        className="ml-5"
      />
    );
  };

  const isDetail = (rowData: Compyuter) => {
    return (
      <div className="sm:col-span-1 col-span-3 flex items-center">
        <div className="flex items-center space-x-3.5">
          <Link
            to={`view-computer/${rowData.slug}`}
            className="hover:text-primary"
          >
            <svg
              className="fill-current"
              width="18"
              height="18"
              viewBox="0 0 18 18"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M8.99981 14.8219C3.43106 14.8219 0.674805 9.50624 0.562305 9.28124C0.47793 9.11249 0.47793 8.88749 0.562305 8.71874C0.674805 8.49374 3.43106 3.20624 8.99981 3.20624C14.5686 3.20624 17.3248 8.49374 17.4373 8.71874C17.5217 8.88749 17.5217 9.11249 17.4373 9.28124C17.3248 9.50624 14.5686 14.8219 8.99981 14.8219ZM1.85605 8.99999C2.4748 10.0406 4.89356 13.5562 8.99981 13.5562C13.1061 13.5562 15.5248 10.0406 16.1436 8.99999C15.5248 7.95936 13.1061 4.44374 8.99981 4.44374C4.89356 4.44374 2.4748 7.95936 1.85605 8.99999Z"
                fill=""
              />
              <path
                d="M9 11.3906C7.67812 11.3906 6.60938 10.3219 6.60938 9C6.60938 7.67813 7.67812 6.60938 9 6.60938C10.3219 6.60938 11.3906 7.67813 11.3906 9C11.3906 10.3219 10.3219 11.3906 9 11.3906ZM9 7.875C8.38125 7.875 7.875 8.38125 7.875 9C7.875 9.61875 8.38125 10.125 9 10.125C9.61875 10.125 10.125 9.61875 10.125 9C10.125 8.38125 9.61875 7.875 9 7.875Z"
                fill=""
              />
            </svg>
          </Link>
          <Link to={`edit-computer/${rowData.slug}`}>
            <GrEdit className="hover:text-primary" />
          </Link>
          <button
            className="hover:text-primary"
            onClick={() => {
              setDeleteOpenModal(true);
              setDeleteModalData(rowData.slug);
            }}
          >
            <svg
              className="fill-current"
              width="18"
              height="18"
              viewBox="0 0 18 18"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M13.7535 2.47502H11.5879V1.9969C11.5879 1.15315 10.9129 0.478149 10.0691 0.478149H7.90352C7.05977 0.478149 6.38477 1.15315 6.38477 1.9969V2.47502H4.21914C3.40352 2.47502 2.72852 3.15002 2.72852 3.96565V4.8094C2.72852 5.42815 3.09414 5.9344 3.62852 6.1594L4.07852 15.4688C4.13477 16.6219 5.09102 17.5219 6.24414 17.5219H11.7004C12.8535 17.5219 13.8098 16.6219 13.866 15.4688L14.3441 6.13127C14.8785 5.90627 15.2441 5.3719 15.2441 4.78127V3.93752C15.2441 3.15002 14.5691 2.47502 13.7535 2.47502ZM7.67852 1.9969C7.67852 1.85627 7.79102 1.74377 7.93164 1.74377H10.0973C10.2379 1.74377 10.3504 1.85627 10.3504 1.9969V2.47502H7.70664V1.9969H7.67852ZM4.02227 3.96565C4.02227 3.85315 4.10664 3.74065 4.24727 3.74065H13.7535C13.866 3.74065 13.9785 3.82502 13.9785 3.96565V4.8094C13.9785 4.9219 13.8941 5.0344 13.7535 5.0344H4.24727C4.13477 5.0344 4.02227 4.95002 4.02227 4.8094V3.96565ZM11.7285 16.2563H6.27227C5.79414 16.2563 5.40039 15.8906 5.37227 15.3844L4.95039 6.2719H13.0785L12.6566 15.3844C12.6004 15.8625 12.2066 16.2563 11.7285 16.2563Z"
                fill=""
              />
              <path
                d="M9.00039 9.11255C8.66289 9.11255 8.35352 9.3938 8.35352 9.75942V13.3313C8.35352 13.6688 8.63477 13.9782 9.00039 13.9782C9.33789 13.9782 9.64727 13.6969 9.64727 13.3313V9.75942C9.64727 9.3938 9.33789 9.11255 9.00039 9.11255Z"
                fill=""
              />
              <path
                d="M11.2502 9.67504C10.8846 9.64692 10.6033 9.90004 10.5752 10.2657L10.4064 12.7407C10.3783 13.0782 10.6314 13.3875 10.9971 13.4157C11.0252 13.4157 11.0252 13.4157 11.0533 13.4157C11.3908 13.4157 11.6721 13.1625 11.6721 12.825L11.8408 10.35C11.8408 9.98442 11.5877 9.70317 11.2502 9.67504Z"
                fill=""
              />
              <path
                d="M6.72245 9.67504C6.38495 9.70317 6.1037 10.0125 6.13182 10.35L6.3287 12.825C6.35683 13.1625 6.63808 13.4157 6.94745 13.4157C6.97558 13.4157 6.97558 13.4157 7.0037 13.4157C7.3412 13.3875 7.62245 13.0782 7.59433 12.7407L7.39745 10.2657C7.39745 9.90004 7.08808 9.64692 6.72245 9.67504Z"
                fill=""
              />
            </svg>
          </button>
        </div>
      </div>
    );
  };

  const typeComputerBodyTemplate = (rowData: Compyuter) => {
    return (
      <a
        href={`/view-computer/${rowData.slug}`}
        className="text-blue-600 hover:underline"
      >
        {rowData.type_compyuter.name}
      </a>
    );
  };

  const idComputerBodyTemplate = (
    _rowData: Compyuter,
    options: { rowIndex: number },
  ) => {
    return <p className="pl-5">{options.rowIndex + 1}</p>;
  };

  // === Объявляем ref'ы для OverlayPanel с типизацией, допускающей null ===
  const deptOverlay = useRef<OverlayPanel | null>(null);
  const sectionOverlay = useRef<OverlayPanel | null>(null);
  const typeOverlay = useRef<OverlayPanel | null>(null);
  const ipOverlay = useRef<OverlayPanel | null>(null);

  // === Колбэки для выбора значений через OverlayPanel ===
  const handleDepartmentSelect = (depName: string) => {
    setFilters((prev) => ({
      ...prev,
      'departament.name': {
        value: depName,
        matchMode: FilterMatchMode.CONTAINS,
      },
    }));
    (deptOverlay.current as any)?.hide();
  };

  const handleSectionSelect = (secName: string) => {
    setFilters((prev) => ({
      ...prev,
      'section.name': {
        value: secName,
        matchMode: FilterMatchMode.CONTAINS,
      },
    }));
    (sectionOverlay.current as any)?.hide();
  };

  const handleTypeSelect = (typeName: string) => {
    setFilters((prev) => ({
      ...prev,
      'type_compyuter.name': {
        value: typeName,
        matchMode: FilterMatchMode.CONTAINS,
      },
    }));
    (typeOverlay.current as any)?.hide();
  };

  const handleIpSelect = (ipValue: string) => {
    setFilters((prev) => ({
      ...prev,
      ipadresss: {
        value: ipValue,
        matchMode: FilterMatchMode.CONTAINS,
      },
    }));
    (ipOverlay.current as any)?.hide();
  };

  const overlayClassName =
    'p-3 bg-white text-black rounded-md shadow-lg max-h-60 overflow-y-auto';

  const clearFilter = (key: string) => {
    setFilters((prev) => ({
      ...prev,
      [key]: { value: null, matchMode: FilterMatchMode.CONTAINS },
    }));
  };

  const departmentHeader = (
    <div className="flex items-center justify-center">
      <span>Цехы</span>
      {filters['departament.name'] && filters['departament.name'].value && (
        <i
          className="pi pi-times-circle ml-2 cursor-pointer text-red-500"
          title="Очистить"
          onClick={() => clearFilter('departament.name')}
        />
      )}
      <i
        className="pi pi-filter ml-2 cursor-pointer text-gray-700"
        onClick={(e) => (deptOverlay.current as any)?.toggle(e)}
      />
      <OverlayPanel
        ref={deptOverlay}
        className={overlayClassName}
        appendTo={document.body}
      >
        {filterOptions.departments.length === 0 ? (
          <div className="text-gray-500">Нет данных</div>
        ) : (
          filterOptions.departments.map((dep) => (
            <button
              key={dep.id}
              className="block w-full text-left px-3 py-1 rounded hover:bg-gray-100"
              onClick={() => handleDepartmentSelect(dep.name)}
            >
              {dep.name}
            </button>
          ))
        )}
      </OverlayPanel>
    </div>
  );

  const sectionHeader = (
    <div className="flex items-center justify-center">
      <span>Отдел</span>
      {filters['section.name'] && filters['section.name'].value && (
        <i
          className="pi pi-times-circle ml-2 cursor-pointer text-red-500"
          title="Очистить"
          onClick={() => clearFilter('section.name')}
        />
      )}
      <i
        className="pi pi-filter ml-2 cursor-pointer text-gray-700"
        onClick={(e) => (sectionOverlay.current as any)?.toggle(e)}
      />
      <OverlayPanel ref={sectionOverlay} className={overlayClassName} appendTo={document.body}>
        {filterOptions.sections.length === 0 ? (
          <div className="text-gray-500">Нет данных</div>
        ) : (
          filterOptions.sections.map((sec) => (
            <button
              key={sec.id}
              className="block w-full text-left px-3 py-1 rounded hover:bg-gray-100"
              onClick={() => handleSectionSelect(sec.name)}
            >
              {sec.name}
            </button>
          ))
        )}
      </OverlayPanel>
    </div>
  );

  const typeHeader = (
    <div className="flex items-center justify-center">
      <span>Тип орг.техники</span>
      {filters['type_compyuter.name'] && filters['type_compyuter.name'].value && (
        <i
          className="pi pi-times-circle ml-2 cursor-pointer text-red-500"
          title="Очистить"
          onClick={() => clearFilter('type_compyuter.name')}
        />
      )}
      <i
        className="pi pi-filter ml-2 cursor-pointer text-gray-700"
        onClick={(e) => (typeOverlay.current as any)?.toggle(e)}
      />
      <OverlayPanel ref={typeOverlay} className={overlayClassName} appendTo={document.body}>
        {filterOptions.type_compyuters.length === 0 ? (
          <div className="text-gray-500">Нет данных</div>
        ) : (
          filterOptions.type_compyuters.map((typeC) => (
            <button
              key={typeC.id}
              className="block w-full text-left px-3 py-1 rounded hover:bg-gray-100"
              onClick={() => handleTypeSelect(typeC.name)}
            >
              {typeC.name}
            </button>
          ))
        )}
      </OverlayPanel>
    </div>
  );

  const ipHeader = (
    <div className="flex items-center justify-center">
      <span>IP аддрес</span>
      {filters.ipadresss && filters.ipadresss.value && (
        <i
          className="pi pi-times-circle ml-2 cursor-pointer text-red-500"
          title="Очистить"
          onClick={() => clearFilter('ipadresss')}
        />
      )}
      <i
        className="pi pi-filter ml-2 cursor-pointer text-gray-700"
        onClick={(e) => (ipOverlay.current as any)?.toggle(e)}
      />
      {/* <OverlayPanel ref={ipOverlay} className={overlayClassName} appendTo={document.body}>
        {filterOptions.ip_addresses.length === 0 ? (
          <div className="text-gray-500">Нет данных</div>
        ) : (
          filterOptions.ip_addresses.map((ip) => (
            <button
              key={ip}
              className="block w-full text-left px-3 py-1 rounded hover:bg-gray-100"
              onClick={() => handleIpSelect(ip)}
            >
              {ip}
            </button>
          ))
        )}
      </OverlayPanel> */}
    </div>
  );

  return (
    <div className="rounded-sm border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark">
      <div className="sm:flex justify-between py-6 px-4 md:px-6 xl:px-7.5 border-b">
        <h4 className="text-xl font-semibold text-black dark:text-white">
          Компьютеры
        </h4>
        <div className="flex items-center gap-3">
          {/* Глобальный поиск */}
          <InputText
            type="search"
            className="sm:w-[300px] rounded-md border-stroke bg-transparent py-2 px-3 text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"
            onInput={(e: React.FormEvent<HTMLInputElement>) =>
              setFilters({
                ...filters,
                global: {
                  value: e.currentTarget.value,
                  matchMode: FilterMatchMode.CONTAINS,
                },
              })
            }
            placeholder="Поиск..."
          />
        </div>
      </div>

      <DataTable
        value={computers}
        rows={500}
        filters={filters}
        emptyMessage={
          <div
            style={{
              textAlign: 'center',
              padding: '20px',
              fontSize: '16px',
              fontWeight: 'bold',
              color: 'gray',
            }}
          >
            🚫 Данные не найдены
          </div>
        }
        globalFilterFields={[
          'departament.name',
          'section.name',
          'user',
          'type_compyuter.name',
          'ipadresss',
        ]}
        rowClassName={() => 'border border-gray-300'}
        className="p-3 table-border"
      >
        <Column
          field="id"
          header="№"
          body={idComputerBodyTemplate}
          headerStyle={{
            fontWeight: 'bold',
            textAlign: 'center',
            paddingLeft: '15px',
            color: 'black',
            border: '1px solid #c8c5c4',
          }}
        />
        <Column
          field="qr_image"
          header="Qr_code"
          body={qrCodeBodyTemplate}
          headerStyle={{
            fontWeight: 'bold',
            textAlign: 'center',
            padding: '10px',
            paddingLeft: '10px',
            color: 'black',
            border: '1px solid #c8c5c4',
          }}
        />
        <Column
          field="departament.name"
          header={departmentHeader}
          headerStyle={{
            fontWeight: 'bold',
            border: '1px solid #c8c5c4',
            textAlign: 'center',
            padding: '10px',
            color: 'black',
          }}
        />
        <Column
          field="section.name"
          header={sectionHeader}
          headerStyle={{
            fontWeight: 'bold',
            border: '1px solid #c8c5c4',
            textAlign: 'center',
            padding: '10px',
            color: 'black',
          }}
        />
        <Column
          field="user"
          header="Пользователь"
          headerStyle={{
            fontWeight: 'bold',
            border: '1px solid #c8c5c4',
            textAlign: 'center',
            padding: '10px',
            color: 'black',
          }}
        />
        <Column
          field="type_compyuter.name"
          body={typeComputerBodyTemplate}
          header={typeHeader}
          headerStyle={{
            fontWeight: 'bold',
            border: '1px solid #c8c5c4',
            textAlign: 'center',
            padding: '10px',
            color: 'black',
          }}
        />
        <Column
          field="ipadresss"
          header={ipHeader}
          headerStyle={{
            fontWeight: 'bold',
            border: '1px solid #c8c5c4',
            textAlign: 'center',
            padding: '10px',
            color: 'black',
          }}
        />
        <Column
          field="isActive"
          header="Активен"
          body={isActiveBodyTemplate}
          headerStyle={{
            fontWeight: 'bold',
            textAlign: 'center',
            padding: '10px',
            color: 'black',
            border: '1px solid #c8c5c4',
          }}
        />
        <Column
          field="actions"
          header="Действия"
          body={isDetail}
          headerStyle={{
            fontWeight: 'bold',
            textAlign: 'center',
            padding: '10px',
            color: 'black',
            border: '1px solid #c8c5c4',
          }}
        />
      </DataTable>

      <ModalDeleteComponent
        openDeleteModal={openDeleteModal}
        setDeleteOpenModal={setDeleteOpenModal}
        deleteModalData={deleteModalData}
        setDeleteCompData={setDeleteCompData}
        deleteCompData={deleteCompData}
      />
    </div>
  );
}
