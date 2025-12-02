
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
    (36, 0.0, 1.0),   # Kick on 1
    (42, 0.25, 0.25), # Hihat
    (38, 0.5, 1.0),   # Snare on 2
    (42, 0.75, 0.25), # Hihat
    (36, 1.0, 1.0),   # Kick on 3
    (42, 1.25, 0.25), # Hihat
    (38, 1.5, 1.0),   # Snare on 4
    (42, 1.75, 0.25)  # Hihat
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    (62, 1.5, 0.375), # D (root)
    (64, 1.875, 0.375), # Eb (chromatic approach)
    (65, 2.25, 0.375), # F (3rd)
    (62, 2.625, 0.375), # D
    (60, 2.625, 0.375), # C (chromatic)
    (62, 3.0, 0.375), # D
    (64, 3.375, 0.375), # Eb
    (65, 3.75, 0.375), # F
    (62, 4.125, 0.375), # D
    (60, 4.5, 0.375), # C
    (63, 4.875, 0.375), # D#
    (65, 5.25, 0.375), # F
    (62, 5.625, 0.375), # D
    (64, 6.0, 0.375)    # Eb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.5, 0.375), # D7: D
    (67, 1.5, 0.375), # A
    (64, 1.5, 0.375), # Eb
    (69, 1.5, 0.375), # C
    (62, 1.875, 0.375), # D
    (67, 1.875, 0.375), # A
    (64, 1.875, 0.375), # Eb
    (69, 1.875, 0.375), # C
    # Bar 3
    (62, 2.25, 0.375), # D
    (67, 2.25, 0.375), # A
    (64, 2.25, 0.375), # Eb
    (69, 2.25, 0.375), # C
    (62, 2.625, 0.375), # D
    (67, 2.625, 0.375), # A
    (64, 2.625, 0.375), # Eb
    (69, 2.625, 0.375), # C
    # Bar 4
    (62, 3.0, 0.375), # D
    (67, 3.0, 0.375), # A
    (64, 3.0, 0.375), # Eb
    (69, 3.0, 0.375), # C
    (62, 3.375, 0.375), # D
    (67, 3.375, 0.375), # A
    (64, 3.375, 0.375), # Eb
    (69, 3.375, 0.375), # C
    (62, 3.75, 0.375), # D
    (67, 3.75, 0.375), # A
    (64, 3.75, 0.375), # Eb
    (69, 3.75, 0.375), # C
    (62, 4.125, 0.375), # D
    (67, 4.125, 0.375), # A
    (64, 4.125, 0.375), # Eb
    (69, 4.125, 0.375), # C
    (62, 4.5, 0.375), # D
    (67, 4.5, 0.375), # A
    (64, 4.5, 0.375), # Eb
    (69, 4.5, 0.375), # C
    (62, 4.875, 0.375), # D
    (67, 4.875, 0.375), # A
    (64, 4.875, 0.375), # Eb
    (69, 4.875, 0.375), # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone (Dante) - motif: D - F - Eb - D (melodic fragment)
sax_notes = [
    (62, 1.5, 0.25), # D
    (64, 1.75, 0.25), # F
    (63, 2.0, 0.25), # Eb
    (62, 2.25, 0.25), # D
    (62, 2.625, 0.25), # D (reprise)
    (64, 2.875, 0.25), # F
    (63, 3.125, 0.25), # Eb
    (62, 3.375, 0.25), # D
    (62, 3.75, 0.25), # D
    (64, 4.0, 0.25), # F
    (63, 4.25, 0.25), # Eb
    (62, 4.5, 0.25), # D
    (62, 4.875, 0.25), # D
    (64, 5.125, 0.25), # F
    (63, 5.375, 0.25), # Eb
    (62, 5.625, 0.25) # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 1.0),   # Kick on 1
    (42, 1.75, 0.25), # Hihat
    (38, 2.0, 1.0),   # Snare on 2
    (42, 2.25, 0.25), # Hihat
    (36, 2.5, 1.0),   # Kick on 3
    (42, 2.75, 0.25), # Hihat
    (38, 3.0, 1.0),   # Snare on 4
    (42, 3.25, 0.25), # Hihat
    # Bar 3
    (36, 3.5, 1.0),   # Kick on 1
    (42, 3.75, 0.25), # Hihat
    (38, 4.0, 1.0),   # Snare on 2
    (42, 4.25, 0.25), # Hihat
    (36, 4.5, 1.0),   # Kick on 3
    (42, 4.75, 0.25), # Hihat
    (38, 5.0, 1.0),   # Snare on 4
    (42, 5.25, 0.25), # Hihat
    # Bar 4
    (36, 5.5, 1.0),   # Kick on 1
    (42, 5.75, 0.25), # Hihat
    (38, 6.0, 1.0),   # Snare on 2
    (42, 6.25, 0.25)  # Hihat
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
