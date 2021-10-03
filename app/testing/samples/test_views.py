import json

import pytest

from samples.models import Machine, Sample, TSO500RunMetricsRanges, Lab

@pytest.mark.django_db
def test_zero_counts_per_week_month_year(client):
    lab = Lab.objects.create(name="Lab_1")
    Machine.objects.create(lab=lab, name="machine_1", machine_type="TSO500")
    resp =  client.get("/api/labs/summary/?labs=Lab_1",
        content_type="application/json")

    assert resp.status_code == 200

    data = resp.json()
    
    assert data["machine_count"] == 1
    assert data["last_7"] == 0
    assert data["last_30"] == 0
    assert data["last_365"] == 0


@pytest.mark.django_db
def test_add_tso500_run(client):
    zero_samples = Sample.objects.all()
    assert len(zero_samples) == 0

    resp = client.post(
        "/api/tso500/",
        {
            "lab_name": "David's awesome lab",
            "machine_name": "David's awesome machine",
            "machine_type": "TSO500",
            "run" : {
                "name": "David's run",
            },
            "tso500_run_metrics": {
                "output_date": "2011-11-11",
                "output_time": "11:11:11",
                "workflow_version": "v1.5.2",
                "run_metrics": "This was a notes section",
                "pct_pf_reads": 90.0,
                "pct_q30_r1": 90.0,
                "pct_q30_r2": 90.0,
                "applicationversion": "0.0.0.0",
                "rtaversion": "0.0.0.0",
                "runnumber": 10,
                "flowcellserial": "Z00ABCDEF",
                "pr2bottleserial": "NS0000000-BUFFR",
                "reagentkitserial": "NS0000000-REAGT",
                "read1": 101,
                "read2": 101,
                "index1read": 8,
                "index2read": 8,
                "tso500_run_metrics_ranges": {
                    "lsl_pct_pf_reads": 0.0001,
                    "usl_pct_pf_reads": 0,
                    "lsl_q30_r1": 0, 
                    "usl_q30_r2": 0,
                    "lsl_q30_r1": 0,
                    "usl_q30_r2": 0
                }
            },
            "dna_library_qc_metrics_ranges": {
                "lsl_contamination_score": 0,
                "usl_contamination_score": 100,
                "lsl_contamination_p_value": 0,
                "usl_contamination_p_value": 1
            },
            "dna_library_qc_metrics_for_small_variant_calling_and_tmb_ranges" : {
                "lsl_median_insert_size": 1,
                "usl_median_insert_size": 10,
                "lsl_median_exon_coverage": 1,
                "usl_median_exon_coverage": 10,
                "lsl_pct_exon_50x": 1,
                "usl_pct_exon_50x": 100,
            },
            "dna_library_qc_metrics_for_msi_ranges" : {
                "lsl_usable_msi_sites": 0,
                "usl_usable_msi_sites": 100
            },
            "dna_library_qc_metrics_for_cnv_ranges" : {
                "lsl_coverage_mad": 0,
                "usl_coverage_mad": 100,
                "lsl_median_bin_count_cnv_target": 0,
                "usl_median_bin_count_cnv_target": 100,
            },
            "dna_expanded_metrics_ranges" : {
                "lsl_total_pf_reads": 0,
                "lsl_mean_family_size": 0,
                "lsl_median_target_coverage": 0,
                "lsl_pct_chimeric_reads": 0,
                "lsl_pct_exon_100x": 0,
                "lsl_pct_read_enrichment": 0,
                "lsl_pct_usable_umi_reads": 0,
                "lsl_mean_target_coverage": 0,
                "lsl_pct_aligned_reads": 0,
                "lsl_pct_contamination_est": 0,
                "lsl_pct_pf_uq_reads": 0,
                "lsl_pct_target_0_dot_4x_mean": 0,
                "lsl_pct_target_100x": 0,
                "lsl_pct_target_250x": 0,
                "usl_total_pf_reads": 0,
                "usl_mean_family_size": 0,
                "usl_median_target_coverage": 0,
                "usl_pct_chimeric_reads": 0,
                "usl_pct_exon_100x": 0,
                "usl_pct_read_enrichment": 0,
                "usl_pct_usable_umi_reads": 0,
                "usl_mean_target_coverage": 0,
                "usl_pct_aligned_reads": 0,
                "usl_pct_contamination_est": 0,
                "usl_pct_pf_uq_reads": 0,
                "usl_pct_target_0_dot_4x_mean": 0,
                "usl_pct_target_100x": 0,
                "usl_pct_target_250x": 0,
            },
            "rna_library_qc_metrics_ranges" : {
                "lsl_median_cv_gene_500x": 0,
                "usl_median_cv_gene_500x": 0,
                "lsl_total_on_target_reads": 0,
                "usl_total_on_target_reads": 0,
                "lsl_median_insert_size": 0,
                "usl_median_insert_size": 0,
            },
            "rna_expanded_metrics_ranges" : {
                "lsl_pct_chimeric_reads": 0,
                "lsl_pct_on_target_reads": 0,
                "lsl_scaled_median_gene_coverage": 0,
                "lsl_total_pf_reads": 0,
                "usl_pct_chimeric_reads": 0,
                "usl_pct_on_target_reads": 0,
                "usl_scaled_median_gene_coverage": 0,
                "usl_total_pf_reads": 0,
            },
            "samples": [
                {
                    "name" : "hiya_0",
                    "tso_500_sample_metrics": {
                        "analysis_status": {
                            "completed_all_steps": True    
                        },
                        "dna_library_qc_metrics": {
                            "contamination_score": 1,
                            "contamination_p_value": 0.05,
                        },
                        "dna_library_qc_metrics_for_small_variant_calling_and_tmb": {
                            "median_insert_size": 2.0,
                            "median_exon_coverage": 1,
                            "pct_exon_50x": 1,
                        },
                        "dna_library_qc_metrics_for_msi": {
                            "usable_msi_sites": 0,
                        },
                        "dna_library_qc_metrics_for_cnv": {
                            "coverage_mad": 0,
                            "median_bin_count_cnv_target": 0,
                        },
                        "dna_expanded_metrics": {
                            "total_pf_reads": 0,
                            "mean_family_size": 0,
                            "median_target_coverage": 0,
                            "pct_chimeric_reads": 0,
                            "pct_exon_100x": 0,
                            "pct_read_enrichment": 0,
                            "pct_usable_umi_reads": 0,
                            "mean_target_coverage": 0,
                            "pct_aligned_reads": 0,
                            "pct_contamination_est": 0,
                            "pct_pf_uq_reads": 0,
                            "pct_target_0_dot_4x_mean": 0,
                            "pct_target_100x": 0,
                            "pct_target_250x": 0,
                        },
                        "rna_library_qc_metrics" : {
                            "median_cv_gene_500x": 0,
                            "total_on_target_reads": 0,
                            "median_insert_size": 0,
                        },
                        "rna_expanded_metrics": {
                            "pct_chimeric_reads": 0,
                            "pct_on_target_reads": 0,
                            "scaled_median_gene_coverage": 0,
                            "total_pf_reads": 0,
                        },
                    }
                },
            ],
        },
        content_type="application/json"
    )
    assert resp.status_code == 201

    sample = Sample.objects.all()
    assert len(sample) == 1
    assert TSO500RunMetricsRanges.objects.all()[0].lsl_pct_pf_reads == 0.0001
