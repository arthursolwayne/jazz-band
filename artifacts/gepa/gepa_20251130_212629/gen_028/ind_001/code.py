
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    (36, 0.0, 0.5),
    (36, 1.0, 0.5),
    # Snare on 2 and 4
    (38, 0.5, 0.5),
    (38, 1.5, 0.5),
    # Hi-hat on every eighth
    (42, 0.0, 0.25),
    (42, 0.25, 0.25),
    (42, 0.5, 0.25),
    (42, 0.75, 0.25),
    (42, 1.0, 0.25),
    (42, 1.25, 0.25),
    (42, 1.5, 0.25)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 2: Everyone in (1.5 - 3.0s)
# Sax melody - One short motif, make it sing. Start it, leave it hanging.
sax_notes = [
    (62, 1.5, 0.375),  # D4
    (66, 1.875, 0.375), # F#4
    (65, 2.25, 0.375),  # F4
    (62, 2.625, 0.375)  # D4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass - Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (50, 1.5, 0.5),  # D3
    (51, 2.0, 0.5),  # Eb3
    (49, 2.5, 0.5),  # C#3
    (50, 3.0, 0.5)   # D3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=start, end=start + duration))

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    (62, 2.0, 0.5),  # D7 (D, F#, A, C)
    (67, 2.0, 0.5),  # A
    (69, 2.0, 0.5),  # Bb
    (64, 2.0, 0.5),  # F#
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Bar 3: Everyone in (3.0 - 4.5s)
# Sax melody continues with variation
sax_notes = [
    (66, 3.0, 0.375),  # F#4
    (65, 3.375, 0.375), # F4
    (62, 3.75, 0.375),  # D4
    (60, 4.125, 0.375)  # B3
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass continues walking
bass_notes = [
    (51, 3.0, 0.5),  # Eb3
    (52, 3.5, 0.5),  # E3
    (53, 4.0, 0.5),  # F3
    (50, 4.5, 0.5)   # D3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=start, end=start + duration))

# Piano continues comping
piano_notes = [
    (62, 3.5, 0.5),  # D7 (D, F#, A, C)
    (67, 3.5, 0.5),  # A
    (69, 3.5, 0.5),  # Bb
    (64, 3.5, 0.5),  # F#
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    # Kick on 1 and 3
    (36, 3.0, 0.5),
    (36, 4.0, 0.5),
    # Snare on 2 and 4
    (38, 3.5, 0.5),
    (38, 4.5, 0.5),
    # Hi-hat on every eighth
    (42, 3.0, 0.25),
    (42, 3.25, 0.25),
    (42, 3.5, 0.25),
    (42, 3.75, 0.25),
    (42, 4.0, 0.25),
    (42, 4.25, 0.25),
    (42, 4.5, 0.25)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 4: Everyone in (4.5 - 6.0s)
# Sax ends with a question
sax_notes = [
    (60, 4.5, 0.25),  # B3
    (62, 4.75, 0.25), # D4
    (60, 5.0, 0.25),  # B3
    (62, 5.25, 0.25), # D4
    (60, 5.5, 0.25),  # B3
    (62, 5.75, 0.25)  # D4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass ends on D3
bass_notes = [
    (50, 4.5, 1.5)  # D3 (held to end of bar)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=start, end=start + duration))

# Piano ends with a 7th chord
piano_notes = [
    (62, 4.5, 0.5),  # D
    (67, 4.5, 0.5),  # A
    (69, 4.5, 0.5),  # Bb
    (64, 4.5, 0.5)   # F#
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Drums end
drum_notes = [
    # Kick on 1 and 3
    (36, 4.5, 0.5),
    (36, 5.5, 0.5),
    # Snare on 2 and 4
    (38, 5.0, 0.5),
    (38, 6.0, 0.5),
    # Hi-hat on every eighth
    (42, 4.5, 0.25),
    (42, 4.75, 0.25),
    (42, 5.0, 0.25),
    (42, 5.25, 0.25),
    (42, 5.5, 0.25),
    (42, 5.75, 0.25),
    (42, 6.0, 0.25)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
