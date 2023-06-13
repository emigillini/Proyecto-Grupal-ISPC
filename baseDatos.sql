
CREATE TABLE Normativas (
    NroRegistro INT PRIMARY KEY,
    TipoNormativa TEXT,
    NroNormativa TEXT,
    Fecha DATE,
    Descripcion TEXT,
    Categoria TEXT,
    Jurisdiccion TEXT,
    OrganoLegislativo TEXT,
    PalabrasClave TEXT
);

INSERT INTO Normativas (NroRegistro, TipoNormativa, NroNormativa, Fecha, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabrasClave)
VALUES (1, 'Ley', '20.744', '2021-01-01', 'Ley de Contrato de Trabajo', 'Laboral', 'Argentina', 'Congreso de la Nación', 'Contrato, Trabajo');

INSERT INTO Normativas (NroRegistro, TipoNormativa, NroNormativa, Fecha, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabrasClave)
VALUES (2, 'Ley', '27.555', '2022-02-01', 'Ley de Teletrabajo', 'Laboral', 'Argentina', 'Congreso de la Nación', 'Teletrabajo');

INSERT INTO Normativas (NroRegistro, TipoNormativa, NroNormativa, Fecha, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabrasClave)
VALUES (3, 'Ley', '7642', '2023-03-01', 'Ley de Ejercicio Profesional de la Informática en Córdoba', 'Profesional', 'Córdoba', 'Legislatura de la Provincia', 'Informática, Ejercicio Profesional');
