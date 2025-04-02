defmodule AppWeb.PetOwnerLiveTest do
  use AppWeb.ConnCase

  import Phoenix.LiveViewTest
  import App.AccountFixtures

  @create_attrs %{first_name: "some first_name", last_name: "some last_name", email: "some email"}
  @update_attrs %{first_name: "some updated first_name", last_name: "some updated last_name", email: "some updated email"}
  @invalid_attrs %{first_name: nil, last_name: nil, email: nil}

  defp create_pet_owner(_) do
    pet_owner = pet_owner_fixture()
    %{pet_owner: pet_owner}
  end

  describe "Index" do
    setup [:create_pet_owner]

    test "lists all pet_owners", %{conn: conn, pet_owner: pet_owner} do
      {:ok, _index_live, html} = live(conn, ~p"/pet_owners")

      assert html =~ "Listing Pet owners"
      assert html =~ pet_owner.first_name
    end

    test "saves new pet_owner", %{conn: conn} do
      {:ok, index_live, _html} = live(conn, ~p"/pet_owners")

      assert index_live |> element("a", "New Pet owner") |> render_click() =~
               "New Pet owner"

      assert_patch(index_live, ~p"/pet_owners/new")

      assert index_live
             |> form("#pet_owner-form", pet_owner: @invalid_attrs)
             |> render_change() =~ "can&#39;t be blank"

      assert index_live
             |> form("#pet_owner-form", pet_owner: @create_attrs)
             |> render_submit()

      assert_patch(index_live, ~p"/pet_owners")

      html = render(index_live)
      assert html =~ "Pet owner created successfully"
      assert html =~ "some first_name"
    end

    test "updates pet_owner in listing", %{conn: conn, pet_owner: pet_owner} do
      {:ok, index_live, _html} = live(conn, ~p"/pet_owners")

      assert index_live |> element("#pet_owners-#{pet_owner.id} a", "Edit") |> render_click() =~
               "Edit Pet owner"

      assert_patch(index_live, ~p"/pet_owners/#{pet_owner}/edit")

      assert index_live
             |> form("#pet_owner-form", pet_owner: @invalid_attrs)
             |> render_change() =~ "can&#39;t be blank"

      assert index_live
             |> form("#pet_owner-form", pet_owner: @update_attrs)
             |> render_submit()

      assert_patch(index_live, ~p"/pet_owners")

      html = render(index_live)
      assert html =~ "Pet owner updated successfully"
      assert html =~ "some updated first_name"
    end

    test "deletes pet_owner in listing", %{conn: conn, pet_owner: pet_owner} do
      {:ok, index_live, _html} = live(conn, ~p"/pet_owners")

      assert index_live |> element("#pet_owners-#{pet_owner.id} a", "Delete") |> render_click()
      refute has_element?(index_live, "#pet_owners-#{pet_owner.id}")
    end
  end

  describe "Show" do
    setup [:create_pet_owner]

    test "displays pet_owner", %{conn: conn, pet_owner: pet_owner} do
      {:ok, _show_live, html} = live(conn, ~p"/pet_owners/#{pet_owner}")

      assert html =~ "Show Pet owner"
      assert html =~ pet_owner.first_name
    end

    test "updates pet_owner within modal", %{conn: conn, pet_owner: pet_owner} do
      {:ok, show_live, _html} = live(conn, ~p"/pet_owners/#{pet_owner}")

      assert show_live |> element("a", "Edit") |> render_click() =~
               "Edit Pet owner"

      assert_patch(show_live, ~p"/pet_owners/#{pet_owner}/show/edit")

      assert show_live
             |> form("#pet_owner-form", pet_owner: @invalid_attrs)
             |> render_change() =~ "can&#39;t be blank"

      assert show_live
             |> form("#pet_owner-form", pet_owner: @update_attrs)
             |> render_submit()

      assert_patch(show_live, ~p"/pet_owners/#{pet_owner}")

      html = render(show_live)
      assert html =~ "Pet owner updated successfully"
      assert html =~ "some updated first_name"
    end
  end
end
