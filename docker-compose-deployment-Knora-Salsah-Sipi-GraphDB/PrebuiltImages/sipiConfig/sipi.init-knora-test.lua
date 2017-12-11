
--
-- Copyright © 2016 Lukas Rosenthaler, Andrea Bianco, Benjamin Geer,
-- Ivan Subotic, Tobias Schweizer, André Kilchenmann, and André Fatton.
-- This file is part of Sipi.
-- Sipi is free software: you can redistribute it and/or modify
-- it under the terms of the GNU Affero General Public License as published
-- by the Free Software Foundation, either version 3 of the License, or
-- (at your option) any later version.
-- Sipi is distributed in the hope that it will be useful,
-- but WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
-- Additional permission under GNU AGPL version 3 section 7:
-- If you modify this Program, or any covered work, by linking or combining
-- it with Kakadu (or a modified version of that library), containing parts
-- covered by the terms of the Kakadu Software Licence, the licensors of this
-- Program grant you additional permission to convey the resulting work.
-- See the GNU Affero General Public License for more details.
-- You should have received a copy of the GNU Affero General Public
-- License along with Sipi.  If not, see <http://www.gnu.org/licenses/>.

require "get_knora_session"

-------------------------------------------------------------------------------
-- This function is being called from sipi before the file is served
-- Knora is called to ask for the user's permissions on the file
-- Parameters:
--    prefix: This is the prefix that is given on the IIIF url
--    identifier: the identifier for the image
--    cookie: The cookie that may be present
--
-- Returns:
--    permission:
--       'allow' : the view is allowed with the given IIIF parameters
--       'restrict:watermark=<path-to-watermark>' : Add a watermark
--       'restrict:size=<iiif-size-string>' : reduce size/resolution
--       'deny' : no access!
--    filepath: server-path where the master file is located
-------------------------------------------------------------------------------
function pre_flight(prefix,identifier,cookie)

    --
    -- For Knora Sipi integration testing
    -- Always the same test file is served
    -- Make sure that this image file exists in config.imgroot
    --

    if config.prefix_as_path then
        filepath = config.imgroot .. '/' .. prefix .. '/' .. 'Leaves.jpg'
    else
        filepath = config.imgroot .. '/' .. 'Leaves.jpg'
    end

    if prefix == "thumbs" then
        -- always allow thumbnails
        return 'allow', filepath
    end

    if prefix == "tmp" then
        -- always deny access to tmp folder
        return 'deny'
    end


    if prefix == "knora" then

        knora_cookie_header = nil

        if cookie ~='' then

            -- tries to extract the Knora session id from the cookie:
            -- gets the digits between "sid=" and the closing ";" (only given in case of several key value pairs)
            -- returns nil if it cannot find it
            session_id = get_session_id(cookie)

            if session_id == nil then
                -- no session_id could be extracted
                print("cookie key is invalid: " .. cookie)
            else
                knora_cookie_header = { Cookie = "KnoraAuthentication=" .. session_id }
            end
        end

        knora_url = 'http://' .. config.knora_path .. ':' .. config.knora_port .. '/v1/files/' .. identifier

        --print("knora_url: " .. knora_url)

        success, result = server.http("GET", knora_url, knora_cookie_header, 5000)

        -- check HTTP request was successful
        if not success then
            server.log("Server.http() failed: " .. result, server.loglevel.LOG_ERR)
            return 'deny'
        end

        if result.status_code ~= 200 then
            server.log("Knora returned HTTP status code " .. result.status_code)
            server.log(result.body)
            return 'deny'
        end

        success, response_json = server.json_to_table(result.body)
        if not success then
            server.log("Server.http() failed: " .. response_json, server.loglevel.LOG_ERR)
            return 'deny'
        end

        --print("status: " .. response_json.status)
        --print("permission code: " .. response_json.permissionCode)

        if response_json.status ~= 0 then
            -- something went wrong with the request, Knora returned a non zero status
            return 'deny'
        end

        if response_json.permissionCode == 0 then
            -- no view permission on file
            return 'deny'
        elseif response_json.permissionCode == 1 then
            -- restricted view permission on file
            -- either watermark or size (depends on project, should be returned with permission code by Sipi responder)
            return 'restrict:size=' .. config.thumb_size, filepath
        elseif response_json.permissionCode >= 2 then
            -- full view permissions on file
            return 'allow', filepath
        else
            -- invalid permission code
            return 'deny'
        end
    end

end
-------------------------------------------------------------------------------
