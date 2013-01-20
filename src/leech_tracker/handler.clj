(ns leech-tracker.handler
  (:use compojure.core)
  (:require [compojure.handler :as handler]
            [compojure.route :as route]
            [ring.middleware.params :as params]))

(defroutes app-routes
  (GET "/" [] (slurp (clojure.java.io/resource "templates/base.html")))
  (GET "/blocked/" [] "Ohai\n")
  (POST "/blocked/" {params :body} (slurp params))
  (route/not-found (slurp (clojure.java.io/resource "templates/404.html"))))

(def app
  (params/wrap-params (handler/site app-routes)))
