from django import forms


class formfield(forms.form):
    
    nama_lengkap           = forms.namalengkap(required=false)
    jenis_kelamin          = forms.jeniskelamin(required=false)
    alamat                 = forms.alamat(required=false)
    tempat_tanggal_lahir   = forms.tempattanggallahir(required=false)
    NISN                   = forms.NISN(required=false)
    NIK                    = forms.NIK(required=false)
    email_input            = forms.EmailInput(required=false)

    nama_orang_tua         = forms.namaorangtua(required=false)
    pekerjaan_orang_tua    = forms.pekerjaanorangtua(required=false)
    no_HP                  = forms.nohp(required=false)

    pilihan = (
        ('jurusan', 'MIPA'),
        ('jurusan', 'IPS'),

    )