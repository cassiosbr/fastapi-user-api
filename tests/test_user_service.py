from types import SimpleNamespace
from unittest.mock import Mock
from app.services.user_service import UserService

def test_create_user():
    mock_db = Mock()
    mock_repo = Mock()
    mock_repo.get_user_by_email.return_value = None  # Simula que o email não existe
    mock_repo.create.return_value = SimpleNamespace(id=1, name="Test User", email="test@example.com")
    
    user_service = UserService(mock_repo)
    user = user_service.create_user(mock_db, "Test User", "test@example.com", "password123")

    # mock_repo.get_user_by_email.assert_called_once_with(mock_db, 'test@example.com')
    # mock_repo.create.assert_called_once_with(mock_db, "Test User", "test@example.com")
    
    assert user.id == 1
    assert user.name == "Test User"
    assert user.email == "test@example.com" 

def test_create_user_with_existing_email():
    mock_db = Mock()
    mock_repo = Mock()
    
    mock_repo.get_user_by_email.return_value = SimpleNamespace(id=1, name="Existing User", email="existing@example.com")
    user_service = UserService(mock_repo)
    
    try:
        user_service.create_user(mock_db, "New User", "existing@example.com", "password123")
    except ValueError as e:
        assert str(e) == "Email já existe"

def test_create_user_with_empty_name():
    mock_db = Mock()
    mock_repo = Mock()
    user_service = UserService(mock_repo)
    
    try:
        user_service.create_user(mock_db, "", "test@example.com", "password123")
    except ValueError as e:
        assert str(e) == "Nome e email são obrigatórios"

def test_create_user_with_empty_email():
    mock_db = Mock()
    mock_repo = Mock()
    user_service = UserService(mock_repo)

    try:
        user_service.create_user(mock_db, "Test User", "", "password123")
    except ValueError as e:
        assert str(e) == "Nome e email são obrigatórios"

def test_create_user_with_long_name():
    mock_db = Mock()
    mock_repo = Mock()
    user_service = UserService(mock_repo)

    long_name = "A" * 101  # Nome com 101 caracteres

    try:
        user_service.create_user(mock_db, long_name, "test@example.com", "password123")
    except ValueError as e:
        assert str(e) == "O nome deve ter no máximo 100 caracteres"