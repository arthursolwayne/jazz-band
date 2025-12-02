
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

# Marcus: Walking bass line (D minor)
bass_notes = [
    (65, 1.5, 0.375), # D
    (67, 1.875, 0.375), # F
    (69, 2.25, 0.375), # A
    (65, 2.625, 0.375), # D
    (67, 2.75, 0.375), # F
    (69, 3.125, 0.375), # A
    (65, 3.5, 0.375), # D
    (67, 3.875, 0.375), # F
    (69, 4.25, 0.375), # A
    (71, 4.625, 0.375), # B
    (69, 5.0, 0.375), # A
    (67, 5.375, 0.375) # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: 7th chords comping on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.875, 0.375), # D7 (F#)
    (64, 1.875, 0.375), # D7 (A)
    (69, 1.875, 0.375), # D7 (D)
    (67, 1.875, 0.375), # D7 (B)
    # Bar 3
    (62, 3.125, 0.375), # D7 (F#)
    (64, 3.125, 0.375), # D7 (A)
    (69, 3.125, 0.375), # D7 (D)
    (67, 3.125, 0.375), # D7 (B)
    # Bar 4
    (62, 4.625, 0.375), # D7 (F#)
    (64, 4.625, 0.375), # D7 (A)
    (69, 4.625, 0.375), # D7 (D)
    (67, 4.625, 0.375)  # D7 (B)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),   # Kick on 1
    (42, 1.5, 0.375),   # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.375), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.375), # Hihat on 4

    (36, 2.75, 0.375),  # Kick on 1
    (42, 2.75, 0.375),  # Hihat on 1
    (38, 3.125, 0.375), # Snare on 2
    (42, 3.125, 0.375), # Hihat on 2
    (36, 3.5, 0.375),   # Kick on 3
    (42, 3.5, 0.375),   # Hihat on 3
    (38, 3.875, 0.375), # Snare on 4
    (42, 3.875, 0.375), # Hihat on 4

    (36, 4.25, 0.375),  # Kick on 1
    (42, 4.25, 0.375),  # Hihat on 1
    (38, 4.625, 0.375), # Snare on 2
    (42, 4.625, 0.375), # Hihat on 2
    (36, 5.0, 0.375),   # Kick on 3
    (42, 5.0, 0.375),   # Hihat on 3
    (38, 5.375, 0.375), # Snare on 4
    (42, 5.375, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax melody (short motif, sing, leave it hanging, come back)
sax_notes = [
    (62, 1.5, 0.375),   # D
    (64, 1.875, 0.375), # F
    (67, 2.25, 0.375),  # B
    (62, 2.625, 0.375), # D
    (64, 3.125, 0.375), # F
    (69, 3.5, 0.375),   # A
    (67, 3.875, 0.375), # B
    (62, 4.25, 0.375),  # D
    (64, 4.625, 0.375), # F
    (69, 5.0, 0.375),   # A
    (67, 5.375, 0.375)  # B
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
