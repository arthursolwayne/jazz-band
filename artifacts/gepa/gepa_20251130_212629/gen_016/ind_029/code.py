
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2: F -> G -> Ab -> A -> Bb -> B -> C -> Db
    (45, 1.5), (47, 1.875), (48, 2.25), (49, 2.625),
    (50, 3.0), (51, 3.375), (52, 3.75), (54, 4.125)
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2, G7 on beat 4
    (59, 2.25), (61, 2.25), (63, 2.25), (65, 2.25),  # F7
    (61, 3.0), (63, 3.0), (65, 3.0), (67, 3.0),      # G7
    # Bar 3: C7 on beat 2, D7 on beat 4
    (62, 3.75), (64, 3.75), (67, 3.75), (69, 3.75),  # C7
    (64, 4.5), (66, 4.5), (69, 4.5), (71, 4.5),      # D7
    # Bar 4: F7 on beat 2, G7 on beat 4
    (59, 5.25), (61, 5.25), (63, 5.25), (65, 5.25),  # F7
    (61, 6.0), (63, 6.0), (65, 6.0), (67, 6.0)       # G7
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(n)

# Sax: Melody - one short motif, make it sing
# Motif: F -> Ab -> Bb -> C
# Start at 1.5s, leave it hanging at 2.0s, return to finish at 2.5s
sax_notes = [
    (53, 1.5, 2.0),   # F
    (56, 2.0, 2.5),   # Ab
    (58, 2.5, 3.0),   # Bb
    (60, 3.0, 3.5),   # C
    (56, 3.75, 4.125), # Ab
    (58, 4.125, 4.5), # Bb
    (60, 4.5, 5.0),   # C
    (59, 5.25, 5.75), # B
    (60, 5.75, 6.0)   # C
]
for note, start, end in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=start, end=end)
    sax.notes.append(n)

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_start = 1.5
for bar in range(2, 5):
    bar_time = bar_start + (bar - 2) * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_time, end=bar_time + 0.125)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_time + 0.375, end=bar_time + 0.5)
    hihat = [
        pretty_midi.Note(velocity=80, pitch=42, start=bar_time + 0.0, end=bar_time + 0.125),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_time + 0.375, end=bar_time + 0.5),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_time + 0.75, end=bar_time + 0.875),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_time + 1.125, end=bar_time + 1.25)
    ]
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.extend(hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
