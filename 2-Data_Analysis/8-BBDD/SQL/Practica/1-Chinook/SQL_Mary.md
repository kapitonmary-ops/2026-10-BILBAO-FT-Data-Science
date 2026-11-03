#1 Obtén los clientes de brasil
SELECT *
FROM customers c
WHERE Country = "Brazil";

#2 Obtén los empleados que son agentes de ventas
SELECT *
FROM employees e
WHERE Title = "Sales Support Agent";

#3 Obtén las canciones de ‘AC/DC
SELECT *
FROM tracks t
WHERE Composer = "AC/DC";

#4 Obtén los campos de los clientes que no sean de USA: Nombre completo, ID, País

SELECT FirstName, LastName, CustomerId, Country
FROM Customers
WHERE Country != "USA";

#5 Obtén los empleados que son agentes de ventas: Nombre completo, Dirección
(Ciudad, Estado, País) y email

SELECT
	FirstName,
	LastName,
	City,
	State,
	Country,
	Email
FROM Employees
WHERE Title = "Sales Support Agent";

#6 Obtén una lista con los países no repetidos a los que se han emitido facturas

SELECT DISTINCT BillingCountry
FROM invoices i;

#7 Obtén una lista con los estados de USA no repetidos de donde son los clientes y
cuántos clientes en cada uno.

SELECT
    State,
    COUNT(*)
FROM customers
GROUP BY State;

#8 Cuántos artículos tiene la factura 37? - "4"

SELECT SUM(Quantity)
FROM invoice_items
WHERE InvoiceId = "37";

#9 Cuántas canciones tiene ‘AC/DC’? - "8"
SELECT COUNT(*)
FROM tracks t
WHERE Composer = "AC/DC";

#10 Cuántos artículos tiene cada factura?
SELECT InvoiceId, Count(*)
FROM invoice_items
GROUP BY InvoiceId;

#11 Cuántas facturas hay de cada país?
SELECT i.BillingCountry , Count(*)
FROM invoices i
GROUP BY BillingCountry;

#12 Cuántas facturas ha habido en 2009 y 2011?  - "166"
SELECT COUNT(*)
FROM invoices
WHERE InvoiceDate LIKE '2009%'
   OR InvoiceDate LIKE '2011%';

#13 Cuántas facturas ha habido entre 2009 y 2011? - "249"
SELECT COUNT(*)
FROM invoices
WHERE InvoiceDate
    BETWEEN '2009-01-01' AND '2011-12-31';

#14 Cuántas clientes hay de España y de Brasil? - "6"
SELECT COUNT(*)
FROM customers c
WHERE c.Country = "Spain"
    OR  c.Country = "Brazil";

#15 Obtén las canciones que su título empieza por ‘You’
SELECT *
FROM tracks
WHERE Name LIKE 'You%';

SEGUNDA PARTE:

#1 Facturas de Clientes de Brasil, Nombre del cliente, Id de factura, fecha de la
factura y el país de la factura
SELECT
    	c.FirstName,
    	c.LastName,
    	i.InvoiceId,
    	i.InvoiceDate,
    	i.BillingCountry
FROM customers c
JOIN invoices i
	ON c.CustomerId = i.CustomerId
WHERE c.Country = 'Brazil';

#2 Obtén cada factura asociada a cada agente de ventas con su nombre completo
SELECT
    	i.InvoiceId,
    	e.FirstName,
    	e.LastName
FROM invoices i
JOIN customers c
    	ON i.CustomerId = c.CustomerId
JOIN employees e
    	ON c.SupportRepId = e.EmployeeId;

#3 Obtén el nombre del cliente, el país, el nombre del agente y el total
SELECT
	i.Total,
	c.FirstName AS CustomerName,
    	c.LastName AS CustomerSurname,
	c.Country,
	e.FirstName AS AgentName
FROM customers c
JOIN  employees e
	ON c.SupportRepId = e.EmployeeId
JOIN invoices i
	ON c.CustomerId = i.CustomerId;

#4 Obtén cada artículo de la factura con el nombre de la canción
SELECT
	i.InvoiceLineId,
	t.Name
FROM invoice_items i
JOIN tracks t
    ON i.TrackId = t.TrackId;

#5 Muestra todas las canciones con su nombre, formato, álbum y género
SELECT
    	t.Name as NameSong,
    	m.Name as NameGenre,
    	a.Title,
    	g.Name as NameFormat
FROM tracks t
JOIN albums a
    	ON t.AlbumId = a.AlbumId
JOIN genres g
    	ON g.GenreId = t.GenreId
JOIN media_types m
    	ON t.MediaTypeId = m.MediaTypeId;


#6 Cuántas canciones hay en cada playlist
SELECT
	p.Name,
COUNT(pt.TrackId)
FROM playlist_track pt
JOIN playlists p
	ON pt.PlaylistId = p.PlaylistId
GROUP BY p.Name;



#7 Cuánto ha vendido cada empleado
SELECT
	e.FirstName,
	e.LastName,
	SUM(i.Total)
FROM employees e
JOIN customers c
	ON e.EmployeeId = c.SupportRepId
JOIN invoices i
	ON c.CustomerId = i.CustomerId
GROUP BY e.EmployeeId, e.FirstName, e.LastName;



#8 ¿Quién ha sido el agente de ventas que más ha vendido en 2009?
SELECT
	e.FirstName,
	e.LastName,
SUM(i.Total)
FROM employees e
JOIN customers c
	ON e.EmployeeId = c.SupportRepId
JOIN invoices i
	ON c.CustomerId = i.CustomerId
WHERE i.InvoiceDate LIKE '2009%'
GROUP BY e.EmployeeId, e.FirstName, e.LastName
ORDER BY SUM(i.Total) DESC
LIMIT 1;


#9¿Cuáles son los 3 grupos que más han vendido?
SELECT
    a.Name
FROM artists a
JOIN albums a2
    ON a.ArtistId = a2.ArtistId
JOIN tracks t
    ON a2.AlbumId = t.AlbumId
JOIN invoice_items ii
    ON t.TrackId = ii.TrackId
GROUP BY a.ArtistId, a.Name
ORDER BY SUM(ii.UnitPrice * ii.Quantity) DESC
LIMIT 3;
