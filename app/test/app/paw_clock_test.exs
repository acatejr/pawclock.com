defmodule App.PawClockTest do
  use App.DataCase

  alias App.PawClock

  describe "pets" do
    alias App.PawClock.Pet

    import App.PawClockFixtures

    @invalid_attrs %{name: nil}

    test "list_pets/0 returns all pets" do
      pet = pet_fixture()
      assert PawClock.list_pets() == [pet]
    end

    test "get_pet!/1 returns the pet with given id" do
      pet = pet_fixture()
      assert PawClock.get_pet!(pet.id) == pet
    end

    test "create_pet/1 with valid data creates a pet" do
      valid_attrs = %{name: "some name"}

      assert {:ok, %Pet{} = pet} = PawClock.create_pet(valid_attrs)
      assert pet.name == "some name"
    end

    test "create_pet/1 with invalid data returns error changeset" do
      assert {:error, %Ecto.Changeset{}} = PawClock.create_pet(@invalid_attrs)
    end

    test "update_pet/2 with valid data updates the pet" do
      pet = pet_fixture()
      update_attrs = %{name: "some updated name"}

      assert {:ok, %Pet{} = pet} = PawClock.update_pet(pet, update_attrs)
      assert pet.name == "some updated name"
    end

    test "update_pet/2 with invalid data returns error changeset" do
      pet = pet_fixture()
      assert {:error, %Ecto.Changeset{}} = PawClock.update_pet(pet, @invalid_attrs)
      assert pet == PawClock.get_pet!(pet.id)
    end

    test "delete_pet/1 deletes the pet" do
      pet = pet_fixture()
      assert {:ok, %Pet{}} = PawClock.delete_pet(pet)
      assert_raise Ecto.NoResultsError, fn -> PawClock.get_pet!(pet.id) end
    end

    test "change_pet/1 returns a pet changeset" do
      pet = pet_fixture()
      assert %Ecto.Changeset{} = PawClock.change_pet(pet)
    end
  end

  describe "owners" do
    alias App.PawClock.Owner

    import App.PawClockFixtures

    @invalid_attrs %{first_name: nil, last_name: nil, email: nil}

    test "list_owners/0 returns all owners" do
      owner = owner_fixture()
      assert PawClock.list_owners() == [owner]
    end

    test "get_owner!/1 returns the owner with given id" do
      owner = owner_fixture()
      assert PawClock.get_owner!(owner.id) == owner
    end

    test "create_owner/1 with valid data creates a owner" do
      valid_attrs = %{first_name: "some first_name", last_name: "some last_name", email: "some email"}

      assert {:ok, %Owner{} = owner} = PawClock.create_owner(valid_attrs)
      assert owner.first_name == "some first_name"
      assert owner.last_name == "some last_name"
      assert owner.email == "some email"
    end

    test "create_owner/1 with invalid data returns error changeset" do
      assert {:error, %Ecto.Changeset{}} = PawClock.create_owner(@invalid_attrs)
    end

    test "update_owner/2 with valid data updates the owner" do
      owner = owner_fixture()
      update_attrs = %{first_name: "some updated first_name", last_name: "some updated last_name", email: "some updated email"}

      assert {:ok, %Owner{} = owner} = PawClock.update_owner(owner, update_attrs)
      assert owner.first_name == "some updated first_name"
      assert owner.last_name == "some updated last_name"
      assert owner.email == "some updated email"
    end

    test "update_owner/2 with invalid data returns error changeset" do
      owner = owner_fixture()
      assert {:error, %Ecto.Changeset{}} = PawClock.update_owner(owner, @invalid_attrs)
      assert owner == PawClock.get_owner!(owner.id)
    end

    test "delete_owner/1 deletes the owner" do
      owner = owner_fixture()
      assert {:ok, %Owner{}} = PawClock.delete_owner(owner)
      assert_raise Ecto.NoResultsError, fn -> PawClock.get_owner!(owner.id) end
    end

    test "change_owner/1 returns a owner changeset" do
      owner = owner_fixture()
      assert %Ecto.Changeset{} = PawClock.change_owner(owner)
    end
  end

  describe "daycare_sessions" do
    alias App.PawClock.DayCareSession

    import App.PawClockFixtures

    @invalid_attrs %{status: nil, checkout: nil, checkin: nil}

    test "list_daycare_sessions/0 returns all daycare_sessions" do
      day_care_session = day_care_session_fixture()
      assert PawClock.list_daycare_sessions() == [day_care_session]
    end

    test "get_day_care_session!/1 returns the day_care_session with given id" do
      day_care_session = day_care_session_fixture()
      assert PawClock.get_day_care_session!(day_care_session.id) == day_care_session
    end

    test "create_day_care_session/1 with valid data creates a day_care_session" do
      valid_attrs = %{status: "some status", checkout: ~U[2025-04-08 17:35:00Z], checkin: ~U[2025-04-08 17:35:00Z]}

      assert {:ok, %DayCareSession{} = day_care_session} = PawClock.create_day_care_session(valid_attrs)
      assert day_care_session.status == "some status"
      assert day_care_session.checkout == ~U[2025-04-08 17:35:00Z]
      assert day_care_session.checkin == ~U[2025-04-08 17:35:00Z]
    end

    test "create_day_care_session/1 with invalid data returns error changeset" do
      assert {:error, %Ecto.Changeset{}} = PawClock.create_day_care_session(@invalid_attrs)
    end

    test "update_day_care_session/2 with valid data updates the day_care_session" do
      day_care_session = day_care_session_fixture()
      update_attrs = %{status: "some updated status", checkout: ~U[2025-04-09 17:35:00Z], checkin: ~U[2025-04-09 17:35:00Z]}

      assert {:ok, %DayCareSession{} = day_care_session} = PawClock.update_day_care_session(day_care_session, update_attrs)
      assert day_care_session.status == "some updated status"
      assert day_care_session.checkout == ~U[2025-04-09 17:35:00Z]
      assert day_care_session.checkin == ~U[2025-04-09 17:35:00Z]
    end

    test "update_day_care_session/2 with invalid data returns error changeset" do
      day_care_session = day_care_session_fixture()
      assert {:error, %Ecto.Changeset{}} = PawClock.update_day_care_session(day_care_session, @invalid_attrs)
      assert day_care_session == PawClock.get_day_care_session!(day_care_session.id)
    end

    test "delete_day_care_session/1 deletes the day_care_session" do
      day_care_session = day_care_session_fixture()
      assert {:ok, %DayCareSession{}} = PawClock.delete_day_care_session(day_care_session)
      assert_raise Ecto.NoResultsError, fn -> PawClock.get_day_care_session!(day_care_session.id) end
    end

    test "change_day_care_session/1 returns a day_care_session changeset" do
      day_care_session = day_care_session_fixture()
      assert %Ecto.Changeset{} = PawClock.change_day_care_session(day_care_session)
    end
  end
end
