defmodule AppWeb.PageController do
  use AppWeb, :controller

  # def home(conn, _params) do
  #   # The home page is often custom made,
  #   # so skip the default app layout.
  #   render(conn, :home, layout: false)
  # end

  def home(conn, _params) do
    # The home page is often custom made,
    # so skip the default app layout.
    render(conn, :home, layout: false)
  end

  def welcome(conn, _params) do
    # The home page is often custom made,
    # so skip the default app layout.
    render(conn, :welcome, layout: false)
  end


end
