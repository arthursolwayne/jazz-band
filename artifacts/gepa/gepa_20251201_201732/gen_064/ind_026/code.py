
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Snare on 2 and 4, hihat on every eighth, kick on 1 and 3
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.375, 0.125),  # Hihat on 1&
    (42, 0.5, 0.125),  # Hihat on 2&
    (38, 0.75, 0.375),  # Snare on 2
    (42, 1.0, 0.125),  # Hihat on 2&
    (42, 1.125, 0.125),  # Hihat on 3&
    (36, 1.5, 0.375),  # Kick on 3
    (42, 1.875, 0.125),  # Hihat on 3&
    (42, 2.0, 0.125),  # Hihat on 4&
    (38, 2.25, 0.375),  # Snare on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Everyone in (1.5 - 3.0s)

# Bass: walking line in F (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    (78, 1.5, 0.375),  # F2
    (80, 1.875, 0.375),  # G2
    (77, 2.25, 0.375),  # E2
    (79, 2.625, 0.375),  # F#2
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chords each bar, resolve on the last
# Bar 2: Fmaj7
piano_notes = [
    (65, 1.5, 0.375),  # F
    (69, 1.5, 0.375),  # A
    (72, 1.5, 0.375),  # C
    (76, 1.5, 0.375),  # E
]

# Bar 3: Bbmaj7
piano_notes.extend([
    (62, 2.25, 0.375),  # Bb
    (66, 2.25, 0.375),  # D
    (69, 2.25, 0.375),  # F
    (73, 2.25, 0.375),  # A
])

# Bar 4: Emaj7
piano_notes.extend([
    (60, 3.0, 0.375),  # E
    (64, 3.0, 0.375),  # G
    (67, 3.0, 0.375),  # B
    (71, 3.0, 0.375),  # D
])

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F - G - D - F
sax_notes = [
    (84, 1.5, 0.375),  # F
    (87, 1.875, 0.375),  # G
    (81, 2.25, 0.375),  # D
    (84, 3.0, 0.375),  # F
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Drums continue (2.25 - 3.75s)
# Same pattern as bar 1
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 2.25, end=start + duration + 2.25))

# Bar 4: Drums continue (3.75 - 5.25s)
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 4.5, end=start + duration + 4.5))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save to file
# midi.write disabled
