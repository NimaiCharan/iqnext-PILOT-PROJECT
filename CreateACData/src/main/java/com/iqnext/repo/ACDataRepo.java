package com.iqnext.repo;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import com.iqnext.model.ACTimeSeries;

public interface ACDataRepo extends JpaRepository<ACTimeSeries,Long> {
	

}
