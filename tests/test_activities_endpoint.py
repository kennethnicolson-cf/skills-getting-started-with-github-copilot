def test_activities_when_requested_then_returns_seeded_activity_data(client):
    # Arrange

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert "Chess Club" in payload
    assert "Programming Class" in payload


def test_activities_when_requested_then_includes_participants_list_structure(client):
    # Arrange

    # Act
    response = client.get("/activities")

    # Assert
    payload = response.json()
    chess = payload["Chess Club"]
    assert isinstance(chess["participants"], list)
    assert all(isinstance(email, str) for email in chess["participants"])
    assert len(payload) >= 1
