
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
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on &1
    (1.125, 42, 100), # Hihat on &2
    (1.5, 38, 100),  # Snare on 3
    (1.875, 42, 100), # Hihat on &3
    (2.25, 42, 100), # Hihat on &4
    (2.625, 42, 100), # Hihat on &4
    (3.0, 36, 100),  # Kick on 1
    (3.75, 42, 100), # Hihat on &1
    (4.125, 42, 100), # Hihat on &2
    (4.5, 38, 100),  # Snare on 3
    (4.875, 42, 100), # Hihat on &3
    (5.25, 42, 100), # Hihat on &4
    (5.625, 42, 100), # Hihat on &4
    (6.0, 36, 100)   # Kick on 1
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: D -> F# -> B -> D (4 notes, ascending)
sax_notes = [
    (1.5, 62, 100, 0.25), # D4
    (1.75, 66, 100, 0.25), # F#4
    (2.0, 71, 100, 0.25), # B4
    (2.25, 62, 100, 0.25), # D4
    (2.5, 62, 100, 0.25), # D4 (rest)
    (2.75, 62, 100, 0.25), # D4 (rest)
    (3.0, 62, 100, 0.25)  # D4 (rest)
]
for time, note, velocity, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration))

# Bass: Walking line in D minor
bass_notes = [
    (1.5, 45, 100, 0.25), # D3
    (1.75, 47, 100, 0.25), # Eb3
    (2.0, 48, 100, 0.25), # E3
    (2.25, 45, 100, 0.25), # D3
    (2.5, 48, 100, 0.25), # E3
    (2.75, 50, 100, 0.25), # F#3
    (3.0, 52, 100, 0.25)  # G3
]
for time, note, velocity, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (1.75, 62, 100, 0.25), # D7 chord: D, F#, A, C
    (1.75, 67, 100, 0.25), # D7
    (1.75, 71, 100, 0.25), # D7
    (1.75, 74, 100, 0.25), # D7
    (2.25, 62, 100, 0.25), # D7
    (2.25, 67, 100, 0.25), # D7
    (2.25, 71, 100, 0.25), # D7
    (2.25, 74, 100, 0.25), # D7
    (2.75, 62, 100, 0.25), # D7
    (2.75, 67, 100, 0.25), # D7
    (2.75, 71, 100, 0.25), # D7
    (2.75, 74, 100, 0.25), # D7
    (3.25, 62, 100, 0.25), # D7
    (3.25, 67, 100, 0.25), # D7
    (3.25, 71, 100, 0.25), # D7
    (3.25, 74, 100, 0.25)  # D7
]
for time, note, velocity, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continuation of the motif, with variation
sax_notes = [
    (3.0, 62, 100, 0.25), # D4
    (3.25, 66, 100, 0.25), # F#4
    (3.5, 71, 100, 0.25), # B4
    (3.75, 69, 100, 0.25), # A4 (chromatic approach)
    (4.0, 62, 100, 0.25), # D4
    (4.25, 62, 100, 0.25), # D4 (rest)
    (4.5, 62, 100, 0.25)  # D4 (rest)
]
for time, note, velocity, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration))

# Bass: Walking line in D minor
bass_notes = [
    (3.0, 52, 100, 0.25), # G3
    (3.25, 54, 100, 0.25), # A3
    (3.5, 55, 100, 0.25), # Bb3
    (3.75, 52, 100, 0.25), # G3
    (4.0, 55, 100, 0.25), # Bb3
    (4.25, 57, 100, 0.25), # C4
    (4.5, 59, 100, 0.25)  # D4
]
for time, note, velocity, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (3.25, 62, 100, 0.25), # D7
    (3.25, 67, 100, 0.25),
    (3.25, 71, 100, 0.25),
    (3.25, 74, 100, 0.25),
    (3.75, 62, 100, 0.25),
    (3.75, 67, 100, 0.25),
    (3.75, 71, 100, 0.25),
    (3.75, 74, 100, 0.25),
    (4.25, 62, 100, 0.25),
    (4.25, 67, 100, 0.25),
    (4.25, 71, 100, 0.25),
    (4.25, 74, 100, 0.25),
    (4.75, 62, 100, 0.25),
    (4.75, 67, 100, 0.25),
    (4.75, 71, 100, 0.25),
    (4.75, 74, 100, 0.25)
]
for time, note, velocity, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Resolution of the motif
sax_notes = [
    (4.5, 62, 100, 0.25), # D4
    (4.75, 66, 100, 0.25), # F#4
    (5.0, 71, 100, 0.25), # B4
    (5.25, 62, 100, 0.25), # D4
    (5.5, 62, 100, 0.25), # D4 (rest)
    (5.75, 62, 100, 0.25), # D4 (rest)
    (6.0, 62, 100, 0.25)  # D4 (rest)
]
for time, note, velocity, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration))

# Bass: Walking line in D minor
bass_notes = [
    (4.5, 59, 100, 0.25), # D4
    (4.75, 61, 100, 0.25), # Eb4
    (5.0, 62, 100, 0.25), # E4
    (5.25, 59, 100, 0.25), # D4
    (5.5, 62, 100, 0.25), # E4
    (5.75, 64, 100, 0.25), # F#4
    (6.0, 66, 100, 0.25)  # G4
]
for time, note, velocity, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (4.75, 62, 100, 0.25), # D7
    (4.75, 67, 100, 0.25),
    (4.75, 71, 100, 0.25),
    (4.75, 74, 100, 0.25),
    (5.25, 62, 100, 0.25),
    (5.25, 67, 100, 0.25),
    (5.25, 71, 100, 0.25),
    (5.25, 74, 100, 0.25),
    (5.75, 62, 100, 0.25),
    (5.75, 67, 100, 0.25),
    (5.75, 71, 100, 0.25),
    (5.75, 74, 100, 0.25),
    (6.25, 62, 100, 0.25),
    (6.25, 67, 100, 0.25),
    (6.25, 71, 100, 0.25),
    (6.25, 74, 100, 0.25)
]
for time, note, velocity, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration))

# Drums: Bar 3 and 4
drum_notes = [
    (3.0, 36, 100),  # Kick on 1
    (3.75, 42, 100), # Hihat on &1
    (4.125, 42, 100), # Hihat on &2
    (4.5, 38, 100),  # Snare on 3
    (4.875, 42, 100), # Hihat on &3
    (5.25, 42, 100), # Hihat on &4
    (5.625, 42, 100), # Hihat on &4
    (6.0, 36, 100)   # Kick on 1
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save to a file
midi.write("dante_intro.mid")
