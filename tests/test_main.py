def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_upload_files(client, testdata):
    filename = "flower.png"
    response = client.post(
        "/uploadfiles/",
        files={"files": (filename, open(testdata(filename), "rb"), "image/png")}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "upload successful",
                               "filenames": [filename]}
