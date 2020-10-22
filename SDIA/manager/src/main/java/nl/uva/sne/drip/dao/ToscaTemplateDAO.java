/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package nl.uva.sne.drip.dao;

import nl.uva.sne.drip.model.tosca.ToscaTemplate;
import nl.uva.sne.drip.model.User;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

/**
 *
 * @author S. Koulouzis
 */
@Repository
public interface ToscaTemplateDAO extends MongoRepository<ToscaTemplate, String> {

}
