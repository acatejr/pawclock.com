defmodule App.PawClock do
  @moduledoc """
  The PawClock context.
  """

  import Ecto.Query, warn: false
  alias App.Repo

  alias App.PawClock.Pet

  @doc """
  Returns the list of pets.

  ## Examples

      iex> list_pets()
      [%Pet{}, ...]

  """
  def list_pets do
    Repo.all(Pet)
  end

  @doc """
  Gets a single pet.

  Raises `Ecto.NoResultsError` if the Pet does not exist.

  ## Examples

      iex> get_pet!(123)
      %Pet{}

      iex> get_pet!(456)
      ** (Ecto.NoResultsError)

  """
  def get_pet!(id), do: Repo.get!(Pet, id)

  @doc """
  Creates a pet.

  ## Examples

      iex> create_pet(%{field: value})
      {:ok, %Pet{}}

      iex> create_pet(%{field: bad_value})
      {:error, %Ecto.Changeset{}}

  """
  def create_pet(attrs \\ %{}) do
    %Pet{}
    |> Pet.changeset(attrs)
    |> Repo.insert()
  end

  @doc """
  Updates a pet.

  ## Examples

      iex> update_pet(pet, %{field: new_value})
      {:ok, %Pet{}}

      iex> update_pet(pet, %{field: bad_value})
      {:error, %Ecto.Changeset{}}

  """
  def update_pet(%Pet{} = pet, attrs) do
    pet
    |> Pet.changeset(attrs)
    |> Repo.update()
  end

  @doc """
  Deletes a pet.

  ## Examples

      iex> delete_pet(pet)
      {:ok, %Pet{}}

      iex> delete_pet(pet)
      {:error, %Ecto.Changeset{}}

  """
  def delete_pet(%Pet{} = pet) do
    Repo.delete(pet)
  end

  @doc """
  Returns an `%Ecto.Changeset{}` for tracking pet changes.

  ## Examples

      iex> change_pet(pet)
      %Ecto.Changeset{data: %Pet{}}

  """
  def change_pet(%Pet{} = pet, attrs \\ %{}) do
    Pet.changeset(pet, attrs)
  end

  alias App.PawClock.Owner

  @doc """
  Returns the list of owners.

  ## Examples

      iex> list_owners()
      [%Owner{}, ...]

  """
  def list_owners do
    Repo.all(Owner)
  end

  @doc """
  Gets a single owner.

  Raises `Ecto.NoResultsError` if the Owner does not exist.

  ## Examples

      iex> get_owner!(123)
      %Owner{}

      iex> get_owner!(456)
      ** (Ecto.NoResultsError)

  """
  def get_owner!(id) do

    Repo.get!(Owner, id)
    |> Repo.preload(:pets)  # Preload the pets association

  end

  @doc """
  Creates a owner.

  ## Examples

      iex> create_owner(%{field: value})
      {:ok, %Owner{}}

      iex> create_owner(%{field: bad_value})
      {:error, %Ecto.Changeset{}}

  """
  def create_owner(attrs \\ %{}) do
    %Owner{}
    |> Owner.changeset(attrs)
    |> Repo.insert()
  end

  @doc """
  Updates a owner.

  ## Examples

      iex> update_owner(owner, %{field: new_value})
      {:ok, %Owner{}}

      iex> update_owner(owner, %{field: bad_value})
      {:error, %Ecto.Changeset{}}

  """
  def update_owner(%Owner{} = owner, attrs) do
    owner
    |> Owner.changeset(attrs)
    |> Repo.update()
  end

  @doc """
  Deletes a owner.

  ## Examples

      iex> delete_owner(owner)
      {:ok, %Owner{}}

      iex> delete_owner(owner)
      {:error, %Ecto.Changeset{}}

  """
  def delete_owner(%Owner{} = owner) do
    Repo.delete(owner)
  end

  @doc """
  Returns an `%Ecto.Changeset{}` for tracking owner changes.

  ## Examples

      iex> change_owner(owner)
      %Ecto.Changeset{data: %Owner{}}

  """
  def change_owner(%Owner{} = owner, attrs \\ %{}) do
    Owner.changeset(owner, attrs)
  end

  alias App.PawClock.DayCareSession

  @doc """
  Returns the list of daycare_sessions.

  ## Examples

      iex> list_daycare_sessions()
      [%DayCareSession{}, ...]

  """
  def list_daycare_sessions do
    Repo.all(DayCareSession)
  end

  @doc """
  Gets a single day_care_session.

  Raises `Ecto.NoResultsError` if the Day care session does not exist.

  ## Examples

      iex> get_day_care_session!(123)
      %DayCareSession{}

      iex> get_day_care_session!(456)
      ** (Ecto.NoResultsError)

  """
  def get_day_care_session!(id), do: Repo.get!(DayCareSession, id)

  @doc """
  Creates a day_care_session.

  ## Examples

      iex> create_day_care_session(%{field: value})
      {:ok, %DayCareSession{}}

      iex> create_day_care_session(%{field: bad_value})
      {:error, %Ecto.Changeset{}}

  """
  def create_day_care_session(attrs \\ %{}) do
    %DayCareSession{}
    |> DayCareSession.changeset(attrs)
    |> Repo.insert()
  end

  @doc """
  Updates a day_care_session.

  ## Examples

      iex> update_day_care_session(day_care_session, %{field: new_value})
      {:ok, %DayCareSession{}}

      iex> update_day_care_session(day_care_session, %{field: bad_value})
      {:error, %Ecto.Changeset{}}

  """
  def update_day_care_session(%DayCareSession{} = day_care_session, attrs) do
    day_care_session
    |> DayCareSession.changeset(attrs)
    |> Repo.update()
  end

  @doc """
  Deletes a day_care_session.

  ## Examples

      iex> delete_day_care_session(day_care_session)
      {:ok, %DayCareSession{}}

      iex> delete_day_care_session(day_care_session)
      {:error, %Ecto.Changeset{}}

  """
  def delete_day_care_session(%DayCareSession{} = day_care_session) do
    Repo.delete(day_care_session)
  end

  @doc """
  Returns an `%Ecto.Changeset{}` for tracking day_care_session changes.

  ## Examples

      iex> change_day_care_session(day_care_session)
      %Ecto.Changeset{data: %DayCareSession{}}

  """
  def change_day_care_session(%DayCareSession{} = day_care_session, attrs \\ %{}) do
    DayCareSession.changeset(day_care_session, attrs)
  end
end
