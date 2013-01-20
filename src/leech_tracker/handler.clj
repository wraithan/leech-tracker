(ns leech-tracker.handler
  (:use compojure.core)
  (:require [compojure.handler :as handler]
            [compojure.route :as route]
            [cheshire.core :as json]
            [clojure.java.jdbc :as sql]))

(defroutes app-routes
  (GET "/" []
       (slurp (clojure.java.io/resource "templates/base.html")))

  (GET "/blocked/" []
       (slurp (clojure.java.io/resource "templates/blocked.html")))

  (POST "/blocked/"
        {body :body}
        (sql/with-connection (System/getenv "DATABASE_URL")
          (sql/insert-record
           :blocked {:url (get (json/parse-string (slurp body) true) :url)})))

  (GET "/list/" []
       (sql/with-connection (System/getenv "DATABASE_URL")
         (json/generate-string (sql/with-query-results results
            ["SELECT * FROM blocked"]
            (into [] results)))))

  (route/not-found
   (slurp (clojure.java.io/resource "templates/404.html"))))

(def app
  (handler/site app-routes))
