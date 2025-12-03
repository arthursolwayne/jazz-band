
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.75),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.75),
]

for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: F - C - G - D - F (roots and fifths with chromatic approaches)
# Bar 2: F (C) -> E (approach) -> F
bass_notes = [
    # Bar 2
    (38, 1.5, 0.375), # F2
    (36, 1.875, 0.375), # E2 (chromatic approach)
    (38, 2.25, 0.375), # F2
    # Bar 3
    (43, 2.625, 0.375), # C3
    (41, 2.875, 0.375), # B2 (chromatic approach)
    (43, 3.25, 0.375), # C3
    # Bar 4
    (48, 3.625, 0.375), # G3
    (46, 3.875, 0.375), # F#3 (chromatic approach)
    (48, 4.25, 0.375), # G3
    # Bar 4 (end)
    (38, 4.625, 0.375), # F2
    (36, 4.875, 0.375), # E2 (chromatic approach)
    (38, 5.25, 0.375), # F2
]
for note_number, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C E)
# Bar 3: Gm7 (G Bb D F)
# Bar 4: Cm7 (C Eb G Bb) -> F7 (F A C E)
piano_notes = [
    # Bar 2
    (65, 1.5, 0.375), (68, 1.5, 0.375), (72, 1.5, 0.375), (76, 1.5, 0.375),
    # Bar 3
    (71, 2.625, 0.375), (74, 2.625, 0.375), (77, 2.625, 0.375), (80, 2.625, 0.375),
    # Bar 4
    (72, 3.625, 0.375), (76, 3.625, 0.375), (79, 3.625, 0.375), (83, 3.625, 0.375),
    (65, 4.625, 0.375), (68, 4.625, 0.375), (72, 4.625, 0.375), (76, 4.625, 0.375),
]
for note_number, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Eb - G - rest
sax_notes = [
    (72, 1.5, 0.375), # F
    (69, 1.875, 0.375), # Eb
    (76, 2.25, 0.375), # G
    # Rest for 0.75s
    (72, 3.625, 0.375), # F (repeat)
    (69, 3.875, 0.375), # Eb
    (76, 4.25, 0.375), # G
]
for note_number, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=note_number, start=start, end=start + duration)
    sax.notes.append(note)

# Drums: Fill the bar
# Bar 2
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.75),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.75),
]
for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Bar 3
drum_notes = [
    (36, 2.625, 0.375), (38, 2.875, 0.375), (42, 2.625, 0.75),
    (36, 3.25, 0.375), (38, 3.5, 0.375), (42, 3.25, 0.75),
]
for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Bar 4
drum_notes = [
    (36, 3.625, 0.375), (38, 3.875, 0.375), (42, 3.625, 0.75),
    (36, 4.25, 0.375), (38, 4.5, 0.375), (42, 4.25, 0.75),
    (36, 4.625, 0.375), (38, 4.875, 0.375), (42, 4.625, 0.375),
]
for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
