(ns leech-tracker.handler
  (:use compojure.core)
  (:require [compojure.handler :as handler]
            [compojure.route :as route]))

(defroutes app-routes
  (GET "/" [] (slurp (clojure.java.io/resource "templates/base.html")))
  (route/not-found (slurp (clojure.java.io/resource "templates/404.html"))))

(def app
  (handler/site app-routes))
