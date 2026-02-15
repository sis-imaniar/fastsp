from pydantic import BaseModel
from datetime import date

class EmployeeResponse(BaseModel):
    Id: int
    Nip: str
    Nama: str
    Email: str
    Posisi: str
    Departemen: str
    TanggalMasuk: date
    Status: str
    Telepon: str