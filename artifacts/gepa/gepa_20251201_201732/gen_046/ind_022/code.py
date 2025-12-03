
import pretty_midi

# Initialize MIDI with 160 BPM (4/4 time)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick (36), snare (38), hihat (42)
drum_kick = 36
drum_snare = 38
drum_hihat = 42

# Bar 1 (0.0 - 1.5s): Drums only — Little Ray sets the mood
drum_notes = [
    (0.0, drum_kick, 100),   # Kick on beat 1
    (0.375, drum_hihat, 80), # Hihat on beat 1&2
    (0.75, drum_snare, 100), # Snare on beat 2
    (1.125, drum_hihat, 80), # Hihat on beat 2&3
    (1.5, drum_kick, 100)    # Kick on beat 3
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Bar 2 (1.5 - 3.0s): Full quartet — start of the motif
## Drums
drum_notes = [
    (1.5, drum_kick, 100),
    (1.875, drum_hihat, 80),
    (2.25, drum_snare, 100),
    (2.625, drum_hihat, 80),
    (3.0, drum_kick, 100)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

## Bass (Marcus) — walking line in Fm (F, Ab, Bb, D)
# Root (F2), fifth (C3), chromatic approach up (Eb3)
bass_notes = [
    (1.5, 72, 90),    # F2
    (1.875, 76, 90),  # Ab2 approached from G (chromatic)
    (2.25, 74, 90),   # Bb2
    (2.625, 77, 90),  # D2 approached from C# (chromatic)
    (3.0, 72, 90)     # F2
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

## Piano (Diane) — open voicings, unique chords per bar
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: D7 (D, F#, A, C)
piano_notes = [
    # Bar 2
    (1.5, 72, 80),     # F
    (1.5, 76, 80),     # Ab
    (1.5, 76, 80),     # C
    (1.5, 70, 80),     # Eb

    # Bar 3
    (2.25, 71, 80),    # Bb
    (2.25, 74, 80),    # D
    (2.25, 72, 80),    # F
    (2.25, 76, 80),    # Ab

    # Bar 4
    (3.0, 74, 80),     # D
    (3.0, 77, 80),     # F#
    (3.0, 79, 80),     # A
    (3.0, 72, 80)      # C
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

## Sax (Dante) — motif: F, Bb, F (staccato on Bb), open on F
sax_notes = [
    (1.5, 72, 95),     # F (start of motif)
    (1.75, 74, 95),    # Bb (staccato)
    (2.0, 72, 95),     # F (resolve)
    (3.0, 72, 95),     # F (repeat, open)
    (3.5, 72, 95)      # F (hold)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 3 (3.0 - 4.5s): Full ensemble continues
## Drums
drum_notes = [
    (3.0, drum_kick, 100),
    (3.375, drum_hihat, 80),
    (3.75, drum_snare, 100),
    (4.125, drum_hihat, 80),
    (4.5, drum_kick, 100)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

## Bass (Marcus) — walking line in Fm
bass_notes = [
    (3.0, 72, 90),    # F2
    (3.375, 76, 90),  # Ab2 approached from G
    (3.75, 74, 90),   # Bb2
    (4.125, 77, 90),  # D2 approached from C#
    (4.5, 72, 90)     # F2
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

## Piano (Diane) — Bb7 -> D7
piano_notes = [
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (3.0, 71, 80),    # Bb
    (3.0, 74, 80),    # D
    (3.0, 72, 80),    # F
    (3.0, 76, 80),    # Ab

    # Bar 4: D7 (D, F#, A, C)
    (3.75, 74, 80),   # D
    (3.75, 77, 80),   # F#
    (3.75, 79, 80),   # A
    (3.75, 72, 80)    # C
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

## Sax (Dante) — motif repeat + slight variation
sax_notes = [
    (3.0, 72, 95),     # F (repeat)
    (3.25, 74, 95),    # Bb (staccato)
    (3.5, 72, 95),     # F (resolve)
    (4.5, 72, 95),     # F (hold)
    (5.0, 72, 95)      # F (end)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 4 (4.5 - 6.0s): Final bar — full quartet, sax holds the F
## Drums
drum_notes = [
    (4.5, drum_kick, 100),
    (4.875, drum_hihat, 80),
    (5.25, drum_snare, 100),
    (5.625, drum_hihat, 80),
    (6.0, drum_kick, 100)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

## Bass (Marcus) — walking line in Fm
bass_notes = [
    (4.5, 72, 90),    # F2
    (4.875, 76, 90),  # Ab2 approached from G
    (5.25, 74, 90),   # Bb2
    (5.625, 77, 90),  # D2 approached from C#
    (6.0, 72, 90)     # F2
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

## Piano (Diane) — D7 (D, F#, A, C) to end
piano_notes = [
    (4.5, 74, 80),    # D
    (4.5, 77, 80),    # F#
    (4.5, 79, 80),    # A
    (4.5, 72, 80)     # C
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

## Sax (Dante) — hold the final F
sax_notes = [
    (4.5, 72, 95),
    (5.5, 72, 95),
    (6.0, 72, 95)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
# midi.write disabled
