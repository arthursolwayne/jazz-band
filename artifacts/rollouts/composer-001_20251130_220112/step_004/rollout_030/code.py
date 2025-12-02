
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here
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

# Marcus: Walking bass line in D, chromatic approaches
# D -> C# -> D -> E -> D -> F -> E -> D
bass_notes = [
    (50, 1.5, 0.375),  # D
    (49, 1.875, 0.375), # C#
    (50, 2.25, 0.375),  # D
    (52, 2.625, 0.375), # E
    (50, 3.0, 0.375),   # D
    (53, 3.375, 0.375), # F
    (52, 3.75, 0.375),  # E
    (50, 4.125, 0.375), # D
    (50, 4.5, 0.375),   # D
    (49, 4.875, 0.375), # C#
    (50, 5.25, 0.375),  # D
    (52, 5.625, 0.375)  # E
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
# D7 -> G7 -> A7 -> D7
piano_notes = [
    # Bar 2
    (62, 1.5, 0.1875), # D
    (67, 1.5, 0.1875), # G
    (67, 1.5, 0.1875), # G (duplicate for 7th)
    (64, 1.5, 0.1875), # B
    # Bar 3
    (67, 2.625, 0.1875), # G
    (72, 2.625, 0.1875), # B
    (72, 2.625, 0.1875), # B (duplicate for 7th)
    (69, 2.625, 0.1875), # D
    # Bar 4
    (62, 3.75, 0.1875), # D
    (67, 3.75, 0.1875), # G
    (67, 3.75, 0.1875), # G (duplicate for 7th)
    (64, 3.75, 0.1875), # B
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

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
    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.375),   # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.375), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.375), # Hihat on 4
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.375),   # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.375), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Saxophone melody (start at bar 2)
# Short motif: D -> F# -> E -> D (with a slight bend on the F#)
sax_notes = [
    (62, 1.5, 0.375),  # D
    (67, 1.875, 0.375), # F#
    (64, 2.25, 0.375),  # E
    (62, 2.625, 0.375), # D
    (67, 3.0, 0.375),   # F#
    (64, 3.375, 0.375), # E
    (62, 3.75, 0.375),  # D
    (67, 4.125, 0.375), # F#
    (64, 4.5, 0.375),   # E
    (62, 4.875, 0.375)  # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
