import React, { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

function Home() {

  const [loading, setLoading] = useState(true);
  const [entries, setEntries] = useState([]);
  const [food, setFood] = useState("");
  const [calories, setCalories] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("/api/calories/");
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const result = await response.json();
        setEntries(result);
      } catch (error) {
        console.error("Error fetching data:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const handleAddEntry = async () => {
    if (food && calories) {
      try {
        const response = await fetch("/api/calories/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem("access")}`,
          },
          body: JSON.stringify({ food, calories: parseInt(calories) }),
        });
        if (!response.ok) {
          throw new Error("Failed to add entry");
        }
        const newEntry = await response.json();
        setEntries([...entries, newEntry]);
        setFood("");
        setCalories("");
      } catch (error) {
        console.error("Error adding entry:", error);
      }
    }
  };

  const handleDeleteEntry = async (id) => {
    try {
      const response = await fetch(`/api/calories/${id}/`, {
        method: "DELETE",
        headers: {
          "Authorization": `Bearer ${localStorage.getItem("access")}`,
        },
      });
      if (response.ok) {
        setEntries(entries.filter(entry => entry.id !== id));
      } else {
        throw new Error("Failed to delete entry");
      }
    } catch (error) {
      console.error("Error deleting entry:", error);
    }
  };

  const totalCalories = entries.reduce((total, entry) => total + entry.calories, 0);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="container mt-5">
      <h1 className="text-center mb-4">Calorie Tracker</h1>

      {/* Input Form */}
      <div className="card p-4 mb-4">
        <div className="row g-3">
          <div className="col-md-6">
            <input
              type="text"
              className="form-control"
              placeholder="Food Item"
              value={food}
              onChange={(e) => setFood(e.target.value)}
            />
          </div>
          <div className="col-md-4">
            <input
              type="number"
              className="form-control"
              placeholder="Calories"
              value={calories}
              onChange={(e) => setCalories(e.target.value)}
            />
          </div>
          <div className="col-md-2">
            <button className="btn btn-primary w-100" onClick={handleAddEntry}>
              Add
            </button>
          </div>
        </div>
      </div>

      {/* Calorie Entries */}
      <div className="card p-4">
        <h3 className="mb-3">Calorie Entries</h3>
        {entries.length > 0 ? (
          <table className="table table-striped">
            <thead>
              <tr>
                <th>#</th>
                <th>Food</th>
                <th>Calories</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {entries.map((entry, index) => (
                <tr key={index}>
                  <td>{index + 1}</td>
                  <td>{entry.food}</td>
                  <td>{entry.calories}</td>
                  <td>
                    <button
                      className="btn btn-danger btn-sm"
                      onClick={() => handleDeleteEntry(entry.id)}
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <p className="text-muted">No entries yet. Add some food items!</p>
        )}
      </div>

      {/* Total Calories */}
      <div className="mt-4 text-center">
        <h4>Total Calories: {totalCalories}</h4>
      </div>
    </div>
  );
}

export default Home;