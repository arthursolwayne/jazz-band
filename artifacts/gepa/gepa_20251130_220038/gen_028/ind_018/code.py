
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 1.0),     # Kick on 1
    (42, 0.0, 0.5),     # Hihat on 1
    (36, 0.75, 1.0),    # Kick on 3
    (42, 0.75, 0.5),    # Hihat on 3
    (38, 1.5, 1.0),     # Snare on 2
    (42, 1.5, 0.5),     # Hihat on 2
    (38, 2.0, 1.0),     # Snare on 4
    (42, 2.0, 0.5)      # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass - Marcus: walking line, chromatic approaches, never the same note twice
bass_notes = [
    (37, 1.5, 0.375),   # F -> Gb
    (38, 1.875, 0.375), # Gb -> G
    (39, 2.25, 0.375),  # G -> Ab
    (40, 2.625, 0.375), # Ab -> A
    (41, 2.625, 0.375), # A -> Bb
    (42, 2.625, 0.375), # Bb -> B
    (43, 2.625, 0.375), # B -> C
    (44, 2.625, 0.375), # C -> Db
    (45, 2.625, 0.375), # Db -> D
    (46, 2.625, 0.375), # D -> Eb
    (47, 2.625, 0.375), # Eb -> E
    (48, 2.625, 0.375)  # E -> F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb) on beat 2
    (53, 1.875, 0.375), # F
    (60, 1.875, 0.375), # A
    (64, 1.875, 0.375), # C
    (62, 1.875, 0.375), # Eb
    # Bar 3: Bb7 (Bb, D, F, Ab) on beat 2
    (58, 3.375, 0.375), # Bb
    (65, 3.375, 0.375), # D
    (64, 3.375, 0.375), # F
    (61, 3.375, 0.375), # Ab
    # Bar 4: E7 (E, G#, B, D) on beat 2
    (60, 4.875, 0.375), # E
    (67, 4.875, 0.375), # G#
    (69, 4.875, 0.375), # B
    (62, 4.875, 0.375)  # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4 (Little Ray)
drum_notes = [
    (36, 1.5, 1.0),     # Kick on 1
    (42, 1.5, 0.5),     # Hihat on 1
    (36, 2.25, 1.0),    # Kick on 3
    (42, 2.25, 0.5),    # Hihat on 3
    (38, 3.0, 1.0),     # Snare on 2
    (42, 3.0, 0.5),     # Hihat on 2
    (38, 3.5, 1.0),     # Snare on 4
    (42, 3.5, 0.5),     # Hihat on 4
    (36, 3.75, 1.0),    # Kick on 1
    (42, 3.75, 0.5),    # Hihat on 1
    (36, 4.5, 1.0),     # Kick on 3
    (42, 4.5, 0.5),     # Hihat on 3
    (38, 5.25, 1.0),    # Snare on 2
    (42, 5.25, 0.5),    # Hihat on 2
    (38, 5.75, 1.0),    # Snare on 4
    (42, 5.75, 0.5)     # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone - Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - Eb - F (octave up on last note)
sax_notes = [
    (53, 1.5, 0.375),   # F
    (58, 1.875, 0.375), # Bb
    (62, 2.25, 0.375),  # Eb
    (64, 2.625, 0.375), # F (octave up)
    (64, 3.0, 0.375),   # F (octave up)
    (62, 3.375, 0.375), # Eb
    (58, 3.75, 0.375),  # Bb
    (53, 4.125, 0.375), # F
    (53, 4.5, 0.375),   # F
    (62, 4.875, 0.375), # Eb
    (58, 5.25, 0.375),  # Bb
    (53, 5.625, 0.375)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
