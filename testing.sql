-- Testing queries --

-- Search perfumes, need to join Fragrance and Perfume_Details
SELECT f.fname, pd.notes, pd.base_note, pd.rating
FROM Fragrance f
JOIN Perfume_Details pd ON f.fname = pd.fname
WHERE f.username = 'your_username';

-- Most commonly used notes
SELECT pd.notes, COUNT(*) as note_count
FROM Fragrance f
JOIN Perfume_Details pd ON f.fname = pd.fname
GROUP BY pd.notes
ORDER BY note_count DESC
LIMIT 1;

-- Average rating by base note
SELECT pd.base_note, AVG(pd.rating) as avg_rating
FROM Perfume_Details pd
GROUP BY pd.base_note
ORDER BY avg_rating DESC;

-- Show perfumes in each line
SELECT f.fname, pd.notes, pd.base_note, pd.rating
FROM Fragrance f
JOIN Perfume_Details pd ON f.fname = pd.fname
ORDER BY f.fname;

-- Average rating of all perfumes in the collection
SELECT AVG(pd.rating) as avg_rating
FROM Fragrance f
JOIN Perfume_Details pd ON f.fname = pd.fname
WHERE f.username = 'your_username';
