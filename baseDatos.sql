
CREATE TABLE Normativas (
    NroRegistro INT PRIMARY KEY,
    TipoNormativa VARCHAR(250),
    NroNormativa VARCHAR(250),
    Fecha DATE,
    Descripcion VARCHAR(250),
    Categoria VARCHAR(250),
    Jurisdiccion VARCHAR(250),
    OrganoLegislativo VARCHAR(250),
    PalabrasClave VARCHAR(250)
);

INSERT INTO Normativas (NroRegistro, TipoNormativa, NroNormativa, Fecha, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabrasClave)
VALUES (1, 'Ley', '20.744', '2021-01-01', 'Ley de Contrato de Trabajo', 'Laboral', 'Argentina', 'Congreso de la Nación', 'Contrato, Trabajo');

INSERT INTO Normativas (NroRegistro, TipoNormativa, NroNormativa, Fecha, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabrasClave)
VALUES (2, 'Ley', '27.555', '2022-02-01', 'Ley de Teletrabajo', 'Laboral', 'Argentina', 'Congreso de la Nación', 'Teletrabajo');

INSERT INTO Normativas (NroRegistro, TipoNormativa, NroNormativa, Fecha, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabrasClave)
VALUES (3, 'Ley', '7642', '2023-03-01', 'Ley de Ejercicio Profesional de la Informática en Córdoba', 'Profesional', 'Córdoba', 'Legislatura de la Provincia', 'Informática, Ejercicio Profesional');
