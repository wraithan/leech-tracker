(ns leech-tracker.handler
  (:use compojure.core)
  (:require [cheshire.core :as json]
            [clabango.parser :refer [render-file]]
            [clojure.java.jdbc :as sql]
            [compojure.route :as route]
            [compojure.handler :as handler]))

(defn get-index [] (render-file "leech_tracker/templates/base.html" {}))
(defn get-blocked [] (render-file "leech_tracker/templates/blocked.html" {}))
(defn post-blocked [body]
  (sql/with-connection (System/getenv "DATABASE_URL")
    (sql/insert-record
     :blocked {:url (get (json/parse-string (slurp body) true) :url)})))
(defn get-list []
  (sql/with-connection (System/getenv "DATABASE_URL")
    (json/generate-string (sql/with-query-results results
                            ["SELECT * FROM blocked"]
                            (into [] results)))))
(defn not-found [] (render-file  "leech_tracker/templates/404.html" {}))

(defroutes app-routes
  (GET "/" [] (get-index))
  (GET "/blocked/" [] (get-blocked))
  (POST "/blocked/" {body :body} (post-blocked body))
  (GET "/list/" [] (get-list))
  (route/not-found (not-found)))

(def app
  (handler/site app-routes))
