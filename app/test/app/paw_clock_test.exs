defmodule App.PawClockTest do
  use App.DataCase

  alias App.PawClock

  describe "pets" do
    alias App.PawClock.Pet

    import App.PawClockFixtures

    @invalid_attrs %{name: nil, pet_type: nil}

    test "list_pets/0 returns all pets" do
      pet = pet_fixture()
      assert PawClock.list_pets() == [pet]
    end

    test "get_pet!/1 returns the pet with given id" do
      pet = pet_fixture()
      assert PawClock.get_pet!(pet.id) == pet
    end

    test "create_pet/1 with valid data creates a pet" do
      valid_attrs = %{name: "some name", pet_type: :cat}

      assert {:ok, %Pet{} = pet} = PawClock.create_pet(valid_attrs)
      assert pet.name == "some name"
      assert pet.pet_type == :cat
    end

    test "create_pet/1 with invalid data returns error changeset" do
      assert {:error, %Ecto.Changeset{}} = PawClock.create_pet(@invalid_attrs)
    end

    test "update_pet/2 with valid data updates the pet" do
      pet = pet_fixture()
      update_attrs = %{name: "some updated name", pet_type: :dog}

      assert {:ok, %Pet{} = pet} = PawClock.update_pet(pet, update_attrs)
      assert pet.name == "some updated name"
      assert pet.pet_type == :dog
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

    @invalid_attrs %{first_name: nil, last_name: nil, phone: nil}

    test "list_owners/0 returns all owners" do
      owner = owner_fixture()
      assert PawClock.list_owners() == [owner]
    end

    test "get_owner!/1 returns the owner with given id" do
      owner = owner_fixture()
      assert PawClock.get_owner!(owner.id) == owner
    end

    test "create_owner/1 with valid data creates a owner" do
      valid_attrs = %{first_name: "some first_name", last_name: "some last_name", phone: "some phone"}

      assert {:ok, %Owner{} = owner} = PawClock.create_owner(valid_attrs)
      assert owner.first_name == "some first_name"
      assert owner.last_name == "some last_name"
      assert owner.phone == "some phone"
    end

    test "create_owner/1 with invalid data returns error changeset" do
      assert {:error, %Ecto.Changeset{}} = PawClock.create_owner(@invalid_attrs)
    end

    test "update_owner/2 with valid data updates the owner" do
      owner = owner_fixture()
      update_attrs = %{first_name: "some updated first_name", last_name: "some updated last_name", phone: "some updated phone"}

      assert {:ok, %Owner{} = owner} = PawClock.update_owner(owner, update_attrs)
      assert owner.first_name == "some updated first_name"
      assert owner.last_name == "some updated last_name"
      assert owner.phone == "some updated phone"
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
end
