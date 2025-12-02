
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.375),   # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.375), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),  # Dm root on 2
    (60, 1.875, 0.375), # C on 3
    (62, 2.25, 0.375),  # D on 4
    (63, 2.625, 0.375), # D# on 1
    (62, 3.0, 0.375),   # D on 2
    (60, 3.375, 0.375), # C on 3
    (59, 3.75, 0.375),  # B on 4
    (62, 4.125, 0.375), # D on 1
    (62, 4.5, 0.375),   # D on 2
    (60, 4.875, 0.375), # C on 3
    (59, 5.25, 0.375),  # B on 4
    (62, 5.625, 0.375)  # D on 1
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.5, 0.375),  # D
    (67, 1.5, 0.375),  # G
    (69, 1.5, 0.375),  # Bb
    (71, 1.5, 0.375),  # D
    # Bar 3
    (62, 2.625, 0.375), # D
    (67, 2.625, 0.375), # G
    (69, 2.625, 0.375), # Bb
    (71, 2.625, 0.375), # D
    # Bar 4
    (62, 3.75, 0.375),  # D
    (67, 3.75, 0.375),  # G
    (69, 3.75, 0.375),  # Bb
    (71, 3.75, 0.375)   # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),   # Kick 1
    (42, 1.5, 0.375),   # Hihat 1
    (38, 1.875, 0.375), # Snare 2
    (42, 1.875, 0.375), # Hihat 2
    (36, 2.25, 0.375),  # Kick 3
    (42, 2.25, 0.375),  # Hihat 3
    (38, 2.625, 0.375), # Snare 4
    (42, 2.625, 0.375), # Hihat 4
    # Bar 3
    (36, 3.0, 0.375),   # Kick 1
    (42, 3.0, 0.375),   # Hihat 1
    (38, 3.375, 0.375), # Snare 2
    (42, 3.375, 0.375), # Hihat 2
    (36, 3.75, 0.375),  # Kick 3
    (42, 3.75, 0.375),  # Hihat 3
    (38, 4.125, 0.375), # Snare 4
    (42, 4.125, 0.375), # Hihat 4
    # Bar 4
    (36, 4.5, 0.375),   # Kick 1
    (42, 4.5, 0.375),   # Hihat 1
    (38, 4.875, 0.375), # Snare 2
    (42, 4.875, 0.375), # Hihat 2
    (36, 5.25, 0.375),  # Kick 3
    (42, 5.25, 0.375),  # Hihat 3
    (38, 5.625, 0.375), # Snare 4
    (42, 5.625, 0.375)  # Hihat 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante): One short motif, make it sing
# Motif: Dm7 -> Bb -> Dm7 -> C -> Dm7
sax_notes = [
    (62, 1.5, 0.6),    # D (start on beat 2)
    (60, 2.1, 0.3),    # C
    (62, 2.4, 0.3),    # D
    (60, 2.7, 0.3),    # C
    (62, 3.0, 0.3),    # D
    (67, 3.3, 0.3),    # G
    (62, 3.6, 0.3),    # D
    (60, 3.9, 0.3),    # C
    (62, 4.2, 0.3),    # D
    (60, 4.5, 0.3),    # C
    (62, 4.8, 0.3),    # D
    (62, 5.1, 0.3),    # D
    (60, 5.4, 0.3),    # C
    (62, 5.7, 0.3)     # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
